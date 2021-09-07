# 기본 에러 메세지

- 이름 오류
- Connection Timeout
- Connection Refused

일부 공용 네트워크에서 22 port나 특정 port에 대해서 접근을 차단할 수 있기 때문에 다른 포트로 시도해볼 것(학교 네트워크도 이랬음..)

# 해결책

## 방화벽 확인

일반적으로 우분투의 경우 ufw를 이용하여 방화벽을 설정하는데

ufw를 사용하지 않는 리눅스일 경우 iptables를 이용하여 설정할 것

또한 기본적으로 ufw는 inactivate 상태가 기본이기 때문에 enable을 해줘야함

```
ufw enable
```

다음 명령어를 이용하여 각 포트별 방화벽 상태를 확인하는 것이 가능함

```
ufw stauts
```

## SSH 서비스 상태 확인

서버의 ssh 서비스가 종료되어있을 가능성 또한 존재함

다음 명령어를 통해 ssh가 제대로 동작하는지를 확인해야함

```
service ssh status
```

## SSH 서비스 포트 확인

ssh 서비스가 실행 중인 포트를 확인해야함

연구실 서버에 접속하려할 때 iptables와 ufw를 이용하여 2022로 포트를 개방하였는데 

ssh는 22, 2222 port만 서비스 중이었음... 그래서 2022는 연결되지 않았음

다음 명령어를 이용하여 서비스 중인 포트 확인이 가능함

```
grep Port /etc/ssh/sshd_config
```

만약 원하는 포트가 열려있지 않는다면 sshd_config 파일 수정

```
sudo vi /etc/ssh/sshd_config
```

서비스가 실행 중이면 서비스가 예상 포트에서 동작 중인지를 확인하는 것이 가능

netstat -plnt 를 이용해도 되지만 커널에서 소켓 정보를 쿼리하는 ss 명령이 더 선호됨

```
ss -plnt
```

포트 변경 후에는 ssh service 재시작

```
sudo service ssh restart
```

만약 해당 포트가 방화벽에 막혀 있을 경우 열어주기
```
sudo ufw allow 2222/tcp
```

제대로 포트가 열린지 확인

서비스가 실행 중이면 서비스가 예상 포트에서 동작 중인지를 확인하는 것이 가능

netstat -plnt 를 이용해도 되지만 커널에서 소켓 정보를 쿼리하는 ss 명령이 더 선호됨

```
ss -tulpn | grep 2222
```

# 참고 자료


[Droplet 자료](https://docs.digitalocean.com/products/droplets/resources/troubleshooting-ssh/connectivity/)
[다른 포트 열기](https://www.cyberciti.biz/faq/howto-change-ssh-port-on-linux-or-unix-server/)
