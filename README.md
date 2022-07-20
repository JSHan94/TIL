# Today I Learned(TIL) Wiki

[![Since](https://img.shields.io/badge/since-2021.03.01-333333.svg?style=flat-square)](https://JSHan94.github.io)
[![author](https://img.shields.io/badge/author-JSHan94-0066FF.svg?style=flat-square)](https://JSHan94.github.io)


## Computer Science

<details>
  <summary>📌 Blockchain</summary>

 - ### Blockchain
    - [기술 동향 및 개념 이해](https://github.com/JSHan94/TIL/blob/main/Blockchain/Basic.md)
      - 블록체인의 최신 기술 동향
      - Public vs Private Blockchain
      - Why Blockchain is Disruptive?
      - Token Economy & Governance
      - IPO/ICO/IEO/STO
      - UTXO와 Account 모델
    - 합의 알고리즘
      - [합의가 이루어지는 과정]() <!--Safety, Liveness, Consensus가 이루어지는 방법, Finality-->
      - [Finality](https://github.com/JSHan94/TIL/blob/main/Blockchain/Consensus/Finality.md)
      - [PoW vs PoS vs DPoS]()
      - [BFT, PBFT]()
      - [Tendermint]()
      - [Raft]()
    - Network
      - [P2P Network](https://github.com/JSHan94/TIL/blob/main/Blockchain/Network/P2P%20Network.md)
      - [Inter-Blockchain Communication]()
      - [Routing Protocol](https://github.com/JSHan94/TIL/blob/main/Blockchain/Network/Routing%20Protocols.md)
      - Membership Protocol
      - Paxos
    - Storage
      - [Blockchain의 구조와 Ledger의 트리 구조]()
      - [블록체인의 구조]()  <!--블록헤더/바디, 머클트리/패트리시아트리-->
      - [Blockchain TX Flow]()
      - [Sharding]()
      - [IPFS](https://github.com/JSHan94/TIL/blob/main/Blockchain/Storage/IPFS.md)
      - [CAP 정리](https://github.com/JSHan94/TIL/blob/main/Blockchain/Storage/CAP%20%EC%A0%95%EB%A6%AC.md)

    - Cryptography & Security
      - [Hash 함수](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Hash%20Function.md) <!--SHA 256, Keecak-256-->
      - [CIA Triad](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/CIA%20Triad.md)
      - [Symmetric Cryptography](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Symmetric%20Cryptography.md)
      - [Asymmetric Cryptography](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Asymmetric%20Cryptography.md)
      - 디지털 서명 알고리즘 <!--ECDSA-->
      - [Blockchain Privacy Projects](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Blockchain%20Privacy%20Projects.md)
      - [Zero-Knowledge Proof](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Zero-Knowledge%20proof.md)
      - 블록체인 Attack 종류 및 대응 방안 <!--합의 알고리즘별 대응, DDos, 코드보안, Reentrancy-->
      - 키 관리 <!--HSM,Multi-sig,MPC, Shamir Secret Sharing, HD Wallet-->
      - 지갑 관리 <!--HD Wallet, -->
      - [Blockchain Privacy 프로젝트](https://github.com/JSHan94/TIL/blob/main/Blockchain/Security/Blockchain%20Privacy%20%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8.md)
    - Smart Contract
      - 스마트 컨트랙트의 개념과 동작 원리
      - 컨트랙트 개발 시 제약 사항
      - Virtual Machine <!--EVM-->
</details>


<details>
  <summary>📌 Web Develop</summary>
</details>


<details>
  <summary>📌 etc</summary>
  
- 22.07.20 
  - python attrs library에서 Optional type에 대해 인자 생성시, ₩attr.ib(converter=converters.optional(parser.parse))₩
  - core build 시 go install -> GOPATH로 binary 파일 생성, go build -> 해당 디렉토리에 빌드 폴더 생성 및 binary 파일 생성
  - git은 snapshot 방식으로 코드 관리
  - Opensource License의 경우 GPL의 경우엔 2차 창작 시 고지 의무 포함, Apache나 MIT는 자유 사용 가능, beerware (복잡하니 만나면 술이나 사줘)라는 라이센스도 존재

</details>

