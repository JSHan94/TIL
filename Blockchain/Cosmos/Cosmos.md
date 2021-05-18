# Cosmos

Inter Blockchain Communication (IBC)를 지원하려고 하는 차세대 블록체인 (21.05.13 기준으로는 아직 미구현..)

CBDC 프로젝트의 블록체인 플랫폼으로 선정하여 활용 중

- 동일한 애플리케이션에 대해 Multi-blockchain을 생성하여 horizontal scaling을 하는 것이 목표
 
- IBC를 이용한 역외 거래의 용이성 활용

Cosmos sdk를 이용한 손쉬운 블록체인 생성 가능

# IBC

두 블록체인 생성 후 relayer를 이용하여 패킷을 전송하고 수신하는 것이 가능함

### 개별 config 파일을 이용하여 블록체인 생성

```
starport serve -c earth.yml
starport serve -c mars.yml
```

기존에 이미 생성되었다면 블록체인을 실행

### relayer config 설정 

```
starport relayer configure --advanced --source-rpc "http://0.0.0.0:26657" --source-faucet "http://0.0.0.0:4500" --source-port "blog" --source-version "blog-1" --target-rpc "http://0.0.0.0:26659" --target-faucet "http://0.0.0.0:4501" --target-port "blog" --target-version "blog-1"
```

테스트 결과 faucet이 설정 안되면 relayer가 연결 안되는 것으로 보임

### Relayer 연결

```
starport relayer connect
```

### 패킷 전달 

```
planetd tx blog send-ibcPost blog channel-0 "Hello" "Hello Mars, I'm Alice from Earth" --from alice --chain-id earth --home ~/.earth
```
