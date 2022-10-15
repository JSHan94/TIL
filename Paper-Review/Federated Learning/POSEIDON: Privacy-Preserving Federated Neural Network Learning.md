# Motivation

다수의 데이터 제공자들 사이에서 데이터를 공유하는 것이 robust한 ML 모델을 위해서 필요함

하지만 다음과 같은 문제가 있음

- 데이터 공유가 어려움 : 민감정보, 프라이버시 규제, 사업 경쟁자
- ML 모델은 학습데이터에 대한 정보를 유출 함
- 개인 데이터를 사용하여 예측을 하는 것은 민감한 일임

이를 방지하기 위해 Privacy-Preserving Machine Learning (PPML)이 필요

# Current approaches

## Centralized

Raw 데이터나 Aggregate 데이터를 중앙 DB로 전송하는 방식

중앙 DB의 보안을 이용하여 데이터를 보호하기 때문에 신뢰할 수 있는 중앙 서버가 필요함

## Decentralized

**Federated Learning** : 모델에 데이터를 전달하지 않고 데이터로 로컬 모델을 업데이트 하는 방식을 사용함

- 여전히 모델은 sensitive함
- Intermediate 모델 업데이트를 공유하는 것은 여러 프라이버시 문제를 일으킴 (Extracting parties' inputs)

## Privacy-Preserving Decentralized

**Differential Privacy** : 데이터 소유자들 사이에서 private intermediate value를 차별적으로 교환함

- Utility degradating
- High privacy budget
- The achieved practical level of privacy remains unclrea

**Multiparty Computation** : 다수의 서버 모델을 secret-sharing 기법을 이용하여 운영함

- Trust를 분리할 서버의 수에 제한이 있음
- 컴퓨팅 서버 사이에 다수가 honest하다고 가정함
- 높은 컴퓨팅 오버헤드가 발생함

# POSEIDON

Multiparty homomorphic encryption을 이용하여 training 데이터와 resulting 모델, querier's evaluation 데이터를 분산 세팅에서 End-to-End 프로텍션을 제공함 

## System Model

N 데이터 제공자가 NN 모델을 학습할 각자의 데이터를 locally 가지고 있음

Querier 가 모델을 쿼리하고 evaluation data에서 예측 결과를 얻음

Parties는 커뮤니케이션 효용성을 위해 tree-network 구조로 연결되어 있음

## Treat Model

N-1 파티까지 collusion을 가진 **Passive-adversar model**

## Objective

Data Confidentiality : 트레이닝과 예측 도중에 어떤 party도 다른 honest party의 인풋 데이터에 대한 정보 이상을 학습할 수 없음

Model Confidentiality : 트레이닝과 예측 도중에 어떤 party도 학습 모델 이상의 정보를 가질 수 없음

## Soluation

**Multipary Homomorphic Encryption (MHE)** and **Federated Learning (FL)**

Local data는 데이터 제공자 premise에 항상 보관 됨

NN model의 weight는 항상 training과 evaluation도중에 암호화된 채로 보관 됨

### MHE

- **Public collective key** 는 모든 party가 알고 있음
- 이에 대한 **Scret key** 는 party들에게 분배되어 있음
- **Decryption** 은 파티들간의 collaboration을 요구함 
- 암호문을 리프레쉬하기 위한 효율적인 **Collaborative bootstrapping** 이 가능함

### FL

- 각 데이터 제공자들은 local iteration을 수행하고 각 레이어의 partial gradient를 계산함
- 이 gradient는 모든 파티에게 aggregated 됨
- 한 party는 average gradient를 이용하여 모델을 update함 

# Implementation

**Lattigo, lattice-based library**를 이용하여 MHE operation 을 구현함

**Onet**을 이용하여 secure channel을 가진 TCP 상에서 party들이 communicate하는 decentralized system을 구현하였음 

**Mininet**를 가상 네트워크 구현을 위해 사용하였음


# Conclusion

MHE를 이용하여 데이터를 보지 않고 계산하는 것이 가능하며 decentralized trust에 의존하며 데이터를 전송할 필요가 없음

또한 모델은 항상 encrypted 되어있고 partial gradient에 추가적인 노이즈를 줄 필요가 없음

실험 결과 정확도가 non-secure distributed solution과 유사하였으며 scalability 분석에서 컴퓨팅/커뮤니케이팅 오버헤드를 평가하였음

평가 결과 party수에 따라 linear하게 증가하였으며 각 레이어에서 neuron의 수나 feature의 수에 따라 logarithmically 증가하는 것을 확인 함

# 참고자료

[Youtube](https://www.youtube.com/watch?v=kX6-PMzxZ3c)
