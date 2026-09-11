# fzf

- 설치 버전: 0.74.3
- 역할: Command-line fuzzy finder written in Go
- 분류: 명시적 설치 도구

## 사용 방법

```sh
fd --type f | fzf
# Ctrl-T: 파일 후보 / Alt-C: 디렉터리 / Ctrl-R: Atuin
```

제공 명령: `fzf`, `fzf-preview.sh`, `fzf-tmux`.

## 관리와 참고

설치 확인은 `brew info fzf`. 업데이트는 필요할 때 `brew upgrade fzf`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://junegunn.github.io/fzf/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/fzf)
