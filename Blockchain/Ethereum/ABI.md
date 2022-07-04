# Application Binary Interface (ABI) in Etheruem Virtual Machine (EVM)

- 블록의 트랜잭션에 binary 형태로 저장되어 있는 이더리움 스마트컨트랙트 코드는 이더리움 클라이언트에 구현된 EVM에 의해 동작함
- EVM은 Opcode라는 instruction을 지원하고 이는 프로세서의 instruction set과 유사하게 동작하는 low-level 코드임 (자세한 내용은 백서에 포함되어있음)
- EVM에게 있어서 Smart contract는 **byte 시퀀스로 이루어진 하나의 프로그램**에 불과함
- External application이나 다른 스마트 컨트랙트가 블록체인과 상호작용하기 위해서는 스마트 컨트랙트의 매서드나 파라미터 등의 정보를 알기 위한 **interface**가 필요함
- 이 때 이용되는 것이 ABI임

# Feature

- API와 같이 human-readable하거나 high-level language 형태 임
- EVM에서 바이너리 데이터로 저장되어진 컴파일 코드와 human-readable 인터페이스는 사라지고, 스마트컨트랙트 인터렉션은 EVM이 해석할 수 있도록 바이너리 형태가 되어야함
- ABI는 Binary contract와 쉽게 인터렉트 할 수 있도록 매서드나 structure를 정의해줌
- ABI는 호출자가 필요한 정보를 정해주고 VM이 이해할 수 있도록 인코딩을 하는데, 이 과정을 **ABI encoding**이라 함
- ABI는 두 프로그램 모듈 사이의 인터페이스임 (그중 하나는 machine code 수준)

# Examples

### Contract

```solidity

// Solidity program to
// demonstrate abi encoding
pragma solidity >=0.4.22 <0.7.0;
  
// Creating a contract
contract Storage 
{
    // Declaring a state variable
    uint256 number; 
  
    // Defining a function
    // to store the number  
    function store(uint256 num) public 
    {
        number = num;
    }
  
    // Defining a function to 
    // send back or return the 
    // stored number
    function retrieve() public 
             view returns (uint256)
    {
        return number;
    }
}
```

### ABI.json
```json
[
    {
        "inputs": [],
        "name": "retrieve",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "stateMutability": "view",
        "type": "function"
    },
    {
        "inputs": [
            {
                "internalType": "uint256",
                "name": "num",
                "type": "uint256"
            }
        ],
        "name": "store",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]
```

