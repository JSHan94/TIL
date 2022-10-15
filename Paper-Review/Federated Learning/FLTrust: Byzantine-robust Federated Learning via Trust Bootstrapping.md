# Motivation

기존에는 다양한 클라이언트들이 중앙 서버에서 처리하는 Centralized Learning이 대세임 

하지만 이와 같은 방식은 다음과 같은 문제가 있음

- Untrusted server (Data breaches, Insider threats)
- High communication cost (Resource-constrained device, IoT, Smart phone)

FL을 사용하자

- Data stay locally on clients
- Clients train model locally
- Clients send models or updates to server
- 실제 사용 사례 (구글 G-Keyboard, 애플 Siri)

# Poison Attack

FL은 Micious client가 거짓 데이터를 이용하여 모델을 공격하는 Poison Attack에 취약함

# Byzantine-robust Federated Learning as Defense

- Byzantine-robust aggregation rule (Krum, Trimmed mean, Median)
- Remove **outlier** local model updates
- Theoretical guarantee (Various assumptions, Bound change of global model parameters cause by malicious clients)

하지만 여전히 strong attack에 대해서는 취약함
- [Local model poisoning attacks](https://www.usenix.org/conference/usenixsecurity20/presentation/fang)
- [Backdoor attacks](http://proceedings.mlr.press/v108/bagdasaryan20a.html)
- No root of trust
- Every client could be malicious

# FLTurst : Bootstrapping Trust

- Server collects a small training dataset
- Server maintains a server model (Like how a client maintains a local model)
- User server model update to bootstrap trust (Assign trust scores for clients)

FLTrust는 FL에서 로컬 모델과 글로벌 모델을 업데이트하는 과정에 적용이 됨

## Aggregation Rule

Cosine Similarity를 이용하여 outlier를 탐지하고 이를 이용하여 Trust Score를 계산함

Local model update에서 Normalize를 함

## Theoretical Analysis

- Under some assumption on the learning problem
- For an arbitrary number of malicious clients
- The difference betwwen the learnt global model and the optimal model under no attack is bounded

# Conclusion

- Design a new Byzantine-robust FL method that is robust against poisoning attacks
- Server can enhance security of FL via collecting small training dataset to bootstrap trust

# 참고자료

[Youtube](https://www.youtube.com/watch?v=zhhdPgKPCN0)
[Bootstrapping](https://learningcarrot.wordpress.com/2015/11/12/%EB%B6%80%ED%8A%B8%EC%8A%A4%ED%8A%B8%EB%9E%A9%EC%97%90-%EB%8C%80%ED%95%98%EC%97%AC-bootstrapping/)
