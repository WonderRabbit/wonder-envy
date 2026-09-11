# icu4c@78

- 설치 버전: 78.3
- 역할: C/C++ and Java libraries for Unicode and globalization
- 분류: 의존성으로 설치

## 사용 방법

```sh
man derb
man escapesrc
man genbrk
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `derb`, `escapesrc`, `genbrk`, `genccode`, `gencfu`, `gencmn`, `gencnval`, `gendict`, `gennorm2`, `genrb`, `gensprep`, `icu-config`, `icuexportdata`, `icuinfo`, `icupkg`, `makeconv`, `pkgdata`, `uconv`.

## 관리와 참고

설치 확인은 `brew info icu4c@78`. 업데이트는 필요할 때 `brew upgrade icu4c@78`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://icu.unicode.org/home)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/icu4c@78)
