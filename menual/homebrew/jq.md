# jq

- 설치 버전: 1.8.2
- 역할: Lightweight and flexible command-line JSON processor
- 분류: 명시적 설치 도구

## 사용 방법

```sh
jq '.' data.json
jq 'keys' data.json
```

제공 명령: `jq`.

## 관리와 참고

설치 확인은 `brew info jq`. 업데이트는 필요할 때 `brew upgrade jq`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://jqlang.github.io/jq/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/jq)
