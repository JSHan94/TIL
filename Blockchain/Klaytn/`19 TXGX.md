# TXGX

Tech Forum by Ground X, 2019년도 발표 요약. [영상링크](https://www.youtube.com/playlist?list=PLKqrwxupttYFng6AOQTXHp2DEHNIQMJSC)

# Klaytn World: From Inception to Completion

<p>
  기존 블록체인 프로젝트들은 처리량, 트랜잭션 소요시간이 너무 큼. 이를 해결하기 위해 클레이튼을 제안함. <br/>
  Finality를 위해 <b>PBFT 기반의 합의알고리즘을 선택하고 TX를 전파하는 채널을 다양하게 만들어</b> 처리량을 높히고자함.<br/>
  TX가 단일 채널에 몰리면 병목현상이 심하기 때문에 <b>멀티 채널을 통해 병렬화</b>하고자함.<br/>
  또한 블록의 정보(Block, Receipt, State 등)가 스토리지에 저장이 되어야하는데, 단일 스토리지에 저장하기에는 시간이 많이 걸림. -> <b>DB 파티션</b> 진행<br/>
  Only State trie cache 를 <b>State trie node cache</b>로 구현 함(?, 잘 이해가 안 됨)<br/>
  클레이튼은 기존의 더 나은 UX를 위해 어카운트 모델을 변경함.<br/>
  기존에는 개인키와 매칭되던 공개키에 대응하는 지갑 Address가 존재하였는데, 이는 개인키가 변경되면 지갑 주소도 변경되어야하는 불편함이 있음<br/>
  이를 개선하기 위해, 클레이튼은 <b>Address와 공개키의 관계를 과감하게 끊어내서 개인키가 바뀌더라도 백업키 등으로 지갑주소를 그대로 사용</b>할 수 있도록함.<br/>
  또한 단일 트랜잭션 포맷에 맞춰서 트랜잭션을 만드는 것은 불편하기 때문에 개발자를 위해 <b>native transaction type을 지원</b> 함.<br/>
  즉, 성능적 측면과 사용자적인 측면에서 개선하고자 노력 함.<br/>
  이외에도 SDK, Explorer 등 개발자들이 쉽게 클레이튼 네트워크에 참여할 수 있는 채널을 만들어 두었음.<br/>
</p>


# Klatyn's Network Architecture and Consensus

<p>
  기존 분산 네트워크의 낮은 처리량과 불확실한 지연 시간이 문제임.
  모든 노드가 동등하냐라는 질문을 하게되고 이를 통해 노드를 3가지 레이어로 나누게 됨
  Consensus Node(CN) : 블록 생성을 전담, 신뢰할 수 있는 엔터티(컨소시엄)들이 관리할 수 있도록 함 / 담합의 문제, 공격 대상이 한정되서 위험성 증가
  Proxy Node Network(PN) : 외부 EN으로부터 받은 트랜잭션을 CN 및 인근 PN에게 전달하고, CN에서 생성된 블록을 EN에 전파
  Endpoint Node Network(EN) : 서비스나 사용자의 트랜잭션을 PN에 보내는 역할을 함.
  블록 생성은 Permissioned하게 하고, 사용자들은 제한 없이 네트워크에 참여할 수 있도록 함. (분산 시스템의 한계인듯..)
  BFT : 즉각적인 Finality / 높은 트랜잭션 메세지 교환(n^2)
  Klaytn은 Committee 를 추가하여 한 블록을 검증하기 위해 랜덤하게 선택된 CN 노드를 통해 메세지 수를 줄임(이러면 BFT의 1/3 이하의 악의적 공격에 Tolerance하지 않을 것 같은데?)
  이를 방지하기 위해서 CN 노드들이 Klay를 예치하고 유지하게 해서 악의적 공격을 방지하도록 노력함.
  또한 Klaytn은 PoS의 블록생성의 불평등을 막기 위해 Gini 계수를 도입함. Staking된 값에 따라 Slot을 생성하여 랜덤하게 셔플하여 블록을 생성 함.
  
  
  
</p>
