# About Paper

Accepted in TPDS (Transactions on Parallel and Distributed Systems) 2020

[TPDS Popular Article 2위](https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=71)

# Motivation

FL에서 Global Model의 데이터셋이 Imbalance 하면 Model의 성능이 떨어지게 됨

그렇기 때문에 이를 Data Augment나 Downsample을 통해 rebalacing하고

FL server와 client 사이에 Mediator 두고 이를 통해 Training 과정을 rescheduling 함.

이런 전체적인 프레임워크를 **Astraea**라고 명함

# Astraea

## Z-score

Data augmentation과 downsampling에서 **rebalancing**을 위해 사용

## Kullback-Leibler divergence

Mediator가 Multi-client의 **rescheduling**을 위해 사용

# IMHO

FL의 목적이 Privacy-preserving인데 Mediator를 두면 결국 central server가 있는 것이 아닌지..?

그리고 Augment와 Downsample을 하려면 데이터의 distribution을 알아야하는데 그것이 이미 데이터를 보는게 되어

FL의 목적에 맞지 않는게 아닌가?

그래도 Github에 오픈소스로 전체 작업 코드가 있고  

다양한 실험을 통해 Astraea가 성능을 높힌다는 것은 보여줌.

Imbalance를 어떤 식으로 탐지하고 처리할지에 대한 논의가 필요할 것으로 생각 됨.

# 참고자료

[Source Code](https://github.com/mtang724/Self-Balancing-Federated-Learning)
