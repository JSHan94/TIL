# TXGX

Tech Forum by Ground X, 2019년도 발표 요약<br/>
[영상링크](https://www.youtube.com/playlist?list=PLKqrwxupttYFng6AOQTXHp2DEHNIQMJSC) <br/>
[기술 블로그](https://medium.com/klaytn)

# Klaytn World: From Inception to Completion

<p>
  기존 블록체인 프로젝트들은 처리량, 트랜잭션 소요시간이 너무 큼. 이를 해결하기 위해 클레이튼을 제안함. <br/>
  Finality를 위해 <b>PBFT 기반의 합의알고리즘을 선택하고 TX를 전파하는 채널을 다양하게 만들어</b> 처리량을 높히고자함.<br/>
  TX가 단일 채널에 몰리면 병목현상이 심하기 때문에 <b>멀티 채널을 통해 병렬화</b>하고자함.<br/>
  또한 블록의 정보(Block, Receipt, State 등)가 스토리지에 저장이 되어야하는데, 단일 스토리지에 저장하기에는 시간이 많이 걸림. &rarr; <b>DB 파티션</b> 진행<br/>
  Only State trie cache 를 <b>State trie node cache</b>로 구현 함(?, 잘 이해가 안 됨)<br/>
  클레이튼은 기존의 더 나은 UX를 위해 어카운트 모델을 변경함.<br/>
  기존에는 개인키와 매칭되던 공개키에 대응하는 지갑 Address가 존재하였는데, 이는 개인키가 변경되면 지갑 주소도 변경되어야하는 불편함이 있음<br/>
  이를 개선하기 위해, 클레이튼은 <b>Address와 공개키의 관계를 과감하게 끊어내서 개인키가 바뀌더라도 백업키 등으로 지갑주소를 그대로 사용</b>할 수 있도록함.<br/>
  또한 단일 트랜잭션 포맷에 맞춰서 트랜잭션을 만드는 것은 불편하기 때문에 개발자를 위해 <b>native transaction type을 지원</b> 함.<br/>
  즉, 성능적 측면과 사용자적인 측면에서 개선하고자 노력 함.<br/>
  이외에도 SDK, Explorer 등 개발자들이 쉽게 클레이튼 네트워크에 참여할 수 있는 채널을 만들어 두었음.<br/>
</p>


# Klatyn's Network Architecture and Consensus

<p>
  기존 분산 네트워크의 낮은 처리량과 불확실한 지연 시간이 문제임<br/>
  모든 노드가 동등하냐라는 질문을 하게되고 이를 통해 노드를 3가지 레이어로 나누게 됨<br/>
  <ul>
  <li/>Consensus Node(CN) : 블록 생성을 전담, 신뢰할 수 있는 엔터티(컨소시엄)들이 관리할 수 있도록 함 / 담합의 문제, 공격 대상이 한정되서 위험성 증가<br/>
  <li/>Proxy Node Network(PN) : 외부 EN으로부터 받은 트랜잭션을 CN 및 인근 PN에게 전달하고, CN에서 생성된 블록을 EN에 전파<br/>
  <li/>Endpoint Node Network(EN) : 서비스나 사용자의 트랜잭션을 PN에 보내는 역할을 함.<br/>
  </ul>
  블록 생성은 Permissioned하게 하고, 사용자들은 제한 없이 네트워크에 참여할 수 있도록 함. (분산 시스템의 한계인듯..)<br/>
  BFT : 즉각적인 Finality / 높은 트랜잭션 메세지 교환(n^2)<br/>
  Klaytn은 Committee 를 추가하여 한 블록을 검증하기 위해 랜덤하게 선택된 CN 노드를 통해 메세지 수를 줄임(이러면 BFT의 1/3 이하의 악의적 공격에 Tolerance하지 않을 것 같은데?)<br/>
  이를 방지하기 위해서 CN 노드들이 Klay를 예치하고 유지하게 해서 악의적 공격을 방지하도록 노력함<br/>
  또한 Klaytn은 PoS의 블록생성의 불평등을 막기 위해 Gini 계수를 도입함. Staking된 값에 따라 Slot을 생성하여 랜덤하게 셔플하여 블록을 생성 함<br/>
  Reward는 Proposer,PoC(Proof of Contribution),KIR(Klaytn Improvement Reserve)로 나뉘어져서 분배됨<br/>
  블록이 특정한 문제로 제대로 동작되지 않을 때(Proposer가 블록을 제안하지 않거나, prepare나 commit에서 2/3 이상 Voting을 못받는 경우) -> Roundchange 진행<br/>
</p>


# Account and Transaction Model in Klaytn

<p>
  Account : 유저와 컨트랙트의 정보를 저장하는 데이터 구조 (Nonce, Balance, CodeHash, Storage Root 등)<br/>
  Transaction : 블록체인의 State를 변경하는 기능<br/>
  클레이튼은 세가지 관점에서 Mass adoption을 노력함 : 사용자 관점, 서비스 제공자 관점<br/>
  <b>사용자 관점</b>
  <ul>
  <li/>개인키가 유출되면 새로운 개인키를 발급할 수밖에 없는데, 이 때문에 Address가 변경되어야 하는 것은 너무 불편함. 또한 Tx History도 잃는 것이 문제임
  <li/>이를 위해 Public key와 Address의 관계를 끊고 Account에 Public key라는 데이터 타입을 추가함
  <li/>또한 Account의 Security를 위해 Multisig를 구현하고자 하였음. 근데 이는 스마트 컨트랙트 등으로 구현하기는 어려워 플랫폼 수준으로 낮춰서 멀티시그 기능을 개발함.
  </ul>
  <b>서비스 제공자 관점</b> 
  <ul>
  <li/>Fee delegation과 같이 트랜잭션 Fee를 서비스 제공자가 낼 수 있게하여 다양한 방법으로 사용자를 끌어들일 전략을 세울 수 있게함.
  <li/>이를 위해 트랜잭션에 Fee payer address, Fee payer signature 필드를 추가함.
  <li/>Sender가 Fee Payer에게 전달하고, 이것이 클레이튼에 기록되게 함. (이렇게 하면 트랜잭션이 복잡해지니 Fee cost가 증가하지는 않는가?)
  <li/>Accout에 Role이 다르기 때문에 이를 위해 어카운트에 추가 된 Key 필드를 확장함; Public key, Multiple public keys, Role-based keys
  <li/>서비스 제공자가 사용자가 키를 분실하여도, RoleUpdate를 해줌으로 특정 계정을 계속 사용할 수 있도록 하는 것이 가능함
  <li/>Explicit한 타입을 제공하고자 노력함
  </ul>
  <b>플랫폼 개발자 관점</b>
  <ul>
  <li/>어카운트 타입을 컨트랙트와 유저로 분리하였음(이더리움에서 EOA와 CA 구별하기 힘들었던 기억이..)
  <li/>User Account에 Codehash등이 포함되지 않아도 되서 저장 용량 감소의 효과 또한 있음
  <li/>트랜잭션 타입도 이와 유사하게 분리하여 스토리지 코스트를 감소하는 것도 가능했음
  </ul>
  이외에도 Human-readable address, Account와 트랜잭션 타입을 더 늘리고자 함
</p>

# Data Layer Architecture & Optimizations

<p>
  <b>기존 데이터 레이어(메모리 & 디스크)의 문제</b>
  <ul>
  <li/>State trie : 어카운트의 데이터를 저장하는 자료 구조. Merkle Patricia Trie 구조가 주로 사용됨. 
  <li/>어카운트 개수가 늘어나면 Trie가 커지기 때문에 메모리 상에서 관리가 불가능함 -> 디스크 영역에서 관리
  <li/>key-value store DB. 하나의 LevelDB에 모든 데이터(Block, Receipts, State 등)를 저장함
  <li/>필요한 데이터를 가져오기 위해 디스크에 접근해야하는데 이는 상당한 성능 저하를 가져올 수 있음. 이런 병목 현상을 줄이기 위해 노력해야함.
  </ul>
  <b>클레이튼의 시도</b>
  <img src="https://raw.githubusercontent.com/JSHan94/TIL/main/Blockchain/Klaytn/images/%6019%20TXGX_Data%20Layer%20Architecture%20%26%20Optimizations_1.PNG"/>
  <ul>
  <li/>메모리 영역에서 State Trie Node Cache를 추가하여 디스크 영역 접근을 줄여줌
  <li/>데이터 종류에 따라 DB를 파티셔닝하여 병렬 처리를 가능하게 함(파티셔닝)
  </ul>
  <b>블록체인 데이터를 줄일 수 있는 방법에 대한 연구</b>
  <img src="https://raw.githubusercontent.com/JSHan94/TIL/main/Blockchain/Klaytn/images/%6019%20TXGX_Data%20Layer%20Architecture%20%26%20Optimizations_2.jpg"/>
  <ul>
  <li/>블록체인은 append-only기 때문에 데이터는 증가하기만함.
  <li/>일반적인 사용자들은 최신 state 데이터만 알고 싶어함. 전체 History에 대해는 큰 관심이 없을 것이라 생각되어 요청 수가 적을 것이라고 가정.
  <li/>최신상태를 계속 업데이트하면서 지나간 데이터를 삭제하고자함 &rarr; 특정 블록 넘버를 기준으로 덮어 DB를 migration 함
  <li/>마이그레이션은 추가적으로 해야되는 작업이므로 trade-off를 잘 핸들링 해야함
  </ul>
</p>

# Horizontal Scaling through Service Chain in Klaytn

<p>
  <b>서비스체인을 사용하는 이유</b>
  <ul>
    <li/>테스트 용도 : Mainnet/Testnet과 별도로 자체 테스트 시
    <li/>Token 전용 DB : token 정보 관리에 최적화된 database로 사용하고 싶을 때
    <li/>비용 : Public blockchain의 사용 비용이 부담될 때
    <li/>신뢰 : 자체 블록체인이지만, Mainnet과 연결하여 User의 신뢰를 얻고 싶을 때(Anchoring)
    <li/>보안 : Chain data를 공개하고 싶지 않거나 네트워크 접근권한을 한정하고 싶을 때
    <li/>성능 : 높은 TPS가 요구되는 서비스를 위해
    <li/>커스터마이징 : 다양한 feature를 수정하는 것이 가능함
  </ul>
  <b>Anchoring</b>
  <ul>
  <li/>서비스 제공자가 사용자들의 신뢰를 얻기 위해 주기적으로 서비스 체인 데이터를 Main-chain에 기록하는 것
  <li/>Integrity : 데이터 변조를 탐지하는 것이 가능함
  <li/>Statistics : 서비스체인의 통계자료를 얻는 것이 가능함
  </ul>
  <b>Value Transfer</b>
  <ul>
  <li/>Bridge contract를 이용해서 Mint와 Burn을 통해 Value Transfer을 하게 함
  <li/>그렇지만 이 같은 방식은 2번의 TX를 요구하기 때문에 UX가 좋지 못함
  <li/>클레이튼은 이를 위해 1개의 TX만으로 Value Transfer가 일어나도록 함
  <li/>또한 Multi-channel을 통해 서비스 체인과 통신의 병목현상을 막았으며, Multi-sig를 통해 다수의 operator의 승인을 요구할 수 있음
  </ul>
</p>
