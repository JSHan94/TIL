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


# Firestore 사용
fbase.js
```javascript
import { initializeApp } from 'firebase/app';
import { getFirestore } from "firebase/firestore";

const firebaseApp = initializeApp({
   ///
   ///
  });

const db = getFirestore();

export default db;
```

## 데이터 저장하기

공식 Docs 참조

```javascript
const docRef = await addDoc(collection(db, "users"), {
      name: name,
    });
    console.log("Document written with ID: ", docRef.id);
    } catch (e) {
        console.error("Hello Error adding document: ", e);
```
