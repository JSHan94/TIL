# Transmission Types

<p align="center">
  <img src="https://github.com/JSHan94/TIL/blob/main/Blockchain/images/routing%20protocols.jpg"/>
</p>

## Unicast 

<ul>
  <li/> one-to-one transmission
  <li/> Transmission Control Protocol (TCP), User Datagram Protocol (UDP)가 해당 프로토콜에 포함 됨
</ul>

## Anycast

<ul>
  <li/> one-to-one-of-Many transmission
  <li/> 단일 송신자로부터 인터넷 상 트래픽인 datagram들을 topology 상의 잠재적인 수신자 그룹 중 가장 가까운 노드로 연결
  <li/> 여러 개의 노드들에 전송될 수 있고 해당 노드들 모두 동일한 목적 주소로 식별 됨
</ul>


## Broadcast

<ul>
  <li/> one-to-all transmission
  <li/> 송신 호스트가 전송한 데이터가 네트워크에 연결된 모든 호스트에 전송되는 방식을 의미
  <li/> 송신자가 보내는 single datagram은 모든 가능한 경로의 endpoint에 라우팅 됨
  <li/> 네트워크는 자동으로 datagram을 복제하여 네트워크의 모든 수신자에게 전송되도록 구현 함
</ul>

## Multicast

<ul>
  <li/> one-to-many-of-many transmission
  <li/> 한 번의 송신으로 메세지나 정보를 목표한 여러 컴퓨터에 동시에 전송하는 것
  <li/> 보통 IP multicast로 형태로 구현되어 스트리밍 서비스 등에 주로 사용됨
  <li/> 주로 IP 라우팅 단계에서 구현되며, 데이터그램을 목적 주소로 보내기 위한 최적의 전송 경로를 생성함
</ul>

<p>
  기존에는 특정 그룹에 메세지를 전달하기 위해서는 클라우드 컴퓨팅 환경에서 multicast 방식을 이용하였지만, 다음과 같은 이유로 어려움
  <ul>
    <li/> 일부 노드의 프로세스에 문제가 발생하여 노드가 crash 될 수 있음
    <li/> 네트워크 상의 문제로 패킷이 딜레이되거나 드랍될 수 있음
    <li/> 네트워크에 새로운 노드가 추가되고 제거되는 것이 빈번함
  </ul>
  즉, Multicast 방식은 fault-tolerance와 scalability 측면에서 부족한 부분이 다수 있음<br/>
  이를 해결하기 위해 Multicast는 다음과 같은 방법을 시도함
</p>


# Gassip Protocol


<p align="center">
  <img src="https://github.com/JSHan94/TIL/blob/main/Blockchain/images/gassip.png"/>
</p>

<p>
  
</p>
