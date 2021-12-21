# 블록 암호

Block chiper는 암호화할 텍스트를 고정 길이의 블록으로 나눠 블록별로 암호화를 적용하는 암호화 알고리즘<br/>
Block chiper는 일반적으로 Feistel chiper라는 설계 전략을 사용하는 구조로 이루어짐(ex. DES)<br/>
Feistel 방식은 암호화와 복호와 연산이 거의 동일하여 복호화 할때는 암호화 과정을 역으로만 이용하면 됨<br/>
AES 같은 최신 블록 암호는 Substitution-Permutation Network(SPN)이라는 대치와 치환 연산의 조합을 사용하는 구조로 이루어짐<br/>


블록 암호는 다음과 같은 운영모드가 있음
- Electronic Code Book (ECB)
- Cipher Block Chaining (CBC)
- Output Feedback (OFB)
- Counter (CTR)

## Electronic Code Book Mode

암호화 알고리즘을 평문의 각 블록마다 하나씩 적용해 암호화된 데이터 결과를 산출하는 모드 <br/>
직관적이지만 안전하지 않으며 정보가 드러날 수 있어서 사용해선 안됨 <br/>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e6/ECB_decryption.svg/601px-ECB_decryption.svg.png"/>
</p>


## Cipher Block Chaining Mode

평문의 각 블록과 이전에 암호화된 블록에 XOR 연산을 적용함<br/>
Initialization Vector(IV)를 사용해 첫번째 블록을 암호화함. IV는 Random하게 선택하는 것이 좋음<br/>

<p align="center">
  <img src="https://www.oreilly.com/library/view/mastering-blockchain/9781788839044/assets/8d0b3db5-6132-4e27-bb69-76de9d91799b.jpg"/>
</p>

## Counter Mode

Stream cipher는 keystream(키 수열)을 사용해 비트 단위로 평문에 함호화를 적용해가는 알고리즘임<br/>  
Stream cipher는 다음과 같은 유형이 있음<br/>
- Synchronous stream cipher : Keysteam이 Key에만 종속되는 암호
- Asynchronous stream cipher : 키 수열이 암호화된 데이터에도 종속되는 암호
Stream cipher에서는 암호화와 복호화는 같은 함수이며, 기본 요구 사항은 키 수열 보안과 난수성임<br/>
Counter 모드에는 효과적으로 블록 암호를 스트림 암호로 사용함. 카운터 값에 고유한 nonce를 이어붙여 Keystream을 생성함<br/>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/3/3f/Ctr_encryption.png"/>
</p>

# DES

- 데이터 암호화 표준(Data Encryption Standard)
- DES는 고작 56비트 길이의 키를 사용하여 Brute force attack에 취약하다는 문제가 발견됨
- 삼중 DES(Triple DES, 3DES)를 도입하여 해결하였지만, 성능저하문제와 블록 크기 등에서 적합하지 않은 문제가 발생

# AES 알고리즘

- 고급 암호화 표준(Advanced Encryption Standard)
- Brute force attack 이외에 효과적으로 AES를 공격하는 방법이 발견되지 않음
- AES 표준은 128 비트 블록 크기만 허용하지만, 키 크기는 128, 192, 256 비트 모두 허용함

## 작동 방식

AES 알고리즘은 암호화를 처리하는 동안 4x4 배열 형태의 state 배열을 여러 라운드에 거쳐가며 수정하게 됨<br/>
키 크기에 따라 요구되는 라운드 수가 다름

|키 크기|필요한 라운드 수|
|---|---|
|128비트|10 라운드|
|192비트|12 라운드|
|256비트|14 라운드|

입력에 따라 암호에 대한 상태 배열을 초기화하고 나면 입력을 암호화하기 위해 4개의 연산을 수행함

1. AddRoundKey : 상태 배열을 마스터 키에서 유도된 Subkey와 XOR 함. Key schedule을 통해 입력 키를 통해 Subkey를 추출함
2. SubBytes : Lookup Table(S box)를 사용해 상태 배열의 모든 Byte를 대치함
3. ShiftRows : 첫 번째 행을 제외하고 각 행을 왼쪽으로 점진적으로 순환하는 방식으로 Shift함
4. MixColumns : 모든 Byte를 열 단위 선형 방식으로 혼합함

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/9/96/AES_Encryption_Round.png"/>
</p>

이 4가지 과정이 AES의 한 라운드에 해당되며, 최종 라운드에서는 4단계를 AddRoundKey로 대체해 이전 3단계를 되돌리지 못하게 함<br/>
각 라운드의 자세한 과정은 [여기](https://blog.naver.com/PostView.naver?blogId=wnrjsxo&logNo=221711255389)를 참고<br/>
다양한 암호화폐 지갑에서 AES 암호를 사용해 로컬에 저장돼 있는 데이터를 암호화 함<br/>
비트코인의 지갑에서는 CBC 모드로 AES-256을 사용함
