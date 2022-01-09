# State Machine 

블록체인은 기본적으로 상태머신(State Machine)임. 이는 **이전 상호 작용을 기억하도록 설계된 시스템**을 의미함. UTXO든 Account든 모두 State Machine의 체계를 따름.
사용자의 상호작용(트랜잭션)은 네트워크에서 브로드캐스트되어 새로운 블록을 생성하고 영구적으로 기록됨. 이 과정에서 새로운 상태로 업데이트가 됨.
UTXO와 Account의 차이는 이런 상태 변경이 되는 방법에서 차이가 있는 것임.

# UTXO

- UTXO : UTXO의 트랜잭션은 입력으로는 사용되지 않은 지출 목록(UTXO)를 받고, 출력으로는 새로운 UTXO를 만들어냄. 한 번 사용된 UTXO는 목록에서 제거 됨.
    - 동시에 여러 트랜잭션을 처리할 수 있는 **확장성**
    - 매 거래마다 새로운 주소를 활용하여 **(pseudo) 익명성**
    - UTXO는 한번 사용된 후 사라지기 때문에 이중 지불을 방지할 수 있음
    - UTXO가 과도하게 생성될 경우 흩어진 코인을 모두 모아야하는 번거로움과 불필요한 수수료를 내야할 문제가 생길 수 있음


# Account 

- Account : Global State가 각 계정의 Balance를 추적 함. 
    - 직관적이고 상태 추적이 가능한 **단순성** 
    - 거래 검증 시 충분한 잔액을 가지고 있는 지만 확인하면 되는 **효율성**
    - 하지만 이는 Double Spending의 가능성이 있어, 이더리움은 모든 계정이 공개적으로 볼 수 있는 nonce를 이용하여 두번 이상 제출 되는 것을 막음


# UTXO vs. Account Model

<img src="https://github.com/JSHan94/TIL/blob/main/Blockchain/images/UTXO%20vs%20Account.jpg"/>



