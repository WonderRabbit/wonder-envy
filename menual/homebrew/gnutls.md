# gnutls

- 설치 버전: 3.8.13_2
- 역할: GNU Transport Layer Security (TLS) Library
- 분류: 의존성으로 설치

## 사용 방법

```sh
man gnutls-certtool
man gnutls-cli
man gnutls-cli-debug
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `gnutls-certtool`, `gnutls-cli`, `gnutls-cli-debug`, `gnutls-serv`, `ocsptool`, `p11tool`, `psktool`.

## 관리와 참고

설치 확인은 `brew info gnutls`. 업데이트는 필요할 때 `brew upgrade gnutls`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://gnutls.org/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/gnutls)
