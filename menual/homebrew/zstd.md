# zstd

- 설치 버전: 1.5.7_1
- 역할: Zstandard is a real-time compression algorithm
- 분류: 명시적 설치 도구

## 사용 방법

```sh
zstd --list archive.zst
zstd --decompress --stdout archive.zst > output
```

제공 명령: `pzstd`, `unzstd`, `zstd`, `zstdcat`, `zstdgrep`, `zstdless`, `zstdmt`.

## 관리와 참고

설치 확인은 `brew info zstd`. 업데이트는 필요할 때 `brew upgrade zstd`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://facebook.github.io/zstd/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/zstd)
