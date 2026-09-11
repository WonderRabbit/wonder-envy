# 설치 도구 사용 매뉴얼

2026-09-11 실제 설치 목록 기준. 사용자가 지정한 `menual/` 이름을 사용한다. 아래 Homebrew 항목은 직접 설치한 도구와 모든 전이 의존성을 포함한다. 수동 설치 CLI·런타임·GUI 앱은 별도 문서에 정리한다. macOS가 기본 제공하는 수천 개의 시스템 실행 파일은 별도 제품 설치 목록으로 세지 않는다.

- [Fish 기본 셸·Catppuccin·lsd](fish-and-themes.md)
- [일상 개발 흐름과 추가 6종](workflow.md)
- [LazyVim 상세 사용법](lazyvim.md)
- [Obsidian 프로젝트·카테고리 운영 매뉴얼](obsidian.md)
- [런타임·Python 도구·AI CLI](runtimes-and-ai.md)
- [GUI 앱·폰트](applications.md)
- [LazyVim 플러그인·Mason·OMO 보조 도구](plugins-and-helpers.md)
- [설치 체크리스트](../local/INSTALL-CHECKLIST.md)
- [기계 판독 설치 목록](inventory.json)

파일명·API URL은 예시이므로 실제 대상에 맞춘다. 조회와 편집·설치 명령을 구분해 실행한다.

## 전체 Homebrew Formula

| 도구 | 설치 버전 | 구분 |
| --- | --- | --- |
| [ast-grep](homebrew/ast-grep.md) | 0.45.3 | 명시적 설치 도구 |
| [atuin](homebrew/atuin.md) | 18.22.0 | 명시적 설치 도구 |
| [autoconf](homebrew/autoconf.md) | 2.73 | 의존성으로 설치 |
| [bash](homebrew/bash.md) | 5.3.15 | 명시적 설치 도구 |
| [ca-certificates](homebrew/ca-certificates.md) | 2026-08-13 | 의존성으로 설치 |
| [cairo](homebrew/cairo.md) | 1.18.4 | 의존성으로 설치 |
| [difftastic](homebrew/difftastic.md) | 0.70.0 | 명시적 설치 도구 |
| [eza](homebrew/eza.md) | 0.23.5 | 명시적 설치 도구 |
| [fd](homebrew/fd.md) | 10.5.0 | 명시적 설치 도구 |
| [fish](homebrew/fish.md) | 4.9.3 | 명시적 설치 도구 |
| [fontconfig](homebrew/fontconfig.md) | 2.18.3 | 의존성으로 설치 |
| [freetype](homebrew/freetype.md) | 2.14.3 | 의존성으로 설치 |
| [fzf](homebrew/fzf.md) | 0.74.3 | 명시적 설치 도구 |
| [gettext](homebrew/gettext.md) | 1.0 | 의존성으로 설치 |
| [gh](homebrew/gh.md) | 2.98.0, 2.100.0 | 명시적 설치 도구 |
| [giflib](homebrew/giflib.md) | 6.1.3 | 의존성으로 설치 |
| [git](homebrew/git.md) | 2.55.0 | 명시적 설치 도구 |
| [glib](homebrew/glib.md) | 2.88.3 | 의존성으로 설치 |
| [gmp](homebrew/gmp.md) | 6.3.0 | 의존성으로 설치 |
| [gnupg](homebrew/gnupg.md) | 2.5.22 | 의존성으로 설치 |
| [gnutls](homebrew/gnutls.md) | 3.8.13_2 | 의존성으로 설치 |
| [go](homebrew/go.md) | 1.27.1 | 의존성으로 설치 |
| [gpgme](homebrew/gpgme.md) | 2.2.0 | 의존성으로 설치 |
| [gpgmepp](homebrew/gpgmepp.md) | 2.2.0 | 의존성으로 설치 |
| [graphite2](homebrew/graphite2.md) | 1.3.15 | 의존성으로 설치 |
| [harfbuzz](homebrew/harfbuzz.md) | 14.4.0 | 의존성으로 설치 |
| [herdr](homebrew/herdr.md) | 0.9.0 | 명시적 설치 도구 |
| [hurl](homebrew/hurl.md) | 8.0.1 | 명시적 설치 도구 |
| [icu4c@78](homebrew/icu4c-78.md) | 78.3 | 의존성으로 설치 |
| [jpeg-turbo](homebrew/jpeg-turbo.md) | 3.2.0 | 의존성으로 설치 |
| [jq](homebrew/jq.md) | 1.8.2 | 명시적 설치 도구 |
| [json-c](homebrew/json-c.md) | 0.19 | 의존성으로 설치 |
| [lazygit](homebrew/lazygit.md) | 0.65.0 | 명시적 설치 도구 |
| [libarchive](homebrew/libarchive.md) | 3.8.9 | 의존성으로 설치 |
| [libassuan](homebrew/libassuan.md) | 3.0.2 | 의존성으로 설치 |
| [libb2](homebrew/libb2.md) | 0.98.1 | 명시적 설치 도구 |
| [libgcrypt](homebrew/libgcrypt.md) | 1.12.3 | 의존성으로 설치 |
| [libgit2](homebrew/libgit2.md) | 1.9.7 | 의존성으로 설치 |
| [libgpg-error](homebrew/libgpg-error.md) | 1.61 | 의존성으로 설치 |
| [libidn2](homebrew/libidn2.md) | 2.3.8 | 의존성으로 설치 |
| [libksba](homebrew/libksba.md) | 1.8.1 | 의존성으로 설치 |
| [libpng](homebrew/libpng.md) | 1.6.58 | 의존성으로 설치 |
| [libssh2](homebrew/libssh2.md) | 1.11.1_4 | 의존성으로 설치 |
| [libtasn1](homebrew/libtasn1.md) | 4.21.0 | 의존성으로 설치 |
| [libtiff](homebrew/libtiff.md) | 4.7.2 | 의존성으로 설치 |
| [libunistring](homebrew/libunistring.md) | 1.4.2 | 의존성으로 설치 |
| [libusb](homebrew/libusb.md) | 1.0.30 | 의존성으로 설치 |
| [libuv](homebrew/libuv.md) | 1.52.1 | 의존성으로 설치 |
| [libx11](homebrew/libx11.md) | 1.8.13 | 의존성으로 설치 |
| [libxau](homebrew/libxau.md) | 1.0.12 | 의존성으로 설치 |
| [libxcb](homebrew/libxcb.md) | 1.17.0 | 의존성으로 설치 |
| [libxdmcp](homebrew/libxdmcp.md) | 1.1.5 | 의존성으로 설치 |
| [libxext](homebrew/libxext.md) | 1.3.7 | 의존성으로 설치 |
| [libxrender](homebrew/libxrender.md) | 0.9.12 | 의존성으로 설치 |
| [little-cms2](homebrew/little-cms2.md) | 2.19.1 | 의존성으로 설치 |
| [llhttp](homebrew/llhttp.md) | 9.4.3 | 의존성으로 설치 |
| [lnav](homebrew/lnav.md) | 0.14.1 | 명시적 설치 도구 |
| [lpeg](homebrew/lpeg.md) | 1.1.0_2 | 의존성으로 설치 |
| [lsd](homebrew/lsd.md) | 1.2.0 | 명시적 설치 도구 |
| [luajit](homebrew/luajit.md) | 2.1.1788856981 | 의존성으로 설치 |
| [luv](homebrew/luv.md) | 1.52.1-0 | 의존성으로 설치 |
| [lz4](homebrew/lz4.md) | 1.10.0 | 의존성으로 설치 |
| [lzo](homebrew/lzo.md) | 2.10 | 의존성으로 설치 |
| [m4](homebrew/m4.md) | 1.4.21 | 의존성으로 설치 |
| [mdq](homebrew/mdq.md) | 0.10.0 | 명시적 설치 도구 |
| [mise](homebrew/mise.md) | 2026.9.4 | 명시적 설치 도구 |
| [ncurses](homebrew/ncurses.md) | 6.6 | 의존성으로 설치 |
| [neovim](homebrew/neovim.md) | 0.12.5_1 | 명시적 설치 도구 |
| [nettle](homebrew/nettle.md) | 4.0 | 의존성으로 설치 |
| [npth](homebrew/npth.md) | 1.8 | 의존성으로 설치 |
| [nspr](homebrew/nspr.md) | 4.40 | 의존성으로 설치 |
| [nss](homebrew/nss.md) | 3.129 | 의존성으로 설치 |
| [oh-my-posh](homebrew/oh-my-posh.md) | 31.2.1 | 명시적 설치 도구 |
| [oniguruma](homebrew/oniguruma.md) | 6.9.10 | 의존성으로 설치 |
| [openjpeg](homebrew/openjpeg.md) | 2.5.4 | 의존성으로 설치 |
| [openssl@3](homebrew/openssl-3.md) | 3.6.4 | 명시적 설치 도구 |
| [p11-kit](homebrew/p11-kit.md) | 0.26.5 | 의존성으로 설치 |
| [pcre2](homebrew/pcre2.md) | 10.47_1, 10.48 | 의존성으로 설치 |
| [pinentry](homebrew/pinentry.md) | 1.3.3 | 의존성으로 설치 |
| [pixman](homebrew/pixman.md) | 0.46.4 | 의존성으로 설치 |
| [pkgconf](homebrew/pkgconf.md) | 3.0.7 | 의존성으로 설치 |
| [poppler](homebrew/poppler.md) | 26.09.0 | 명시적 설치 도구 |
| [pyenv](homebrew/pyenv.md) | 2.8.5 | 명시적 설치 도구 |
| [readline](homebrew/readline.md) | 8.3.3 | 의존성으로 설치 |
| [resvg](homebrew/resvg.md) | 0.48.1 | 명시적 설치 도구 |
| [ripgrep](homebrew/ripgrep.md) | 15.2.0 | 명시적 설치 도구 |
| [sevenzip](homebrew/sevenzip.md) | 26.03 | 명시적 설치 도구 |
| [sqlite](homebrew/sqlite.md) | 3.53.4 | 명시적 설치 도구 |
| [stow](homebrew/stow.md) | 2.4.1 | 명시적 설치 도구 |
| [tcl-tk@8](homebrew/tcl-tk-8.md) | 8.6.18 | 명시적 설치 도구 |
| [tree](homebrew/tree.md) | 2.3.2 | 명시적 설치 도구 |
| [tree-sitter](homebrew/tree-sitter.md) | 0.27.0 | 의존성으로 설치 |
| [tree-sitter-cli](homebrew/tree-sitter-cli.md) | 0.27.0 | 명시적 설치 도구 |
| [unibilium](homebrew/unibilium.md) | 2.1.4 | 의존성으로 설치 |
| [utf8proc](homebrew/utf8proc.md) | 2.11.3 | 의존성으로 설치 |
| [webp](homebrew/webp.md) | 1.6.0 | 의존성으로 설치 |
| [worktrunk](homebrew/worktrunk.md) | 0.77.0 | 명시적 설치 도구 |
| [xorgproto](homebrew/xorgproto.md) | 2025.1 | 의존성으로 설치 |
| [xz](homebrew/xz.md) | 5.8.3 | 명시적 설치 도구 |
| [yazi](homebrew/yazi.md) | 26.9.1 | 명시적 설치 도구 |
| [yq](homebrew/yq.md) | 4.53.6 | 명시적 설치 도구 |
| [zlib](homebrew/zlib.md) | 1.3.2 | 명시적 설치 도구 |
| [zoxide](homebrew/zoxide.md) | 0.10.0 | 명시적 설치 도구 |
| [zsh-syntax-highlighting](homebrew/zsh-syntax-highlighting.md) | 0.8.0 | 명시적 설치 도구 |
| [zstd](homebrew/zstd.md) | 1.5.7_1 | 명시적 설치 도구 |
