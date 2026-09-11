# stow

- 설치 버전: 2.4.1
- 역할: Organize software neatly under a single directory tree (e.g. /usr/local)
- 분류: 명시적 설치 도구

## 사용 방법

```sh
stow --simulate --target="$HOME" <package>
# dotfiles 원본 디렉터리에서 미리보기 후 적용
```

제공 명령: `chkstow`, `stow`.

## 관리와 참고

설치 확인은 `brew info stow`. 업데이트는 필요할 때 `brew upgrade stow`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://www.gnu.org/software/stow/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/stow)
