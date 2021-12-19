# Introduction

중앙 서버 없이 각 단말이 서로 동등한 입장에서 통신을 하는 네트워크. 각 단말은 서버이기도 하고 동시에 클라이언트가 될 수 있음.<br/>
비트코인 네트워크는 전체 노드가 블록과 트랜잭션 교환을 위한 P2P 네트워크를 공동으로 관리할 수 있음.<br/>
합의 알고리즘은 네트워킹를 커버하지 않기 때문에 비트코인 프로그램은 채굴자나 별도의 네트워크 프로토콜을 사용 함.

# Bitcoin P2P Network

## P2P Discovery

비트코인 프로그램을 실행시키면 어떤 IP address가 활성화 된 노드인지 알수가 없음<br/>
그렇기 때문에 비트코인 코어 내에 하드코딩되어 있는 하나 이상의 DNS 네임(DNS Seeds)을 쿼리를 날림<br/>
새로운 incoming connection을 허용하는 풀 노드를 응답으로 받게 됨<br/>
DNS seeds는 비트코인 커뮤니티에 의해 유지 됨. 

- Dynamic DNS seeds
  - Active하다고 생각되는 노드를 찾기 위해 네트워크를 스캔하여 연결할 IP를 찾는 서버
  - 피어들이 네트워크를 떠나거나 IP 주소가 바뀌는 경우가 많기 때문에 사용
  - 딜레이를 줄이는 것과 불필요한 DNS seeds 연결이 많아지는 것은 Trade-off 관계임
- Static DNS seeds
  - Manually updated되고 inactive node들을 위해 IP 주소를 더 잘 제공할 것 같은 시드를 제공하는 서버

DNS seeds가 인증 받지 않았거나 악의적인 공격자 또는 Man-in-the-middle 공격자에 의해 제한된 IP 주소 결과만 리턴 받을 수가 있음<br/>
그렇기 때문에 비트코인 프로그램은 DNS seeds에 독점적으로 의존해서는 안 됨<br/>

## Connecting to Peers

- Version Message : 피어에 연결되면 version number, block, current time을 담은 메세지를 remote node에 보냄. remote node도 응답으로 자신의 것을 보냄
- Verack Message : 양 쪽 노드가 연결이 성공적으로 이루어졌다는 것을 의미하는 메세지

프로그램이 네트워크에 연결 되면 연결된 피어가 다른 피어들의 IP 주소와 Port 번호를 알려주는 메세지를 보냄 (fully decentralized peer discovery)<br/>
노드는 연결 되었다면 일정 시간(비트코인의 경우 30분)마다 해당 메세지를 보냄. 만약 90분 이상 메세지가 없으면 연결이 끊긴 것으로 생각함<br/>

## Initial Block Download




# 참고자료

[BitcoinDeveloper : P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html)
