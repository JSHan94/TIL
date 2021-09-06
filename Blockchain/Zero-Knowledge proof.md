# Motivation

Interactive proof system : prover 와 verifier 상호 간 메세지를 교환하는 컴퓨테이션을 모델링한 abstract machine을 뜻함 

기존 Interactive proof system에서는 다음과 같이 가정하였음

Prover : 무한정의 계산 자원을 가졌지만 **신뢰할 수 없는 존재**

Verifier : 한정된 계산 자원을 가졌지만 **신뢰할 수 있는 존재**

이런 전제하에서는 공격 시나리오에서 prover가 악역이었으며, 이들이 verifier를 공격하는 상황을 가정하였음

하지만 **verifier가 악의적일 수 있는 시나리오**에 대해 가정할 수가 있음 

이를 통해 다음과 같은 두 가지 질문에 대한 대답을 하고자 함

1. 누구나 verifier가 knowledge를 누설하지 않았다는 것을 확인할 수 있는가
2. verifier가 검증 과정 동안 알고 있어야 하는 knowledge의 비중은 어느 정도인가

이 의문점들을 해결하기 위해서 prover가 제공한 proof를 통해 악의적인 verifier가 검증을 수행할 수는 있지만 prover의 knowledge 자체에 대해서는 유추할 수 없는 시스템이 요구됨

이것이 바로 Zero Knowledge proof 

# Zero Knowledge proof (ZKP)

ZKP는 다음과 같은 조건이 만족되어야 함

1. Completeness : 어떤 조건이 참이라면, honest verifier는 honest prover에 의해 이 사실을 납득할 수 있다. (모든 정답 사례를 찾아낼 수 있다.)
2. Soundness : 어떤 조건이 거짓이라면, dishonest prover는 거짓말을 통해 verifier에게 조건이 참임을 절대 납득시킬 수 없다. (어떠한 오답 사례도 정답 사례라고 잘못 판단하지 않는다.)
3. Zero-Knowledge : 어떤 조건이 참일 때, verifier는 이 조건이 참이라는 사실 이외에 정보를 알 수 없다.

# Example

Case 1. Alibaba's Cave

양 갈래 동굴 안에 도어락이 있고, prover가 요구한 대로 나오는지 아닌 지를 여러번 반복하여 우연의 확률을 낮춤

유명한 case라 자세한 설명은 생략

Case 2. Finding Waldo

Case 3. Mini sudoku

# Non-interactive : Schnorr Identification Protocol

Non-Interactive : prover와 verifier의 메시지 교환을 최소화 하는 것을 의미, prover가 증명에 필요한 메시지를 보내고 연결이 끊어지더라도 메세지는 verifying 되어야한다는 것

Schnorr Protocol : 암호학에서, prover가 자신의 Private key를 공개하지 않고 이를 가지고 있다는 것을 증명하는 방법. 키 교환과 관련된 프로토콜로, 블록체인에 적용될 수 있는 예제

자세한 방법은 [해당 링크 참조]:(https://medium.com/decipher-media/zero-knowledge-proof-chapter-1-introduction-to-zero-knowledge-proof-zk-snarks-6475f5e9b17b)

# Structure of ZK Proof

구성 : 영지식 증명은 주어진 함수에 해당하는 회로, 주어진 회로에 대해서 입출력을 증명하고자 하는 증명자, 이를 검증하는 검증자

보통 검증자와 증명자는 서로 공유하는 키를 가짐. 이 키를 CRS (Common Reference String)이라 부르고 이는 RRS, SRS로 나뉨.

Interactive Proof : 증명을 위해 증명자와 검증자가 상호간의 통신하는 것. 검증자가 랜덤한 질의 값을 보내고, 해당 질의에 대해 알맞은 답을 증명자가 보내면 확실히 답을 알 것이라고 검증자가 믿게 됨

하지만 블록체인과 같은 경우에는 Interactive Proof를 하기 어렵기 때문에 랜덤 질의를 하는 것이 아니라 해시함수를 사용함. 

증명자의 입장에서는 해시의 출력값을 원하는 값으로 통제할 수 없기 때문에 해시의 출력값이 마치 자신에게 랜덤값과 같이 보이게 됨. 이런 방법을 피앗-샤미르(FS) 휴리스틱이라 부름. 비상호적인 증명 방식임

영지식에서 임의의 코드(f)에 대해서 주어진 입력(x)을 넣으면 해당 출력(x)이 나오는 것이 보장됨.

입출력이 f에 맞는 경우 x는 언어 L(f)에 속한다라고 이야기함

f를 수행할 때 비밀 입력(w)이 필요할 수 있는데, 영지식에서는 이를 Witness라고 부름.

(x;w)가 L(f)에 속한다는 것을 w를 보여주지 않고 증명하는 것이 영지식 증명이다.

영지식 증명은 크게 두가지로 나뉨

- 프론트엔드 : 산술 회로식을 만드는 부분
- 백엔드 : 산술 회로식에 대해서 증명을 생성하는 부분. Circuit Specific (주어진 회로에 맞는 SRS 키를 만드는 것) 과 Universal (회로에 상관 없이 SRS나 RRS를 Polynomial Commitment 기법을 통해 만드는 것) 방식 두가지로 나뉨

여기서 산술식이란 덧셈과 곱셈으로 식을 변환하는 것

## Circuit Specific ZK Proof

QAP (Quadratic Arithmetic Program) : 회로 표현 방식

- Pinocchio : n개의 곱셈 게이트를 가지는 QAP 형태로 주어진 회로에 대해서 증명자가 n에 비례하는 시간에 증명 생성 및 회로 크기와 상관없이 상수시간 검증
- Groth16 : Pinocchio를 더 개선한 것으로 작은 크기의 증명을 생성하는 영지식 증명법
- KLO19 : Groth16과 동일한 증명 크기로 시뮬레이션 추출이 가능한 기법이 개발

## Universal ZK Proof

Circuit Specific ZK Proof의 경우 회로에 대해서 각각 다른 SRS (Structured Reference String)를 생성해야하고 생성과정에서 비밀 정보를 사용하는데 이비밀 정보가 유출되면 증명이 조작하는 것이 가능하기 때문에 SRS 생성과정을 신뢰할 수 있어야만 한다는 단점이 있음. Universal ZK Proof는 회로에 상관없는 CRS (Common Reference String)을 만들어 두고 회로가 주어진 경우, 이에 대한 증명을 다항식 commitment에 의해서 증명하는 방식

여기서 신뢰 주체가 필요한 SRS 기반 기법과 필요 없는 RRS 기반 기법으로 나뉘어짐.

다음과 같은 것들이 이에 포함 됨
- Sonic
- Plonk : 가장 작은 다항식을 필요로 하기 때문에 가장 증명 크기가 작은 기법
- DARK : RRS
- Bulletproofs : 대수 기반 기법으로 벡터 내적연산 지원, 블록체인 회사에서 많이 채택함. RRS 기반. 하지만 검증 시간이 원래 회로 계산보다 오래 걸려 Plonk로 전환 중
- Stark : 양자 저항성을 가진 기법으로 FRI (Fast Reed-Solomon Interactive Oracle Proofs)에 기반.


# 참고자료

[Diving into the zk-SNARKs Setup Phase(Trusted setup 이유)](https://medium.com/qed-it/diving-into-the-snarks-setup-phase-b7660242a0d7)
[Zk-SNARKs: Under the Hood(비탈릭부테린 포스팅)](https://medium.com/@VitalikButerin/zk-snarks-under-the-hood-b33151a013f6)
