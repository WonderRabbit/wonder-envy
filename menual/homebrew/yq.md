# yq

- 설치 버전: 4.53.6
- 역할: Process YAML, JSON, XML, CSV and properties documents from the CLI
- 분류: 명시적 설치 도구

## 사용 방법

```sh
yq '.' config.yaml
yq -o=json '.' config.yaml | jq 'keys'
```

제공 명령: `yq`.

## 관리와 참고

설치 확인은 `brew info yq`. 업데이트는 필요할 때 `brew upgrade yq`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/mikefarah/yq)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/yq)
