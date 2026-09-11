# gettext

- 설치 버전: 1.0
- 역할: GNU internationalization (i18n) and localization (l10n) library
- 분류: 의존성으로 설치

## 사용 방법

```sh
gettext --version
# 번역 카탈로그 처리법은 공식 매뉴얼의 msgfmt/msgmerge 참고
```

제공 명령: `autopoint`, `envsubst`, `gettext`, `gettext.sh`, `gettextize`, `msgattrib`, `msgcat`, `msgcmp`, `msgcomm`, `msgconv`, `msgen`, `msgexec`, `msgfilter`, `msgfmt`, `msggrep`, `msginit`, `msgmerge`, `msgpre`, `msgunfmt`, `msguniq`, `ngettext`, `po-fetch`, `printf_gettext`, `printf_ngettext`, `recode-sr-latin`, `spit`, `xgettext`.

## 관리와 참고

설치 확인은 `brew info gettext`. 업데이트는 필요할 때 `brew upgrade gettext`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://www.gnu.org/software/gettext/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/gettext)
