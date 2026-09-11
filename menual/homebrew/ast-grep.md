# ast-grep

- 설치 버전: 0.45.3
- 역할: Code searching, linting, rewriting
- 분류: 명시적 설치 도구

## 사용 방법

```sh
ast-grep run --lang ts --pattern 'console.log($$$ARGS)' src/
```

제공 명령: `ast-grep`, `sg`.

## 관리와 참고

설치 확인은 `brew info ast-grep`. 업데이트는 필요할 때 `brew upgrade ast-grep`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://ast-grep.github.io/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/ast-grep)
