# 해결 링크

package.json의 “type” 필드에 별도의 값이 없거나 “commonjs”로 설정되어 있으면 기본 모듈 처리 방식이 require를 사용하는 commonjs 방식으로 설정되기 때문에 import 부분에서 에러가 발생했던 것이고 “type” 필드 값을 “module”로 설정한 후엔 모듈 처리 방식이 import를 사용하는 es6 방식으로 변경되었기 때문

https://takeknowledge.netlify.app/bugfix/cannot-use-import-statement-outside-a-module/
