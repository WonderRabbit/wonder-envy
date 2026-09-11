# harfbuzz

- 설치 버전: 14.4.0
- 역할: OpenType text shaping engine
- 분류: 의존성으로 설치

## 사용 방법

```sh
man hb-info
man hb-raster
man hb-shape
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `hb-info`, `hb-raster`, `hb-shape`, `hb-subset`, `hb-vector`, `hb-view`.

## 관리와 참고

설치 확인은 `brew info harfbuzz`. 업데이트는 필요할 때 `brew upgrade harfbuzz`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/harfbuzz/harfbuzz)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/harfbuzz)
