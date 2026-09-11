# sqlite

- 설치 버전: 3.53.4
- 역할: Command-line interface for SQLite
- 분류: 명시적 설치 도구

## 사용 방법

```sh
sqlite3 -readonly database.sqlite '.tables'
```

제공 명령: `sqlite3`.

## 관리와 참고

설치 확인은 `brew info sqlite`. 업데이트는 필요할 때 `brew upgrade sqlite`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://sqlite.org/index.html)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/sqlite)
