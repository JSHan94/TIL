# 해시 함수

- 임의의 길이인 입력 문자열을 고정 길이(128비트 ~ 512비트) digest를 만드는 데 사용됨
- 해시 함수는 키가 없으며 데이터 무결성을 제공함
- 해시 함수를 구성할 때는 대개 반복 적용되는 전용 해시 함수 구성 기술을 사용
- 주로 디지털 서명과 HMAC 같은 메세지 인증코드(Message Authentication Code, MAC) 드에 사용
- 일방향 함수, 암호화 primitive, 의사 난수 생성기에도 사용됨
- 역상 저항성, 제 2역상 저항성, 충돌 저항성과 같은 보안 속성을 갖고 있음
    - 역상 저항성(preimage resistance) : 역으로 계산이 불가능함. 일방향 속성(one-way property)라고도 함 
    - 제 2 역상 저항성 : h(x)가 주어 졌을 때 m != x 이면 h(m)!=h(x)여야 한다는 것. 약 충돌 저항성(weak collision resistance)이라고도 함  
    - 충돌 저항성(collision resistance) : 각기 다른 입력 메시지의 해시 결과가 같지 않아야함. h(x) != h(z)여야 함. 강 충돌 저항성
    - 

<p align="center"><img src="https://www.oreilly.com/library/view/mastering-blockchain/9781788839044/assets/5b00db59-5445-4032-af0a-bfed9693b71c.jpg"/></p>

본질적으로 해시 함수는 충돌을 일으킬 수밖에 없지만, 충돌을 일으키는 입력을 찾아내는 것은 계산적으로 불가능하게 해야함<br/>
이를 위해 **눈사태 효과**(avalanche effect)를 이용하여 입력이 조금만 달라져도 완전히 다른 결과가 나오게 해야함<br/>
반복 해시 함수로는 **Merkle-damgard construction**이 있음<br/>

## 메세지 다이제스트

Message Digest 함수로 MD4, MD5 등이 있음. 두 함수 모두 안전하지 않아 더이상 사용하지 않아야 함

## 보안 해시 알고리즘

- SHA-0 : 1993년 도입한 160비트 함수
- SHA-1 : SSL과 TLS 구현에 일반적으로 사용됨. 이제 안전하지 않다고 간주되어 인증 기관에서 사용하지 않음
- SHA-2 : SHA-224, **SHA-256**, SHA-384, SHA-512 등이 속함. SHA-256을 이용해 PoW 함수에서 채굴자가 소모한 계산량 확인
- SHA-3 : 가장 최신 SHA 함수군. SHA-3-224,256,384,512 등이 속하며 Keccak 알고리즘을 NIST에서 표준화한 버전
- RIPEMD : RACE 무결성 프리미티브 평가 메세지 다이제스트. 비트코인 주소 생성시 RIPEMD 160을 사용함
- Whirlpool : W라는 암호를 기반으로 하며 미야구치-프리닐 압축함수를 이용

## SHA-256 설계

비트코인에서 사용되며 2<sup>64</sup> 비트보다 작은 크기의 입력 메세지를 받음<br/>
블록의 크기는 512비트이며 워드의 크기는 32비트이고, 결과는 256비트 digest임<br/>
압축 함수는 512비트 메세지 블록과 256 비트의 중간 해시 값을 처리함<br/>

1. 전처리
    - 메세지의 패딩을 사용해 블록의 크기를 512비트로 조정
    - 메세지를 블록으로 파싱하여 패딩을 포함해 512비트의 동일한 블록으로 분할
    - 초기 해시 값을 설정하는데, 8개의 32비트 워드로 이루어지며 첫 8개의 소수의 제곱근을 구해 소수 부분의 맨 앞 32를 취하여 얻음
    - 초깃값은 무작위로 선택되며 알고리즘에 백도어가 존재하지 않는다는 신뢰성을 제공함 
2. 해시 계산
    1. 각 메세지 블록을 순서대로 처리하며 전체 해시 결과를 계산(64 라운드). 동일한 라운드가 없도록 각 라운드 다른 상수를 이용
    2. 메세지 스케줄을 준비함
    3. 8개의 작업 변수를 초기화 함
    4. 중간 해시 값을 계산함
    5. 메세지를 처리한 후 결과 해시 값을 산출함 

<p align="center"><img src="https://www.cast-inc.com/sites/default/files/styles/d06/public/images/2019-06/sha-256-block.png?itok=qGZssnfA"/></p>


## SHA-3 (Keccak) 설계

SHA-3는 SHA-1,2와 상당히 다르며, 치환에 키를 사용하지 않는 unkeyed permutation을 기반으로 함<br/>
또한 임의의 길이의 입력 메세지를 처리하는데 다른 해시함수와 달리 Merkle-damgard 변환을 사용하지 않음<br/>
Sponge and squeeze construction이란 방법을 사용함<br/>
- 데이터에 패딩을 적용한 다음 스펀지에 absorbing 함
- XOR을 사용해 치환 상태의 부분집합으로 변환된 다음, 변환 상태를 나타내는 결과를 Squezze 함

<p align="center"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/SpongeConstruction.svg/300px-SpongeConstruction.svg.png"/></p>

