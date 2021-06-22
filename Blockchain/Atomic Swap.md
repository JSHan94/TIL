# Atomic swap

이종의 블록체인 네트워크 상에서 작동하는 서로다른 두 암호화폐를 교환 하는 기술.

# Process

Alice가 LTC를 Bob의 BTC로 교환한다고 가정

- Alice는 LTC를 금고역할을 하는 Smart Contract 주소에 입금
- 금고 생성 시 앨리스는 해당 금고에 접근가능한 Key 생성
- 해당 키의 암호화 해시를 Bob에게 공유 (Bob은 키 자체가 아닌 키의 해시값만을 알고 있기에 LTC에 접근 불가능)
- Bob은 Alice가 제공한 해시를 사용해 또 다른 금고 Smart Contract 주소를 생성하고 자신의 BTC 입금
- BTC를 수령하기 위해서 Alice는 동일한 키를 사용해야하고, 이를 통해 해당 키를 Bob에게 제공함 (Hash Lock 이라는 기능 때문에 가능)
- Alice가 BTC를 수령하자마자 Bob이 LTC를 수령하게 되며 Atomic swap가 종료 됨

Atomic이라는 용어는 이 Process가 하나라도 성립하지 않으면 전혀 진행되지 않는다는 사실과 관련있음.

만약 당사자 중 예정된 대로 진행하지 않을 시 자금은 자동으로 소유주에게 돌아가게 됨.

이 Process는 on-Chain과 off-chain 두 가지 방식으로 진행되는 것이 가능함.

on-chain은 swap 과정에 사용되는 블록체인 네트워크 중 하나에서 진행이 되며, off-chain은 second layer에서 진행이 됨.

이는 양 방향 지불 채널에 기반하며, Ligthning Network와 유사함.

# HTLC (Hash TimeLock Contract)

BTC 라이트닝 네트워크의 중요한 부분이며, 이는 hashlock과 timelock 두 가지 기능을 기본으로 함.

Hashlock은 데이터의 일부가 공개되지 않으면 자금이 사용되는 것을 방지하는 것.

Timelock은 contract가 사전에 설정된 기간 내에서만 실행되도록 하는 기능.

그렇기 때문에 HTLC는 Atomic swap가 부분적으로 실행되는 것을 방지하는 일련의 특정한 규칙들을 생성하여, 신뢰의 필요성을 제거함.

# 장점

탈중앙화.

개인 수수료가 매우 낮거나 없기 때문에 운용비용이 훨씬 저렴함.

높은 수준의 상호운용성을 통해 매우 빠르게 거래가 가능함.

# 한계점

필수적인 requirement가 존재함,

- 두 암호화폐가 동일한 해싱 알고리즘을 사용해야함 (BTC의 경우 SHA-256)
- 사용자의 프라이버시 침해 가능성이 존재함

# 참고자료

[Binance Academy](https://academy.binance.com/ko/articles/atomic-swaps-explained)
