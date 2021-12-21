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
