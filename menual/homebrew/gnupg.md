# gnupg

- 설치 버전: 2.5.22
- 역할: GNU Privacy Guard (OpenPGP)
- 분류: 의존성으로 설치

## 사용 방법

```sh
gpg --list-keys
gpg --verify release.sig release.tar.gz
```

제공 명령: `addgnupghome`, `applygnupgdefaults`, `dirmngr`, `dirmngr-client`, `gpg`, `gpg-agent`, `gpg-authcode-sign.sh`, `gpg-card`, `gpg-connect-agent`, `gpg-mail-tube`, `gpg-wks-client`, `gpg-wks-server`, `gpgconf`, `gpgparsemail`, `gpgscm`, `gpgsm`, `gpgsplit`, `gpgtar`, `gpgv`, `kbxutil`, `watchgnupg`.

## 관리와 참고

설치 확인은 `brew info gnupg`. 업데이트는 필요할 때 `brew upgrade gnupg`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://gnupg.org/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/gnupg)
