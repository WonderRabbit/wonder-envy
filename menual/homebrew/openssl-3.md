# openssl@3

- 설치 버전: 3.6.4
- 역할: Cryptography and SSL/TLS Toolkit
- 분류: 명시적 설치 도구

## 사용 방법

```sh
openssl version
openssl dgst -sha256 file.txt
```

제공 명령: `c_rehash`, `openssl`.

## 관리와 참고

설치 확인은 `brew info openssl@3`. 업데이트는 필요할 때 `brew upgrade openssl@3`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://openssl-library.org)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/openssl@3)
