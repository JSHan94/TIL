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

