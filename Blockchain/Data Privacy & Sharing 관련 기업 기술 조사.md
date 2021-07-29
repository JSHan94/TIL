# Privacy Coins

Bitcoin의 경우 Pseduanonymous임

A->B, B->C, C->A 와 같이 해당 주소가 누군지를 알 순 없지만,

트랜잭션 그래프 분석을 통해 클러스터링 하는 것이 가능하며 

다양한 방법(거래소 분석, 채굴 풀, 다크웹 등)으로 해당 주소가 누구 것인지 아는 것이 가능함

식별화 기술은 점점 더 발전해가고 있고 BTC 익명화 기술은 정체되어있음

그렇기 때문에 프라이버시를 지키기 위해서는 새로운 기술들이 필요함

이때 프라이버시를 지킨 다는 것은 **송금자, 수신자, 금액**을 숨겨야함

## Dash

Coin Join, Mixer를 이용하여 입출력을 헷갈리게 하는 방식으로 접근

초기 Privacy 접근 방법

하지만 낮은 수준의 privacy만 제공함

## Monero

n 개 중 누가 나인지 

### 송금자 숨기기

Ring Signature
- 송금자가 5명이면, 5개의 난수를 만듬
- 만약 자신이 해당 서명 중 하나라면 (프라이빗 키를 가지고 있다면) 사이클을 만들 수 있음
- 프라이빗 키가 없을 경우에는 싸이클을 만들 수 없음
- 외부 사람이 봤을 때는 5개 중 하나의 사람임을 알 수 있음

### 수신자 숨기기 (Stealth address, one-time address)

- 수신자 주소를 그대로 사용하지 않고, 임의의 값(r)을 섞어서 만든 일회용 주소를 블록체인에 기록
- 이로 인해 동일한 사람이 10번 받아도 다 다른 주소에 보내는 것 처럼 보임
- 이때 사용한 임의의 값도 숨겨서 (R=rG) 트랜잭션에 기록
- 받는 사람은 자신의 키와 암호화된 임의의 값을 계산하여 자신에게 보낸 돈인지를 알 수 있음

cf) View Key : 다른 사람이 거래내역을 볼 수 있게 해주는 키 제공

### 금액 숨기기 (Confidential transaction)

내역 자체를 세부적으로 볼 수 없지만 거래가 말이 되는지를 확인함

- 정확한 금액은 받는 사람 주소로 암호화하여 기록하기 때문에 수신자만 알 수 있고, 제 3자는 거래가 유효한지만 아래 방식으로 검증
- 1. 트랜잭션의 입력의 합과 출력의 합이 동일하고 (즉, 돈이 새롭게 만들어지거나 사라지지 않고) - Perdersen commitment
- 2. 모든 입력과 출력이 양수임을 증명 - Range Proof

Pedersen commitment

- commitment : 나중에 실제 값을 밝히기 전에 값을 숨겨서 공개, 나중에 다른 값을 주장할 수 없음
- 마치 봉투에 미리 값을 적어서 낸 다음 확인하는 것
- 덧셈이 가능한 동형암호 성질을 가짐 commitment - 1 + 4= 2 + 3 이면 H(1) + H(4) = H(2) + H(3)
- 이를 통해 제 3자에게 값을 보여주지 않고 입력과 출력의 합이 같다는 것을 확인하는 것이 가능함

Range Proof

- 1 + 4 = 2 + 3, 1 + 4 = -95 + 100 인 상황을 막기 위해 모든 입결과 출력이 양수인지 검사
- 음수 값이 있는 것은 맞지 않기 때문에
- Bulletproofs 를 사용 하여 range proof를 합쳐서 크기 절약

## Zcash

Monero에서 더 나아가서, 과거 거래 내역(동전) 중 하나가 나임을 증명

트랜잭션 검사

- 무엇인지 알려주지 않지만, 동전이 존재하며 그 동전에 해당하는 개인키를 안다는 증명이 올바른지?
- 금액이 보이지 않지만 들어온 돈과 나가는 돈이 같은지?
- 이미 사용한 동전을 다시 사용하지 않는지?

## MimbleWimble

해리포터에서 말을 못하게 하는 마법 이름..

가명으로 본 방식을 제안함. 해당 아이디어에 영감 받아 다양한 프로젝트가 진행됨

### Coin Commitment

MimbleWimble에는 주소가 없음

여기에는 동전 단위로만 소유권을 주장할 수 있는 것임

송금 시 지갑끼리 통신하게 됨

서로 난수를 교환하며 교환 (Pedersen commitment 사용)

**Coin commitment = 난수 * G + 금액 * H**

난수와 금액을 알면 코인의 주인으로 결정

금액의 경우 입력에서 출력을 빼면 0, 난수의 차이를 트랜잭션 커널에 기록함

추가적으로 CoinJoin(cut-through)도 사용

## IP 주소 숨기기

- Monero : Kovri, Grin의 Dandelion (민들레)
- Tor 같은 onion routing 사용 (네트워크에서 바로 보내는 것이 아니라 빙빙 돌리면서 숨김)

## 대안

CoinJoin, Ring signature, ZKP 이외에도

TEE 하드웨어, MPC, 동형암호 등을 적용하여 프라이버시를 보장하는 것도 가능함

각각의 장단점 및 비용을 고려하여 적용하면 됨


# Electric Coin

Zcash를 개발한 회사로 암호화폐 투자/블록체인 스타트업.

[기술 블로그](https://electriccoin.co/blog/)


# AirBloc

AB180 (마케팅 솔루션 스타트업)에서 개발한 개인 고객들의 데이터를 기업간 sharing를 위해 사용되는 토큰.

2020년에 ETH에서 Klaytn으로 swap함.

개인적으로는 해당 비즈니스 모델이 가능성이 높다고 생각하여 오래동안 지켜봐옴. 실제로도 관련 비즈니스를 하고 싶음.

## Luft 

Luft는 실시간 유저 행동분석에 특화 된 자체 개발된 데이터스토어이다.

Kafka / S3으로 부터 각각 배치 / 실시간으로 데이터를 받아, 데이터를 사용자 별로 파티션해 저장한 후, 이를 바탕으로 OLAP 쿼리를 제공.

현재 Airbridge에서 실시간 코호트 분석 기능을 제공하는 데 사용 되고 있음.

## Airbridge

웹&앱 통합 광고 성과 어트리뷰션 솔루션 (국내에선 최초지만 해외에서 유사한 솔루션 회사를 EO 채널에서 본 기억이 있음.. 여성 대표였는데)

[Airbridge](https://www.ab180.co/solutions/airbridge)

## Airbloc Protocol

[기술 블로그 1](https://medium.com/airbloc)
[기술 블로그 2](https://blog.ab180.co/)

개인적으로 김효준님의 포스팅 글들이 도움이 많이 되었음


## 기타

[ABL 비즈니스 백서](https://docs.google.com/document/d/1LF6sloRssOR2S9fPf9O0qK5vmx6HG-duA3JF4fwuR_A/edit#heading=h.k2idc8y9sax0)
[ABL 기술 백서](https://docs.google.com/document/d/1wcF6vwZN6TmAMlt6s6WLe2jlixz0xrVX9O1E5z4Cp1s/edit?airbridge_referrer=airbridge%3Dtrue%26event_uuid%3D710d149e-2eec-4cc8-8e49-8e40762abf78%26client_id%3D98a905ea-943b-4e35-97ca-2f4d4b5a846e%26short_id%3D2ffuu%26referrer_timestamp%3D1627364863536%26channel%3Dmedium%26tracking_template_id%3D38db49e0927e8868a25bba83e04fd9b9)
[AB180 리크루팅 & 기술스택 확인](https://recruit.ab180.co/)
