# Express에서 Async/Await 적용하기


```javascript
//기본
const {Router} = require('express');
const router = Router();

router.get('/',(req,res) =>{
  res.send("hello world")
});
```

일반적으로는 비동기 처리가 대다수이기 때문에 setTimeout, Promise 적용

```javacript
//비동기 처리를 위한 setTimeout 사용
function test(){
  return new Promise(resolve=>{
    setTimeout(()=>resolve('hello world'), 3000)
  });
}

router.get('/',(req,res)=>{
  test().then(result=>res.send(result));
});
```

await 키워드는 Promise에서 사용가능하기에 test()를 awiat 해보기
```
router.get('/', async(req,res)=>{
  const result = await test();
  res.send(result);
});
```

동작은하지만 실제 환경에서 예상치 못한 오류가 발생하기에 예외처리가 필요함

에러를 잡기 위해 try/catch를 사용할 수도 있지만 코드가 nested 되며 어려워짐

이를 해결하기 위해서 데코레이터 패턴 권장

구체적인 방법은 참고 자료 확인

# 참고 자료

https://programmingsummaries.tistory.com/399
