# Starport

Cosmos SDK 상에 구현되어 있는 블록체인 프레임워크

Starport accelerates chain development by scaffolding everything you need so you can focus on business logic

# 사용 시 팁

디폴트로 config.yml를 바탕으로 실행함. 이 때 체인이 생성되는 홈 디렉토리를 설정하는 것도 가능

```
planetd start --home ~/.venus # 체인 정보가 .venus에 저장됨
planetd start --home ~/.earth # 체인 정보가 .earth에 저장됨
```

또한 다른 config.yml을 생성하여 해당 config로 실행 시키는 것이 가능

```
starport serve -c venus.yml # venus.yml을 기반으로 실행
starport serve -c earth.yml # earth.yml을 기반으로 실행
```

config file 예시

```yml
accounts:
  - name: alice
    coins: ["1000token", "100000000stake"]
  - name: bob
    coins: ["500token"]
validator:
  name: alice
  staked: "100000000stake"
faucet:
  name: bob
  coins: ["5token"]
genesis:
  chain_id: "earth"
init:
  home: "$HOME/.earth"
```

# 참고자료

https://tutorials.cosmos.network/hello-world/tutorial/
