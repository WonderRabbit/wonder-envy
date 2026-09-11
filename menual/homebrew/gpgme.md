# gpgme

- 설치 버전: 2.2.0
- 역할: Library access to GnuPG
- 분류: 의존성으로 설치

## 사용 방법

```sh
man gnupg-key-manage
man gpgme-config
man gpgme-json
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `gnupg-key-manage`, `gpgme-config`, `gpgme-json`, `gpgme-tool`.

## 관리와 참고

설치 확인은 `brew info gpgme`. 업데이트는 필요할 때 `brew upgrade gpgme`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://www.gnupg.org/related_software/gpgme/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/gpgme)
