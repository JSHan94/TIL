# 블록체인 최신 기술 동향

- 1세대(BTC) : 서로 신뢰할 수 없는 사람들 간의 온라인 상에서 P2P로 가치를 전달할 수 있는 디지털 화폐
- 2세대(ETH) : 전 세계에 분포된 컴퓨터가 인간의 운영 없이 스스로 구동할 수 있는 어플리케이션 플랫폼
- 3세대(?) : 기존 세대보다 더 빠르고, 탈중화된 플랫폼이라 정의하지만 아직 명확하게 지칭되는 Player는 

**블록체인 연구 동향**

- SmartContract : 스마트 계약의 보안적 문제에 대한 연구
- 중앙 집중화 문제 : 마이닝 풀이 특정 국가나 기관에 집중되는 현상을 막는 방법에 대한 연구
- 암호화 함수의 한계 : Post-Quantum Cryptography (양자 후 암호) 기술에 대한 연구
- 합의 알고리즘 : 에너지 효율적인 알고리즘, 보안성이나 성능적인 측면에서의 연구
- 확장성 : Layer2, Off-chain 등 처리 속도나 다른 블록체인과연 상호운용성과 같은 확장성에 대한 연구
- 프라이버시 : 코드 난독화 등을 통해 Public Blockchain에서도 프라이버시와 기밀성을 제공하는 연구

# 기초 개념

## Public vs Private Blockchain

- Public Blockchain : 누구든(해커나 악의적인 공격자 포함) 블록체인 네트워크 참여하여 블록체인의 엔터티로 역할을 할 수 있는 플랫폼
- Private Blockchain : 참여자가 특정한 프로세스를 거쳐서(신원 인증 등) 블록체인 엔터티로 참여할지 말지를 결정하는 플랫폼 

컨소시움, 하이브리드 블록체인이 있기는 하지만 결국 Private에 속한다고 생각 함


## Why Blockchain is Disruptive Tech?

블록체인에 사용되는 기술들은 사실 새로운 것이 없음(PKI, Merkle tree, SHA, PoW, ECC). 하지만 비트코인이란 프로젝트를 시작으로 새로운 개념이 만들어짐. 기존에는 데이터 컨트롤을 관리자가 전담하였지만 블록체인 기술을 통해 규칙을 기반으로 여러 엔터티가 공동의 합의를 통해 결정하는 것이 가능해짐. 즉, 법칙 기반의 단일 데이터에 대한 공동 관리가 가능해짐

[참고 아티클](https://brunch.co.kr/@mobiinside/935)


## Token Economy & Governance

- Token Economy : 코인과 토큰을 서비스에 제공하여 참여자들이 특정 행위에 대해 보상을 받게하여 시스템을 활성화 시키고자하는 경제 생태계. 
- Governance : 블록체인에서 의사결정이 이루어지는 과정 (the process by which decision are made).


## IPO/ICO/IEO/STO

- IPO : Initial Public Offering. 기업공개, 주식에서의 상장
- ICO : Initial Coin Offering. 암호화폐 공개
- IEO : Initial Exchange Offering. 거래소를 통해 자금유치를 대행하는 개념
- IBO : Initial Bounty Offering. 암호화폐 대가 공개. 백서 번역, SNS 활동, 사용자 등록과 검증 등 블록체인 생태계 형성 기여에 대한 보상
- STO : Security Token Offering. 실물자산을 근거로 이윤의 일부를 배당으로 받거나 소유권 주장 가능하게하는 토큰. IPO에 비해 저렴


## UTXO와 Account 모델

<img src="https://mblogthumb-phinf.pstatic.net/MjAyMDA5MTJfMTI5/MDAxNTk5ODkwMzM3MDI1.wffCdDVRXlVU6y1G2gKS2PzlHptvHKXUdbvOUuptQMcg.kB3txHZ9w6JFIZ5qLD6MYPww1Rrl1-KoJuqztj4aZMwg.PNG.pcmola/1_eAKr5SIZfWXwC9dFBOmS3Q.png?type=w800"/>
- UTXO : UTXO의 트랜잭션은 입력으로는 사용되지 않은 지출 목록(UTXO)를 받고, 출력으로는 새로운 UTXO를 만들어냄. 한 번 사용된 UTXO는 목록에서 제거 됨.
    - 동시에 여러 트랜잭션을 처리할 수 있는 **확장성**
    - 매 거래마다 새로운 주소를 활용하여 **(pseudo) 익명성**
    - UTXO는 한번 사용된 후 사라지기 때문에 이중 지불을 방지할 수 있음
    - UTXO가 과도하게 생성될 경우 흩어진 코인을 모두 모아야하는 번거로움과 불필요한 수수료를 내야할 문제가 생길 수 있음
- Account : Global State가 각 계정의 Balance를 추적 함. 
    - 직관적이고 상태 추적이 가능한 **단순성** 
    - 거래 검증 시 충분한 잔액을 가지고 있는 지만 확인하면 되는 **효율성**
    - 하지만 이는 Double Spending의 가능성이 있어, 이더리움은 모든 계정이 공개적으로 볼 수 있는 nonce를 이용하여 두번 이상 제출 되는 것을 막음


## Node & Client

<p>
  A node refers to a <b>running piece of client software.</b><br/>
  A client is an <b>implementation of blockchain</b> that verifies all transactions in each block, keeping the network secure and the data accurate.
</p>

[이더리움 공식문서](https://ethereum.org/en/developers/docs/nodes-and-clients/)

## 블록의 일반적 구조

<p>
    <img src="https://steemitimages.com/p/2FFvzA2zeqoVZ5NRzV2o8MyJEzowAL6rjbt8w3dTGpUdKftDHiMJKETpjxquKcdhhAZYWXERxofcjZ6V2AQugwz8ke3UAceG7GNj1ZKhogzK3ngrA9QMPspiszQyL?format=match&mode=fit&width=640">
</p>

## Turing Complete

<p>
    Turing Complete는 어떤 복잡한 알고리즘이든 수행할 수 있는 Turing Machine을 의미 함<br/>
    Turing Complete가 되기 위해서는 루프와 분기 기능이 필요함<br/>
    비트코인의 스크립트 언어는 표준 산술 연산만 지원하기 때문에 Turing incomplete하고 이더리움의 Solidity는 Turing Complete 함<br/>
    Turing Complete한 코드를 블록체인 상에서 사용하려면 Virtual Machine을 사용해야 함<br/>
    
</p>

## Cryptographic Hash
<p>
암호학적으로 collision을 찾기 힘든 해시 함수. SHA-256, keccak256 등
</p>

## Digital signature

<p>
  트랜잭션을 발생 시켰을 때 소유권을 증명하는 기법. ECDSA 타원곡선 암호화 등 <br/>
  개인키로 암호화 시켜서 공개키로 검증할 수 있게 함.
</p>


## SmartContract

<p>
  특정 주소에 배포되어 있는 TX로 실행가능한 코드
  <ul>
    <li>스마트 컨트랙트 소스코드는 함수와 상태를 표현; 컨트랙트 소스코드는 블록체인에 저장 됨</li>
    <li>함수는 상태를 변경하는 함수, 상태를 변경하지 않는 함수로 나뉨</li>
    <li>사용자,EOA owner (<-> Contract Account, CA)가 스마트 컨트랙트 함수를 실행하거나 상태를 읽을 때 주소가 필요함</li>
  </ul>
  스마트 컨트랙트는 사용자가 실행함
  <ul>
    <li>상태를 변경하는 함수를 실행하려면 그에 맞는 TX를 생성하여 블록에 추가 함 (TX체결 = 함수의 실행)</li>
    <li>상태를 변경하지 않는 함수, 상태를 읽는 행위는 TX가 필요없음 (노드에서 실행). 주로 데이터를 읽는 함수</li>
  </ul>
  <b>Contract = Code(함수) + Data(상태)</b><br/>
</p>

## Nonce

<p>
  일반적으로는 PoW에서 연산 속도를 조절하기 위한 난이도를 결정하는 값임. <br/>
  그렇지만 이더리움과 같은 어카운트 기반의 블록체인에서 트랜잭션 nonce는 현재 트랜잭션이 몇번 수행되었는 지를 알려주는 값임 <br/>
  트랜잭션이 한 어카운트에서 여러번 실행되는 것을 막는 역할을 함. state가 네트워크 딜레이 등으로 동시에 처리될 수 없기 때문에 막음<br/>
  이 때문에 이더리움은 비트코인과 달리 병렬처리가 되지 않는 문제가 있음
</p>

## RLP Algorithm

<p>
  이더리움에서 데이터를 serialize하기 위한 인코딩 방식. 길이와 타입을 의미하는 prefix와 함께 데이터를 재귀적으로 표현함.<br/>
  단절된 오프라인 상황에서 개인키를 생성하고 트랜잭션을 바이너리 형태로 생성하는데 유용하기 때문에 사용됨.<br/>
</p>

## Verifiable Random Function (VRF)

<p>
  A public-key pseudorandom function that provides proofs that its outputs were calculated correctly <br/>
  컴퓨터과학에서 100% 랜덤한 값을 생성할 수 는 없고 항상 유사랜덤 값만 생성하는 것이 가능함 <br/>
  난수를 생성할 때, 여러 사용자가 보낸 값을 활용할 경우, 마지막 전송하는 사용자에 의해서 난수 결과값이 조작될 수 있는 문제가 있음.<br/>
  이에 대한 대안으로 블록체인에서 난수를 생성하는 방법은 Commit Reveal Scheme, BLS scheme 등이 있음. <br/>
  
  <ol>
    <li>Commit Reveal Scheme : 각 사용자가 난수 생성을 위한 값을 보낼 때 그 값을 암호화 시켜서 보내도록 함. </li>
    <li>BLS Scheme : 임계 값 서명 시스템 중 하나로, m of n이 서명할 경우 유효한 서명이 되게함. </li>
  </ol>
</p>

## Accumulator

<p>
  집합에서 어떤 항목이 있는지 없는지를 확인하는 기법. Blockchain에서는 Merkle Tree를 주로 사용함
</p>

## Key exchange

<p>
  P2P 통신 시 서로 임의로 만든 키를 교환하고, 암호화 된 상태에서 변조가 되지 않을 것이라 생각하고 데이터 교환함
</p>

## RPC (Remote Procedure call)

<p>
  RPC는 별도의 원격 제어를 위한 코딩 없이 다른 주소 공간에서 함수나 프로시저를 실행할 수 있게 하는 프로세스 간 통신 기술.<br/>
  RPC를 이용하면 프로그래머는 함수가 실행 프로그램에 로컬 위치이든 원격 위치이든 동일하게 코드 사용 가능 
</p>

[Wiki](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C)


## IPFS

<p>
IPFS(아이피에프에스)는 "InterPlanetary File System"의 약자로서, 분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜이다. 냅스터, 토렌트(Torrent) 등 P2P 방식으로 대용량 파일과 데이터를 공유하기 위해 사용한다. <br/>
기존의 HTTP 방식은 데이터가 위치한 곳의 주소를 찾아가서 원하는 콘텐츠를 한꺼번에 가져오는 방식이었지만, IPFS는 데이터의 내용을 변환한 해시값을 이용하여 전 세계 여러 컴퓨터에 분산 저장되어 있는 콘텐츠를 찾아서 데이터를 조각조각으로 잘게 나눠서 빠른 속도로 가져온 후 하나로 합쳐서 보여주는 방식으로 작동한다. <br/>
해시 테이블은 정보를 키와 값의 쌍(key/value pairs)으로 저장하는데, 전 세계 수많은 분산화된 노드들이 해당 정보를 저장하기 때문에 사용자는 IPFS를 사용함으로써 기존 HTTP 방식에 비해 훨씬 빠른 속도로 데이터를 저장하고 가져올 수 있다.
</p>

[Wiki](http://wiki.hash.kr/index.php/IPFS)
[Medium 아티클](https://medium.com/@kblockresearch/8-ipfs-interplanetary-file-system-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1%EB%B6%80-http-web%EC%9D%84-%EB%84%98%EC%96%B4%EC%84%9C-ipfs-web%EC%9C%BC%EB%A1%9C-46382a2a6539)

## Web3

<p>
  web3.js 와는 전혀 상관 없는 것으로<br/>
  웹3 재단에서는 웹3.0을 다음과 같은 3가지 특징을 가진 인터넷이라 정의함<br/>
  <ol>
    <li> 사용자의 데이터는 기업이 아닌 자신이 소유 </li>
    <li> 보안성을 가진 글로벌 디지털 거래 </li>
    <li> 탈중앙화된 정보와 가치의 온라인 거래소 </li>
  </ol>
  다시말해 웹3.0은 블록체인이 만들어지고 연결되어 가는 생태계를 의미함<br/>
</p>

## Merkle Tree vs Merkle Patricial Tree

### Merkle Tree
<p>
  머클 트리는 블록에 포함된 거래를 트리 형태로 요약한 것. 블록이 보유하고 있는 거래내역들의 해시 값을 가장 가까운 거래 내역끼리 쌍을 지어 해시화 하고, 쌍을 지을 수 없을 때까지 해당 과정을 반복하여 완성되는데, 이를 통해 다수의 데이터를 하나로 묶어 용량을 절약할 수 있음. <br/>
  머클 트리에서는 모든 거래내역들을 해시화한 머클 루트를 통해 트리 내에 거래 내역의 변동 여부를 쉽게 확인하고, 이 루트를 헤더에 담아 트랜잭션의 유효성을 보장함. <br/>
  블록체인의 성능 향상에 다음과 같은 방식으로 크게 기여함.<br/>
  가까운 노드 2개를 합쳐가면서 하나의 값만 남아있을 때까지 이 과정을 반복한다.<br/>
  <ol>
    <li> 특정 거래 내역을 증명하기 위해 모든 거래 내역을 검색할 필요 없음. 데이터 일부만을 처리해 보관하는 라이트 노드를 분리해 거래 속도를 높힐 수도 있음</li>
    <li> 모든 거래내역들이 합하여 해시화 된 것이 머클 루트이기 때문에, 특정 거래내역을 확인하기 위해 일일히 트랜잭션을 확인할 필요 없음</li>
  </ol>
</p>

### Merkle Patricia Tree

<p>
  이더리움에서 사용하는 방식. PATRICIA 는 Practical Algorithm To Retrieve Information Coded In Alphanumeric의 약자로 영숫자로 코딩된 정보를 검색하는 알고리즘을 뜻 함. <br/>
  트랜잭션 트리의 각 노드는 [key,value] 값을 갖고 있어서 정보를 더욱 효율적으로 탐색할 수 있음. <br/>
  <div><img src="https://asecuritysite.com/public/merkle04.png"/></div>
  종류로는 크게 State(상태 정보) Trie, Storage(계정 정보) Trie, Transactions(거래 정보) Trie, Receipts(가스사용량,로그 등 부가 정보) Trie
</p>
