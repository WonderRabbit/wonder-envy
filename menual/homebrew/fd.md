# fd

- 설치 버전: 10.5.0
- 역할: Simple, fast and user-friendly alternative to find
- 분류: 명시적 설치 도구

## 사용 방법

```sh
fd --type f '\.md$'
fd --hidden --exclude .git config
```

제공 명령: `fd`.

## 관리와 참고

설치 확인은 `brew info fd`. 업데이트는 필요할 때 `brew upgrade fd`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/sharkdp/fd)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/fd)
