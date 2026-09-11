# xz

- 설치 버전: 5.8.3
- 역할: General-purpose data compression with high compression ratio
- 분류: 명시적 설치 도구

## 사용 방법

```sh
xz --list archive.xz
xz --decompress --stdout archive.xz > output
```

제공 명령: `lzcat`, `lzcmp`, `lzdiff`, `lzegrep`, `lzfgrep`, `lzgrep`, `lzless`, `lzma`, `lzmadec`, `lzmainfo`, `lzmore`, `unlzma`, `unxz`, `xz`, `xzcat`, `xzcmp`, `xzdec`, `xzdiff`, `xzegrep`, `xzfgrep`, `xzgrep`, `xzless`, `xzmore`.

## 관리와 참고

설치 확인은 `brew info xz`. 업데이트는 필요할 때 `brew upgrade xz`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://tukaani.org/xz/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/xz)
