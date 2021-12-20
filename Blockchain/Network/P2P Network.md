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

풀 노드가 새로운 트랜잭션을 검증하기 위해서는 기존에 mined 된 모든 블록에 대한 정보를 받아야 함<br/>
이 과정을 Initial Block Download (IBD) 또는 Inital sync라고 함<br/>
비트코인의 경우 최신 블록보다 144 블록(24시간 정도) 이상 뒤쳐져 있거나 하면 IBD가 실행 됨<br/>

## Block-First

비트코인에서 IBD는 best block chain에서 블록을 다운로드하는 것이 목표이며, Block-First라고도 불림

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-blocks-first-flowchart.svg">
</p>

1. **GetBlocks Message** : IBD -> Sync, 하나 이상의 블록 헤더 정보 전달
    - Sync Node는 IBD 노드가 연결한 Remote node

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-getblocks.svg">
</p>

2. **Inv Message** : Sync -> IBD, 최대 500개의 block inventory (블록 정보)를 보내줌
    - Inventory : 네트워크에서 정보에 대한 unique identifier

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-getblocks.svg">
</p>

3. **GetData Message** : IBD -> Sync, 하나 이상의 블록 inventory 
    - IBD 노드는 블록의 부모 블록을 받기 전까지 검증할 수 가 없음
    - 부모 블록이 없어서 검증 받지 못하는 블록을 orphan(고아) 블록이라고 함

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-getdata.svg">
</p>

4. **Block** : Sync -> IBD, 하나의 serialized 된 블록
    - 각 블록 요청에 대한 블록 정보를 전달 함

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-block.svg">
</p>

5. **Second GetBlock Message**
    - IBD 노드는 각 블록을 다운로드하고 유효성을 검사한 다음 다운로드할 최대 128개 블록을 큐에 유지하면서 다음 블록 요청
    - 블록을 요청하면 Sync 노드에 추가로 GetBlock 메세지를 보냄
    - 일치하는 해시를 찾아 해당 지점의 다음 블록부터 시작하여 500개의 블록 인벤토리로 응답함
    - 만약 일치하는 해시를 못찾은 경우 두 노드가 공통으로 갖는 유일한 노드를 0으로 가정하고 블록 1부터 재 전송함
    - 이런 반복 검색을 통해 IBD 노드의 로컬 블록체인이 Sync 노드의 로컬 블록체인에서 분기되더라도 Sync 노드는 더 가능성 높은 블록 정보를 보낼 수 있음
    - 이 포크 감지는 IBD 노드가 블록 체인의 끝에 가까워질수록 점점 더 유용해집니다. 

### Block-First IBD pros & cons

Pros
- Simplicity

Cons
- Speed Limit : IBD가 단일 Sync node에 의존하면 대역폭의 제한으로 다운로드 낮아짐
- Download Restart : IBD 노드는 다운로드가 완료되기 전까지 longest chain인지 알 수가 없음
- Disk Fill Attack : longest chain이 아닌 무의미한 정보로 disk를 채우는 공격을 할 수가 있음
- High memory Use : Sync 노드는 블록 순서에 상관없는 블록을 보낼 수 있기 때문에 Orphan 블록으로 메모리 리소스 낭비 가능

Bitcoin core는 Header-First IBD를 통해 이런 단점들을 일부 또는 전체 해결하고 있음


## Header-First

Bitcoin core 0.10.0은 IBD를 위해 header-first 방식을 채택함
header-first는 블록의 일부분만 검증하여 best header chain을 다운로드 하는 것이며, 병렬적으로 해당 헤더에 매칭되는 블록을 다운 받는 것임

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-headers-first-flowchart.svg">
</p>

1. **GetHeaders Message**: IBD -> Sync, 하나 이상의 헤더 해시 요청

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-getheaders.svg">
</p>

2. **Headers Message**: Sync -> IBD, 최대 2000개 블록 헤더

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-ibd-headers.svg">
</p>

3. 블록 헤더를 검증한 후
    - IBD 노드는 블록 검증 후 다음 두 가지를 병렬적으로 수행함
    - Download More Headers: sync 노드에게 다음 2000개 헤더를 요청함
    - Download Blocks: IBD 노드가 헤더를 다운받은 후 각 블록에 대한 정보를 요청하고 다운로드 함

<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-headers-first-moving-window.svg">
</p>

## Block Broadcasting

Miner가 새로운 블록을 생성하면 그 블록을 다음 중 하나의 방법으로 피어들에게 전달함

- Unsolicited Block Push
    - "Block" message를 풀노드 피어들에게 전달 함
- Standard Block Relay
    - Miner가 standard relay node 역할을 하며 "inv" message를 새로운 블록에 대한 inventory와 함께 피어인 풀노드와 SPV 모두에게 보냄
    - 이에 대한 response는 다음과 같음
    - **block-first(BF)** 피어는 full block을 요구하는 "getdata" message를 보냄
    - **header-first(HF)** 피어는 highest-height header의 해시를 포함한 "getheaders" message의 응답을 요청함. 이후 full block 정보를 요청함. header를 먼저 요청함으로써 header-first 피어는 ophan block을 거절하는 것이 가능함
    - **Simplified Payment Verification(SPV)** 클라이언트는 merkle block을 요청하는 "getdata" message의 응답을 요구함

|Message|From->To|Payload|
|:---|:---:|---|
|inv|Relay->Any|The inventory of the new block|
|getdata|BF->Relay|The inventory of the new block|
|getheaders|HF->Relay|One or more header hashes on the HF node’s best header chain (BHC)|
|headers|Relay→HF|Up to 2,000 headers connecting HF node’s BHC to relay node’s BHC|
|block|Relay→BF/HF|The new block in serialized format|
|merkleblock|Relay→SPV|The new block filtered into a merkle block|
|tx|Relay→SPV|Serialized transactions from the new block that match the bloom filter|

## Orphan Blocks

Orphan Block이란 특정 노드에서 이전 블록의 헤더 해시 값이 본적이 없는 블록을 지칭함<br/>
이는 부모노드가 best block chain의 일부가 아닌 stale block과 다름<br/>


<p align="center">
  <img src="https://developer.bitcoin.org/_images/en-orphan-stale-definition.svg">
</p>

## Transaction BroadCasting

트랜잭션을 피어에게 전달하기 위해서는 inv message가 전달됨<br/>
getdata message의 응답을 받으면 트랜잭션은 tx message를 통해 트랜잭션이 보내짐<br/>
해당 트랜잭션을 받은 피어는 트랜잭션이 valid하다고 가정하고 동일한 방법으로 트랜잭션을 포워딩함<br/>

## Memory Pool

Full peer는 다음 블록에 포함될 수 있는 unconfirmed 트랜잭션을 추적함<br/>
unconfirmed 트랜잭션은 Bitcoin Core에서 non-persistent memory에 저장이되며 이것이 Memory pool(mempool)임<br/>
피어가 shut down하면 wallet에 저장된 트랜잭션을 제외한 메모리 풀에 있는 트랜잭션은 비트코인 네트워크에서 사라지게 됨<br/>
늦게 채굴되어 stale block이 된 트랜잭션은 mempool로 다시 돌아갈 수가 있다<br/>
이렇게 다시 추가된 트랜잭션은 블록이 해당 트랜잭션을 포함하게 되면 거의 즉시 pool에서 제거되게 된다<br/>
이는 bitcoin core가 stale block을 하나씩 제거하는 것임<br/>
SPV 클라이언트는 트랜잭션을 relay하지 않기 때문에 memory pool을 갖고 있지 않음<br/>
SPV는 트랜잭션을 독립적으로 검증하는 것이 불가능하여 블록을 생성하는 것이 불가능하고, 오직 UTXO를 소비하는 것만 가능함<br/>


# 참고자료

[BitcoinDeveloper : P2P Network](https://developer.bitcoin.org/devguide/p2p_network.html)
