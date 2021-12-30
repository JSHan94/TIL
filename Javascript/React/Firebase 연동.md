# 사전 준비

<ol>
  <li/> Firebase 가입 및 프로젝트 생성
  <li/> 프로젝트 Config 파일 생성
  <li/> 프로젝트 내 firebase 인스톨
</ol>

firebase 설치
```
npm install firebase
```

fbase.js
```javascript
import { initializeApp } from 'firebase/app';
import { getDatabase } from "firebase/database";

const firebaseConfig = {
      ////
      ////
      ////
      ////
 };


firebase.initializeApp(firebaseConfig);
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);
```

# 데이터 저장하기

```javascript
```

# 데이터 삭제하기

```javascript
```

# Listener 

```javascript
```
