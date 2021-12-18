# Motivation

Interactive proof system : prover 와 verifier 상호 간 메세지를 교환하는 컴퓨테이션을 모델링한 abstract machine을 뜻함 <br/>
기존 Interactive proof system에서는 다음과 같이 가정하였음<br/>
Prover : 무한정의 계산 자원을 가졌지만 **신뢰할 수 없는 존재**<br/>
Verifier : 한정된 계산 자원을 가졌지만 **신뢰할 수 있는 존재**<br/>
이런 전제하에서는 공격 시나리오에서 prover가 악역이었으며, 이들이 verifier를 공격하는 상황을 가정하였음<br/>
하지만 **verifier가 악의적일 수 있는 시나리오**에 대해 가정할 수가 있음<br/>
이를 통해 다음과 같은 두 가지 질문에 대한 대답을 하고자 함<br/>

1. 누구나 verifier가 knowledge를 누설하지 않았다는 것을 확인할 수 있는가<br/>
2. verifier가 검증 과정 동안 알고 있어야 하는 knowledge의 비중은 어느 정도인가<br/>

이 의문점들을 해결하기 위해서 prover가 제공한 proof를 통해 악의적인 verifier가 검증을 수행할 수는 있지만 prover의 knowledge 자체에 대해서는 유추할 수 없는 시스템이 요구됨<br/>
이것이 바로 Zero Knowledge proof 

# Zero Knowledge proof (ZKP)

ZKP는 다음과 같은 조건이 만족되어야 함

1. Completeness : 어떤 조건이 참이라면, honest verifier는 honest prover에 의해 이 사실을 납득할 수 있다. (모든 정답 사례를 찾아낼 수 있다.)
2. Soundness : 어떤 조건이 거짓이라면, dishonest prover는 거짓말을 통해 verifier에게 조건이 참임을 절대 납득시킬 수 없다. (어떠한 오답 사례도 정답 사례라고 잘못 판단하지 않는다.)
3. Zero-Knowledge : 어떤 조건이 참일 때, verifier는 이 조건이 참이라는 사실 이외에 정보를 알 수 없다.

ZKP 프로토콜을 사용하면 인코딩 된 정보인 proof를 생성해야함. 이 proof의 크기가 너무 크거나 검증자 연산에 추가적인 코스트가 발생하면 오버헤드가 더 커짐.<br/>

## Non-interactive : Schnorr Identification Protocol

Non-Interactive : prover와 verifier의 메시지 교환을 최소화 하는 것을 의미, prover가 증명에 필요한 메시지를 보내고 연결이 끊어지더라도 메세지는 verifying 되어야한다는 것<br/>
Schnorr Protocol : 암호학에서, prover가 자신의 Private key를 공개하지 않고 이를 가지고 있다는 것을 증명하는 방법. 키 교환과 관련된 프로토콜로, 블록체인에 적용될 수 있는 예제<br/>
자세한 방법은 [해당 링크 참조](https://medium.com/decipher-media/zero-knowledge-proof-chapter-1-introduction-to-zero-knowledge-proof-zk-snarks-6475f5e9b17b)

## Structure of ZK Proof

**Structure** : 영지식 증명은 주어진 함수에 해당하는 회로, 주어진 회로에 대해서 입출력을 증명하고자 하는 증명자, 이를 검증하는 검증자<br/>
보통 검증자와 증명자는 서로 공유하는 키를 가짐. 이 키를 CRS (Common Reference String)이라 부르고 이는 RRS, SRS로 나뉨.<br/>
**Interactive Proof** : 증명을 위해 증명자와 검증자가 상호간의 통신하는 것. 검증자가 랜덤한 질의 값을 보내고, 해당 질의에 대해 알맞은 답을 증명자가 보내면 확실히 답을 알 것이라고 검증자가 믿게 됨<br/>
하지만 블록체인과 같은 경우에는 Interactive Proof를 하기 어렵기 때문에 랜덤 질의를 하는 것이 아니라 해시함수를 사용함. <br/>
증명자의 입장에서는 해시의 출력값을 원하는 값으로 통제할 수 없기 때문에 해시의 출력값이 마치 자신에게 랜덤값과 같이 보이게 됨. 이런 방법을 피앗-샤미르(FS) 휴리스틱이라 부름. 비상호적인 증명 방식임<br/>
영지식에서 임의의 코드(f)에 대해서 주어진 입력(x)을 넣으면 해당 출력(x)이 나오는 것이 보장됨.<br/>
입출력이 f에 맞는 경우 x는 언어 L(f)에 속한다라고 이야기함<br/>
f를 수행할 때 비밀 입력(w)이 필요할 수 있는데, 영지식에서는 이를 Witness라고 부름.<br/>
(x;w)가 L(f)에 속한다는 것을 w를 보여주지 않고 증명하는 것이 영지식 증명이다.<br/>
영지식 증명은 크게 두가지로 나뉨<br/>

- **프론트엔드** : 산술 회로식을 만드는 부분
- **백엔드** : 산술 회로식에 대해서 증명을 생성하는 부분. Circuit Specific (주어진 회로에 맞는 SRS 키를 만드는 것) 과 Universal (회로에 상관 없이 SRS나 RRS를 Polynomial Commitment 기법을 통해 만드는 것) 방식 두가지로 나뉨

여기서 산술식이란 덧셈과 곱셈으로 식을 변환하는 것

## Circuit Specific ZK Proof

ZKP 변환 과정 : Computation -> Arthimetic Circuit -> R1CS -> QAP<br/>

- **Computation** : ZKP는 임의의 연산(Computation)을 Proof로 바꾸는 과정. 우선 연산을 Circuit으로 바꿔야 함.
- **Arithmetic Circuit** : Validity function의 계산과정을 연산 회로(AND/OR 등의 논리게이트)로 표현한 것
- **R1CS** : 사칙연산 게이트 단위로 표현된 연산회로, 이 형태에서는 각 게이트에 주어진 입출력 값이 유효한지 확인할 수 있음. 그렇지만 전체 수식에 대한 유효성을 검증하기 위해서는 각 게이트별 유효성을 일일이 검사해야하여 검증자 입장에서 많은 검증횟수가 요구됨
- **QAP** (Quadratic Arithmetic Program) : R1CS에서의 단점을 극복하기 위해 등장한 회로 표현 방식. 각 게이트별 제약사항을 임의의 게이트 변수를 통해 하나의 다항식으로 표현하는 방법. 이하 QAP의 예시
  - Pinocchio : n개의 곱셈 게이트를 가지는 QAP 형태로 주어진 회로에 대해서 증명자가 n에 비례하는 시간에 증명 생성 및 회로 크기와 상관없이 상수시간 검증
  - Groth16 : Pinocchio를 더 개선한 것으로 작은 크기의 증명을 생성하는 영지식 증명법
  - KLO19 : Groth16과 동일한 증명 크기로 시뮬레이션 추출이 가능한 기법이 개발

## Universal ZK Proof

Circuit Specific ZK Proof의 경우 회로에 대해서 각각 다른 SRS (Structured Reference String)를 생성해야하고 생성과정에서 비밀 정보를 사용하는데 이비밀 정보가 유출되면 증명이 조작하는 것이 가능하기 때문에 SRS 생성과정을 신뢰할 수 있어야만 한다는 단점이 있음. Universal ZK Proof는 회로에 상관없는 CRS (Common Reference String)을 만들어 두고 회로가 주어진 경우, 이에 대한 증명을 다항식 commitment에 의해서 증명하는 방식

여기서 신뢰 주체가 필요한 SRS 기반 기법과 필요 없는 RRS 기반 기법으로 나뉘어짐.

다음과 같은 것들이 이에 포함 됨
- Sonic
- Plonk : 가장 작은 다항식을 필요로 하기 때문에 가장 증명 크기가 작은 기법
- DARK : RRS
- Bulletproofs : 대수 기반 기법으로 벡터 내적연산 지원, 블록체인 회사에서 많이 채택함. RRS 기반. 하지만 검증 시간이 원래 회로 계산보다 오래 걸려 Plonk로 전환 중
- Stark : 양자 저항성을 가진 기법으로 FRI (Fast Reed-Solomon Interactive Oracle Proofs)에 기반.

## Why Trusted Setup?

모든 ZKP 시스템은 prover가 치팅을하거나 fake proof를 생성하는 것을 막기 위해 verifier가 반드시 무엇이 proven되는 지를 알고 있어야함.<br/>
이는 ZKP property 중 soundness와 직접적으로 연관된 성질이며 일부 예시에서는 verifier가 full representation of statement를 가지는 것을 의미하기도함.<br/>
하지만 이는 증명해야할 statement가 커서 verification 과정이 느려지고, 어플리케이션에 low latency(e.g transaction propagation)이나 high bandwidth로 인해 bottleneck 현상이 발생할 수 있음.<br/>
이는 prover와 verifier 모두에게 이용가능한 CRS(SRS)의 관계를 pre-processing 단계에서 생성하는 방식으로 해결 가능한데, 이 과정에서 trusted setup 과정이 필요로함.<br/>
verifier가 proven하도록 보장하는 현존하는 (21'09) 세가지 방법은 다음과 같음<br/>

- **Verifier gets the full statement** : verifier가 명시적인 표현 관계(represtation of relation)를 사용. Bulletproof가 해당 케이스에 사용 됨. CRS의 일종인 URS(Unifom Reference String) 사용. prover와 verifier가 randomness와 public parameter에 동의함 
- **Verifier gets a succint representation of the statement** : 여러번 반복 계산되는 basic representation을 가진다는 것을 의미함. 예를들어 100번의 pedersen commitment를 반복하여 증명할경 우 하나의 pedersen commitment만을 relation으로 요구함. random oracle의 무작위성과 그것에 대한 강한 assumption에 의존하지만, SHA-3 해시함수로 대체되어 heuristically 생성될 수 있음(Fiat-Shamir heuristic이라 불림)
- **Pre-processing** : SNARK는 어떤 relation이든지 succintness를 보장함. 이를 위해, verifier는 relation의 summary에 의존하며, 이는 pre-processing stage에서 short string of bit를 모두 digest함을 의미함. PGHR, BTCV14, Groth16과 같은 QAP-based pre-processing SNARK의 경우가 그 예시임. 이 경우 pre-processing에서 생성된 SRS가 있음. 특히 prover의 SRS는 linear in relation size인 반면 verifier의 SRS는 Shrot함. 전처리 단계 없이는 이런 증명시스템을 구축할 수 없음

prover의 privacy와 verifier에게 치팅하지 않는 것 tradeoff 관계임. 일반적으로 ZKP 시스템은 randomness를 요구함. <br/>
non-interactive한 시스템의 경우 이 무작위성이 사전에 설정되어야하고 proof는 공개적으로 검증 가능해야함(URS). <br/>
URS와 달리 SRS는 setup이 비공개 무작위성에 의존함. 고로 fake proof를 생성할 백도어의 가능성이 존재함 (toxic waste).<br/>
그렇기에 엔터티들을 신뢰할 수 있도록 키를 생성하는 trusted setup이 필요함.<br/>
물론 하나의 entity가 키를 생성하는 것은 모든 사람이 verifer이자 prover인 ZKP시스템의 사용 목적을 무산시킬 수 있음.<br/>
이에 대한 해결 책으로 MPC를 적용하여 신뢰 가정을 줄이는 방법이 존재함. 이상적으로는 모든 당사자가 악의적이거나 compromised하지 않으면 보안은 유지가 됨.<br/>
일반적으로 succint ZKP는 trusted setup이나 multiparty ceremony 형태의 setup 단계를 필요로함. <br/>
예외적인 예시로는 statement가 충분히 작아서 succintness가 중요한 issue가 아닌경우나 compactly하게 작성 가능할 때(예를들어 매우 반복적으로 작성하거나)는 setup을 필요로하지 않음.


# 대표적인 ZKP 프로토콜

## ZK-SNARK

간결한 지식 프로토콜인 SNARK(Succint Non-interactive adaptive ARgument of Knowledge). Zero-knowlege Arguement란 증명이 오직 계산적이라는 의미를 내포함

- Zero-knowlege Proof : 확률적인 Soundness 제공
- Zero-knowlege Arguement : 연산적인 Soundness 제공

ZK-SNARK 특징

- Non-interactive
- 증명의 크기가 유의미하게 작음
- CRS가 필요하기 때문에 Trusted Setup 과정이 필요함
- 연산 -> 회로 -> R1CS -> QAP -> ZK-SNARK

Schwartz-zippel lemma에 따르면 서로 다른 다항식은 대부분의 점에서 서로 다른 값을 가짐.<br/>
임의의 점에 대해 다항식(연산)들이 같은 값을 가지는 것을 보이면 높은 확률로 다항식(연산)이 같음을 보일 수 있음.<br/>
여기서 임의의 점(평가에 사용할 QAP 다항식에서의 점)이라는 것이 Trusted setup 단계에서의 공개 매개 변수(CRS)로 부터 생성이 됨.<br/>
만약 정직하게 CRS가 생성이 되었다면 누구도 점에 대해서 알 수 없으며 부정한 다항식이나 증명을 생성할 수 가 없음<br/>



# 관련 프로젝트

[SnarkJS](https://github.com/iden3/snarkjs) : javascript 기반, iden3+circom circuit 활용, Groth16/Plonk
[BulletProof-dalek](https://github.com/dalek-cryptography/bulletproofs) : Bullet-proof 관련 논문이나 실험에서 많이 사용됨
[libsnark](https://github.com/scipr-lab/libsnark) : C++ 기반, 대중적으로 많이 쓰임
[BulletProof-nodejs](https://github.com/santiq/bulletproof-nodejs) : node js 기반, 4.3k stars
[zkrp](https://github.com/ing-bank/zkrp) : Zero Knowledge Range Proof, Go 기반

# 참고자료

[zk-SNARK 변환 과정](https://medium.com/ai-networkkr/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8%EC%97%90%EC%84%9C%EC%9D%98-%EA%B0%9C%EC%9D%B8%EC%A0%95%EB%B3%B4%EB%B3%B4%ED%98%B8-%EA%B8%B0%EC%88%A0-zk-snark-1-de5804e9b50e)

[영지식 증명기술 동향(국내 자료)](https://webcache.googleusercontent.com/search?q=cache:tqAMdVbpblkJ:https://www.itfind.or.kr/publication/regular/weeklytrend/weekly/view.do%3FboardParam1%3D7961%26boardParam2%3D7961+&cd=2&hl=ko&ct=clnk&gl=kr)

[Diving into the zk-SNARKs Setup Phase(Trusted setup 이유)](https://medium.com/qed-it/diving-into-the-snarks-setup-phase-b7660242a0d7)

[Zk-SNARKs: Under the Hood(비탈릭부테린 포스팅)](https://medium.com/@VitalikButerin/zk-snarks-under-the-hood-b33151a013f6)
