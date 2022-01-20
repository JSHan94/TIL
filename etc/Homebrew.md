# Homebrew

맥, 리눅스용 패키지 관리 툴

# Install

```bash
# 설치확인 명령어
brew doctor
# Homebrew 설치 명령어
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
brew install cask
brew install mas
```

# Usage

## Brewfile 생성

- tap : Homebrew 내의 기본 저장소(Formulae라고도 함) 외의 서드 파티 저장소입니다. (tap "homebrew/bundle", tap "homebrew/cask")
- brew : Homebrew에서 제공하는 패키지를 설치할 수 있습니다. (brew "mas", brew "mysql", brew "node")
- cask : Homebrew로 제공하진 않지만 GUI 기반의 애플리케이션 (ex. Chrome, Notion 등)을 설치할 수 있습니다. (cask "visual-studio-code")
- mas : App Store에서 받을 수 있는 애플리케이션을 설치할 수 있습니다. (mas "Xcode", id: 497799835)



## install을 위한 설정 
```bash
touch install.sh
```

```sh
#!/usr/bin/env bash

# Homebrew 설치 여부 확인
if ! which brew
then
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# 스크립트 내에서 일부 sudo 권한이 필요한 명령을 수행하기 위해 root 패스워드를 입력
# sudo 권한이 필요한 이유 : cask로 설치한 애플리케이션을 바로 실행하기 위해 다운로드 된 파일에 대한 격리 속성 제거 작업
read -r -s -p "[sudo] sudo password for $(whoami):" pass

# BrewFile 실행 명령어
brew bundle

# cask로 다운로드시 웹에서 다운로드한 것과 동일하기 때문에 실행을 하면 Security 문제로 실행되지 않음
# cask로 설치한 애플리케이션을 바로 실행하기 위해 다운로드 된 파일에 대한 격리 속성 제거 작업 명령어
sudo xattr -dr com.apple.quarantine /Applications/Google\ Chrome.app
sudo xattr -dr com.apple.quarantine /Applications/Visual\ Studio\ Code.app
sudo xattr -dr com.apple.quarantine /Applications/Sublime\ Text.app
sudo xattr -dr com.apple.quarantine /Applications/Zeplin.app
sudo xattr -dr com.apple.quarantine /Applications/Notion.app
sudo xattr -dr com.apple.quarantine /Applications/Slack.app
sudo xattr -dr com.apple.quarantine /Applications/Fork.app
sudo xattr -dr com.apple.quarantine /Applications/MySQLWorkbench.app

# awscli를 사용하여 AWS 인증 정보 설정
aws configure

# 설치 성공 완료 메세지 노출
printf '\n install success! \n'
```

```bash
chmod +x ./install.sh
```

# 참고자료

[mac 셋팅 관련 github 글](https://github.com/seongjoojin/mac-dev-setup)
[Homebrew로 Mac 개발 환경 세팅 자동화](http://labs.brandi.co.kr/2020/05/26/leekh.html)

