# glib

- 설치 버전: 2.88.3
- 역할: Core application library for C
- 분류: 의존성으로 설치

## 사용 방법

```sh
man gdbus
man gdbus-codegen
man gi-compile-repository
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `gdbus`, `gdbus-codegen`, `gi-compile-repository`, `gi-decompile-typelib`, `gi-inspect-typelib`, `gio`, `gio-querymodules`, `glib-compile-resources`, `glib-compile-schemas`, `glib-genmarshal`, `glib-gettextize`, `glib-mkenums`, `gobject-query`, `gresource`, `gsettings`, `gtester`, `gtester-report`.

## 관리와 참고

설치 확인은 `brew info glib`. 업데이트는 필요할 때 `brew upgrade glib`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://docs.gtk.org/glib/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/glib)
