# hurl

- 설치 버전: 8.0.1
- 역할: Run and Test HTTP Requests with plain text and curl
- 분류: 명시적 설치 도구

## 사용 방법

```sh
hurl --test --variable base_url=http://127.0.0.1:8080 tests/http/health.hurl
```

제공 명령: `hurl`, `hurlfmt`.

## 관리와 참고

설치 확인은 `brew info hurl`. 업데이트는 필요할 때 `brew upgrade hurl`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://hurl.dev)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/hurl)
