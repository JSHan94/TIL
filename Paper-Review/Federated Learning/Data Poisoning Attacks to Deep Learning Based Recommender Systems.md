# Motivation

Deep Learning 기반의 추천 시스템들이 급격하게 성장하였음 (Recommender System, RS + Deep Learning Techniques, DL)

그런데 여기서 Data poisoning attack이 문제가 되고 이런 시스템을 디자인해보겠음

# DL based RS

user-item 관계를 모델링하기 위해 DL를 사용함

Reduce the loss between the predicted rating and real rating during training time

## Profile pollution attack 

- Testing time에서 일어남
- 일반 유저의 과거 행동을 오염시킴
- Relies on cross-site request forgery(CSRF)
- item-to-item recommender system에서만 적용 가능

## Data poisoning attack

- Training time에서 일어남
- 가짜 유저를 추천 시스템에 추가함

Algorithm-agnostic (random attack etc), **Algorithm-specific** (Graph-based etc) 존재


# Threat Model

## Attacker's Goal

공격자는 타겟 아이템을 promote하는 것을 목적으로 함

## Attacker's Backgroung Knowledge

공격자가 user-item interaction matrix에 접근 가능하다고 가정

공격자는 타겟 추천 시스템의 internal neural network architecture 접근 권한을 가질 수도 있음

## Attacker's Capabilities

공격자가 m 가짜 유저를 n filler item을 추천 시스템에 삽입하는 것을 가능함

# Problem Formulation

타겟 아이템 t의 Hit Ratio (HR)을 최대화

## Challenge

가짜 유저 v에 대해서

- 스코어를 측정하는 것이 discrete함 
> Relaxing rating scores to continuous variable
- HR은 가짜유저 v의 스코어 백터와 직접적으로 연관되어 있지 않음
> Converting the optimization problem into a tractable one

DL based RS에 대해서

- It is not practical to adopt any attack method that requires high computation overhead for a single fake user
- Sparse datasets usually lead to a high interference to the perdicted ratings of specific users
> RS tries to reduce the loss between the real and predicted ratings in the training process

## Solution

- Proposing the poison model to simulate the final state of the target RS that has been successfully compromised (Predicted ratings -> Real ratings)
- Proposing the selection probability of items to increase the diversity of filler items (Roboustness)

# Overview of Attack

- Approximating HR
- Constructing Poison Model
- Selecting Filler Items

# Conclusion

- DL based RS에 대한 Data poison attack 최초의 시스템 연구
- Optimization problem로써 attack을 정의하였고 그것을 해결하기 위해 다수의 테크닉 개발
- 실제 3개의 데이터 셋을 통해 공격 모델 평가
- Data poisoning attack의 효용성에 미치는 영향과 통계적 분석을 통해 가짜 사용자를 탐지하는 것에 대해 연구함

# 참고자료

[Youtube](https://www.youtube.com/watch?v=PS6IlsiIv4Y)
