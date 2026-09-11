# nettle

- 설치 버전: 4.0
- 역할: Low-level cryptographic library
- 분류: 의존성으로 설치

## 사용 방법

```sh
man nettle-hash
man nettle-lfib-stream
man nettle-pbkdf2
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `nettle-hash`, `nettle-lfib-stream`, `nettle-pbkdf2`, `pkcs1-conv`, `sexp-conv`.

## 관리와 참고

설치 확인은 `brew info nettle`. 업데이트는 필요할 때 `brew upgrade nettle`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://www.lysator.liu.se/~nisse/nettle/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/nettle)
