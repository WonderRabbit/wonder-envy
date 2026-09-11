# ripgrep

- 설치 버전: 15.2.0
- 역할: Search tool like grep and The Silver Searcher
- 분류: 명시적 설치 도구

## 사용 방법

```sh
rg --line-number --smart-case '검색어' .
rg --files
```

제공 명령: `rg`.

## 관리와 참고

설치 확인은 `brew info ripgrep`. 업데이트는 필요할 때 `brew upgrade ripgrep`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/BurntSushi/ripgrep)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/ripgrep)
