# mise

- 설치 버전: 2026.9.4
- 역할: Polyglot runtime manager (asdf rust clone)
- 분류: 명시적 설치 도구

## 사용 방법

```sh
mise tasks ls
mise run env-paths
# 본 구성은 작업 실행 전용. mise use/activate로 런타임을 중복 관리하지 않음
```

제공 명령: `mise`.

## 관리와 참고

설치 확인은 `brew info mise`. 업데이트는 필요할 때 `brew upgrade mise`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://mise.jdx.dev/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/mise)
