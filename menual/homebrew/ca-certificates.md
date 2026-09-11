# ca-certificates

- 설치 버전: 2026-08-13
- 역할: Mozilla CA certificate store
- 분류: 의존성으로 설치

## 사용 방법

```sh
brew info ca-certificates
# 독립 실행 CLI가 없는 라이브러리/자료 패키지. 상위 도구가 로드하거나 빌드 시 연결한다.
```

직접 실행보다 의존하는 앱·빌드 도구를 통해 사용한다. 프로젝트별 링크·include 옵션은 공식 문서에 따른다.

## 관리와 참고

설치 확인은 `brew info ca-certificates`. 업데이트는 필요할 때 `brew upgrade ca-certificates`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://curl.se/docs/caextract.html)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/ca-certificates)
