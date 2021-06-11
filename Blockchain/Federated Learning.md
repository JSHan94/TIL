# Federated Learning

연합 학습으로 불리기도 하며 다수의 로컬 클라이언트가 하나의 중앙 서버와 협력하여 데이터가 탈중앙화된 상황에서 글로벌 모델을 학습하는 기술임

로컬 클라이언트로는 IoT, Mobile Device 등이 포함될 수 있음

https://ai.googleblog.com/2017/04/federated-learning-collaborative.html 구글 AI 블로그에 소개 되기도 하였으며 실제 G Keyboard에 적용되고 있음

연합 학습은 **데이터 프라이버시 향상**과 **커뮤니케이션 효율성** 두 가지 장점이 있음

로컬 클라이언트에서 민감 정보들을 수집할 경우 프라이버시를 보장할 수 있으며 

수 만개의 로컬 디바이스의 데이터를 모두 중앙 서버로 전송할 경우 네트워크 트래픽과 스토리지 비용이 증가하는 데 이 비용을 감소 시킬 수 있음



# 참고 자료

FL 논문 : [FL 소개 논문, 2015](https://arxiv.org/abs/1602.05629), [FL 이정표, 2019](https://arxiv.org/abs/1912.04977)

관련 코드 : [FL with Tensorflow](https://github.com/tensorflow/federated)

참고 사이트 : [CURG Medium](https://medium.com/curg/%EC%97%B0%ED%95%A9-%ED%95%99%EC%8A%B5-federated-learning-%EA%B7%B8%EB%A6%AC%EA%B3%A0-%EC%B1%8C%EB%A6%B0%EC%A7%80-b5c481bd94b7)
