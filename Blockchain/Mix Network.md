# Mix Network

Mix 네트워크는 라우팅 프로토콜로, mix라는 프록시 서버 체인을 이용하여 communication을 추적하기 어렵게 만든다.

이는 복수의 sender로부터 메세지를 받고, 이를 셔플하고 랜덤한 순서로 다음 목적지나, mix node로 전단하는 방식을 가진다.

이를 통해 end-to-end communication의 연관성을 알기 어렵고, 개별 mix 노드는 자신에게 들어오고 나가는 메세지들에 대해서만 알기 때문에 

악의적인 노드로 부터 network resistant를 가질 수 있게 된다.



# 참고 자료

https://en.wikipedia.org/wiki/Mix_network
