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

