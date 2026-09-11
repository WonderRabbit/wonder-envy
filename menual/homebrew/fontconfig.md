# fontconfig

- 설치 버전: 2.18.3
- 역할: XML-based font configuration API for X Windows
- 분류: 의존성으로 설치

## 사용 방법

```sh
fc-list
fc-match "JetBrainsMono Nerd Font"
```

제공 명령: `fc-cache`, `fc-cat`, `fc-conflist`, `fc-genconf`, `fc-list`, `fc-match`, `fc-pattern`, `fc-query`, `fc-scan`, `fc-validate`.

## 관리와 참고

설치 확인은 `brew info fontconfig`. 업데이트는 필요할 때 `brew upgrade fontconfig`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://wiki.freedesktop.org/www/Software/fontconfig/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/fontconfig)
