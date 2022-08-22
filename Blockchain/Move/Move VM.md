# Move Spec
- Move VM의 인스턴스화는 empty table (Hashmap and Vec behind Mutex)인 `Loader` 인스턴스 초기화로 시작
    - `Loader` 는 효율적인 code cache임
    - code cache는 lifetime을 가지고 code는 함수나 script가 실행되는 런타임에 호출됨
    - 로드가 되면 모듈과 스크립트는 로드된 형태로 재사용되며 즉시 실행할 준비가 됨
    - 코드를 로드하는 것은 비용이 비싸고 VM은 eager loading(즉시 로딩)을 수행함
- Execution이 실행되면 더이상 코드 로딩이 없고 모든 코드는 실행되고 load time에 캐시될 준비가 됨
    - Eager model이 런타임에러가 linking에서 발생하지 않는다는 것을 보장하고 given invocation은 다른 코드 path 때문에 로딩과 링킹이 실패하지 않을 것임
    - invocation의 지속성은 execution이 시작하기 전에 보장됨
    - runtime 에러는 가능하며 예상되어짐
- 이 모델은 전형적인 블록체인의 요구사항에 만족함
    - Validation은 genesis에서 생성된 일부 함수만 사용하고, 일단 load 되면 코드는 cached로 부터 즉시, 항상 fetch되어짐
    - Execution은 data view (stable하고 immutable한)의 context임. code 또한 stable하기 때문에 loading 과정을 최적화 하는 것이 중요함. 또한 트랜잭션은 homogeneous하고 코드 재사용은 performance와 stability 향상을 일으킴
- VM은 데이터 캐시 일관성을 위한 내부 구현이 있음 (클라이언트의 부담을 덜어냄) -> `Session`(런타임에 유일한 통신 방법)
    - `Session`의 목적은 VM에 invocation set을 위한 데이터 캐시를 생성하고 관리하는 것
    - 또한 side effect를 adapter에 적절한 형태로 반환하기 위해 사용
    - `Session`은 call을 VM의 `Runtime`(논리 및 구현이 실행되고 시작되는)으로 보냄

## Code cache
- 모듈을 로딩할 때 VM은 모듈의 데이터 스토어에 쿼리를 함
    - 해당 Binary는 로더에 의해 deserialized, verified, loaded, cached 됨
    - 로드되면 모듈은 VM instance의 lifetime동안 절대 재요청하지 않음
    - Code는 시스템에서 immutable한 리소스임
- 로딩의 과정은 다음과 같은 과정으로 진행됨
    1. `Binary` (serialized된 모듈), `Vec<u8>` (data store로 부터 fetch되어진 것). 이들은 네트워크 접근을 요청할 수 있음
    2. binary는 deserialized되고 verified 됨
    3. 모듈의 dependencies가 로드됨 (1~4의 각 dependecy에 대해 반복됨)
    4. 모듈이 해당되는 dependcy에 링킹되고 (runtime동안 적절한 형태로 변형됨) loader에 의해 캐싱됨
- 로딩된 모듈의 reference는 network나 verification이나 transformation로부터 runtime structure로 어떠한 fetching도 수행하지 않음 (e.g. linking)
- 일반적인 client의경우 code cache의 consistency가 adapter가 재시작 때까지 진행중인 트랜잭션을 멈추는 hard upgrade를 수행하는 시스템 트랜잭션에 의해 깨질수 있음
    - 다른 클라이언트는 다른 code model을 가질 수도 있음 (e.g. 다른 versioning의 형태)
- 정리하면, Move VM 인스턴스를 홀딩하고 있는 클라이언트는 code cache의 행동을 알고 있어야하고 로드된 코드와 호환되는 data view(`DataStore`)를 제공해야함
    - 또한 클라이언트는 특정 조건이 code cache의 consistency를 바꿀 때 새로운 VM을 릴리즈하고 인스턴스화할 책임이 있음

## Publishing
- Client는 calling을 통해 시스템 안에있는 모듈을 publish함
```rust
pub fn publish_module(
    &mut self,
    module : Vec<u8>,
    sender : AccountAddress,
    gas_status : &mut impl GasMeter,
) -> VMResult<()>;
```
- module은 serialized 형태로 있으며 VM은 다음과 같은 과정을 수행함
    - Deserialize Module
        - 모듈이 deserialize 하지 않으면 에러를 발생 (with a proper `StatusCode`)
    - 모듈 주소를 확인하고 sender address와 동일한 지 확인함
        - publisher가 모듈을 소유하고 있는 account인지를 검증함
        - 만약 두 address가 일치하지 않으면 에러 발생 (`StatusCode::MODULE_ADDRESS_DOES_NOT_MATCH_SENDER`)
    - 모듈이 이미 publish 되었는 지를 확인함
        - Code는 Move에서 immutable함
        - existing module을 overwrite하려는 시도는 에러를 발생 (`StatusCode::DUPLICATE_MODULE_NAME`)
    - Verify loading
        - VM은 correctness를 검증하기 위해 모듈의 verification을 수행함
        - 하지만 어떠한 모듈의 디펜던시도 캐시에 저장되진 않음
        - VM은 모듈이 reference가 발견될 때 호출되도록 보장함
        - 만약 모듈이 로드하는데 실패하면 에러 발생
    - Publish
        - VM은 모듈의 serialized bytes를 proper key로 storage에 write함
        - 이후 모듈의 어떠한 reference도 valid함

## Script Execution
- VM은 script의 실행을 허용함
    - script는 `script` 블록에 선언된 Move 함수이고 logical transaction을 달성하기 위해 온체인에 퍼블리시하는 프레임워크에 call을 수행함
    - script는 storage에 저장되어지지 않고 **다른 스크립트나 모듈에 의해 호출되어지지 않음**
```rust
pub fn execute_script(
    &mut self,
    script: Vec<u8>,
    ty_args : Vec<TypeTag>,
    args : Vec<Vec<u8>>,
    senders : Vec<AccountAddress>,
    gas_status : &mut impl GasMeter,
) -> VMResult<()>;
```
- `script`는 serialized 된 형태임
    - script가 generic하다면 `ty_args` 벡터는 type argument에 대해 `TypeTag` 값을 포함함.
    - 스크립트에 대한 `signer` 어카운트 어드레스는 `sender` 벡터에 정의되어짐
    - 다른 추가적인 인자는 `args` 벡터에 (각 인자가 BCS-serialized vector of bytes) 제공되어짐
- VM은 다음과 같은 과정을 진행함
    - Load script and Main function
        - 스크립트 바이너리의 `sha3_256` 해시 값을 계산함
        - 해시는 스크립트 캐시에 접근하는 데 사용되어지고 이 해시는 스크립트의 identity를 위해 사용되어짐
        - 만약 캐시에 없다면, 스크립트가 로드됨. 로딩이 실패하면, execution은 정지하고 에러가 발생
        - 스크립트 메인 함수는 type argument 인스턴스화에 대해 확인됨. 만약 에러가 있다면 execution은 정지하고 에러가 밸생함
    - Build argument list
        - 첫번째 인자는 sender vector에 있는 account address를 VM에 의해 생성된 `Signer`임
        - `args` vector로 부터의 다른 인자들은 허용된 타입인지 whitelisting되고 script의 인자로 추가됨
        - 타입이 허용되지 않을 경우 에러 발생 (`StatusCode::TYPE_MISMATCH`)
    - Execute Script
        - VM은 스크립트를 실행할 인터프리터를 가져옴
        - 실행 도중 에러가 발생하면 트랜잭션은 취소됨
        - VM은 실행결과가 성공인지 실패인지 반환함

## Script Function Execution
- Script Function은 Move bytecode가 Move의 온체인 모듈에 있는 script visibility에서 부터 온 것을 제외하고는 script와 유사함
```rust
pub fn execute_script_function(
    &mut self,
    module : &ModuleId,
    function_name : &IdentStr,
    ty_args : Vec<TypeTag>,
    args : Vec<Vec<u8>>,
    senders : Vec<AccountAddress>,
    gas_status : &mut impl GasMeter,
) -> VMResult<()>;
```
- Script function을 실행하는 것은 script와 유사함
    - 대신 script function은 on-chain module로 부터 bytecode를 가져옴
    - Move VM은 script visibility를 가졌는지 확인함
    - 나머지 script function 실행은 script와 동일함
    - fucntion이 존재하지 않으면 (`FUNCTION_RESOLUTION_FAILURE`), 함수가 script visibility를 가지고 있지 않으면 (`EXECUTE_SCRIPT_FUNCTION_CALLED_ON_NON_SCRIPT_VISIBLE`) 에러 발생

## Function Execution
- VM은 함수 이름과 `ModuleId`를 통해 모듈 안에 있는 함수를 실행시키는 것을 허용함
    - Function 이름은 모듈 내에서 유니크하며 overloading을 지원하지 않음
    - 그렇기에 function signature가 필요하지 않음
    - argument checking은 interpreter에 의해 수행됨
- Adapter는 validation과 execution으로 설명되는 특정 시스템 함수 실행을 하는 이 entry point를 사용함
    - 이는 시스템이 visibility 체크가 없는 entry point임
    - 클라이언트는 이 엔트리포인트를 내부적으로 사용 (genesis를 만들거나)하거나 wrap하여 제약을걸어 expose함
```rust
pub fn execute_function(
    &mute self,
    module : &ModuleId,
    function_naem :&IdenStr,
    ty_args : Vec<TypeTag>,
    args : Vec<Vec<u8>>,
    gas_status  : &mut impl GasMeter,
) -> VMResult<()>;
```
- VM 동작 과정
    - Load function
        - 명세된 module이 먼저 호출됨
        - VM은 모듈에서 함수를 찾음
        - `ty_args`에 있는 모든 타입이 호출됨. Type 인자는 mismatch가 있는 지를 체크함
    - Build argument list
        - 인자는 whitelisting된 허용 타입인지 체크됨
    - Execute function
        - VM은 함수를 실행하는 interpreter를 호출함