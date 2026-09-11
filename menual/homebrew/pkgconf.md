# pkgconf

- 설치 버전: 3.0.7
- 역할: Package compiler and linker metadata toolkit
- 분류: 의존성으로 설치

## 사용 방법

```sh
pkg-config --list-all
pkg-config --cflags --libs sqlite3
```

제공 명령: `bomtool`, `pccritic`, `pkg-config`, `pkgconf`, `spdxtool`.

## 관리와 참고

설치 확인은 `brew info pkgconf`. 업데이트는 필요할 때 `brew upgrade pkgconf`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/pkgconf/pkgconf)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/pkgconf)
