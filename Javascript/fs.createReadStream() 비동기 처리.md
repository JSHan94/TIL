# 문제상황

fs.createReadStream()을 이용하여 CSV 파일을 읽으려하였는데 계속해서 빈 array만 리턴 됨

# 원인 

stream은 비동기적으로 파일을 chunk단위로 읽으며 수행되고, 그전에 getFileContents 함수는 이미 빈 배열을 return 해버리기 때문입니다.

# 해결 방법

https://basketdeveloper.tistory.com/69
