
# Node & Client

<p>
  A node refers to a <b>running piece of client software.</b><br/>
  A client is an <b>implementation of blockchain</b> that verifies all transactions in each block, keeping the network secure and the data accurate.
</p>

[이더리움 공식문서](https://ethereum.org/en/developers/docs/nodes-and-clients/)

# Cryptographic Hash
<p>
암호학적으로 collision을 찾기 힘든 해시 함수. SHA-256, keccak256 등
</p>

# Digital signature

<p>
  트랜잭션을 발생 시켰을 때 소유권을 증명하는 기법. ECDSA 타원곡선 암호화 등 <br/>
  개인키로 암호화 시켜서 공개키로 검증할 수 있게 함.
</p>

# SmartContract

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

# Nonce

<p>
  일반적으로는 PoW에서 연산 속도를 조절하기 위한 난이도를 결정하는 값임. <br/>
  그렇지만 이더리움과 같은 어카운트 기반의 블록체인에서 트랜잭션 nonce는 현재 트랜잭션이 몇번 수행되었는 지를 알려주는 값임 <br/>
  트랜잭션이 한 어카운트에서 여러번 실행되는 것을 막는 역할을 함. state가 네트워크 딜레이 등으로 동시에 처리될 수 없기 때문에 막음<br/>
  이 때문에 이더리움은 비트코인과 달리 병렬처리가 되지 않는 문제가 있음
</p>

# RLP Algorithm

<p>
  이더리움에서 데이터를 serialize하기 위한 인코딩 방식. 길이와 타입을 의미하는 prefix와 함께 데이터를 재귀적으로 표현함.<br/>
  단절된 오프라인 상황에서 개인키를 생성하고 트랜잭션을 바이너리 형태로 생성하는데 유용하기 때문에 사용됨.<br/>
</p>

# Verifiable Random Function (VRF)

<p>
  A public-key pseudorandom function that provides proofs that its outputs were calculated correctly <br/>
</p>

# Accumulator

<p>
  집합에서 어떤 항목이 있는지 없는지를 확인하는 기법. Blockchain에서는 Merkle Tree를 주로 사용함
</p>

# Key exchange

<p>
  P2P 통신 시 서로 임의로 만든 키를 교환하고, 암호화 된 상태에서 변조가 되지 않을 것이라 생각하고 데이터 교환함
</p>

# RPC (Remote Procedure call)

<p>
  RPC는 별도의 원격 제어를 위한 코딩 없이 다른 주소 공간에서 함수나 프로시저를 실행할 수 있게 하는 프로세스 간 통신 기술.<br/>
  RPC를 이용하면 프로그래머는 함수가 실행 프로그램에 로컬 위치이든 원격 위치이든 동일하게 코드 사용 가능 
</p>

[Wiki](https://ko.wikipedia.org/wiki/%EC%9B%90%EA%B2%A9_%ED%94%84%EB%A1%9C%EC%8B%9C%EC%A0%80_%ED%98%B8%EC%B6%9C)


# IPFS

<p>
IPFS(아이피에프에스)는 "InterPlanetary File System"의 약자로서, 분산형 파일 시스템에 데이터를 저장하고 인터넷으로 공유하기 위한 프로토콜이다. 냅스터, 토렌트(Torrent) 등 P2P 방식으로 대용량 파일과 데이터를 공유하기 위해 사용한다. <br/>
기존의 HTTP 방식은 데이터가 위치한 곳의 주소를 찾아가서 원하는 콘텐츠를 한꺼번에 가져오는 방식이었지만, IPFS는 데이터의 내용을 변환한 해시값을 이용하여 전 세계 여러 컴퓨터에 분산 저장되어 있는 콘텐츠를 찾아서 데이터를 조각조각으로 잘게 나눠서 빠른 속도로 가져온 후 하나로 합쳐서 보여주는 방식으로 작동한다. <br/>
해시 테이블은 정보를 키와 값의 쌍(key/value pairs)으로 저장하는데, 전 세계 수많은 분산화된 노드들이 해당 정보를 저장하기 때문에 사용자는 IPFS를 사용함으로써 기존 HTTP 방식에 비해 훨씬 빠른 속도로 데이터를 저장하고 가져올 수 있다.
</p>

[Wiki](http://wiki.hash.kr/index.php/IPFS)
[Medium 아티클](https://medium.com/@kblockresearch/8-ipfs-interplanetary-file-system-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-1%EB%B6%80-http-web%EC%9D%84-%EB%84%98%EC%96%B4%EC%84%9C-ipfs-web%EC%9C%BC%EB%A1%9C-46382a2a6539)

# Web3

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
