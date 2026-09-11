# 공식 웹 근거와 최신 패키지 상태

수집일: 2026-09-06 (한국 시간). 대상: [전체 패키지 목록](02-package-catalog.md)의 Formula 203종과 Cask 13종, 합계 216개 설치 흔적. 이전 버전을 고정하지 않고 새 Mac에서 최신 안정판을 선택하기 위한 자료다.

## 조사 범위와 해석

- Homebrew 공식 API 216개 URL을 실제 HTTP GET으로 조회했다. 212개는 HTTP 200, 4개는 HTTP 404였다. HTTP 200 중 core의 `orca`는 사용자의 앱과 다른 제품이라 적용 대상에서 제외했다.
- Formula 버전은 API `versions.stable`, Cask 버전은 `version` 필드다. Formula의 Homebrew 패키징 revision은 생략했다. API에 `generated_date`가 있는 성공 응답은 모두 2026-09-06이었다. upstream의 가장 최근 릴리스나 LTS 여부를 일괄 보증하는 값은 아니다.
- 직접 설치 Formula 47종과 Cask 13종은 별도로 공식 설치문서 또는 프로젝트 공홈을 조회했다. 아래 표의 HTTP 200은 응답 본문을 읽었다는 뜻이다. 모든 설치 절차를 실행했다는 뜻이 아니며, 공홈 첫 화면만 확보한 행은 설치문서 내용까지 확인한 것으로 간주하지 않는다.
- 전수 표의 공홈 URL은 **실시간 공식 API가 제공한 메타데이터**다. 의존성 156종의 공홈 본문을 모두 연 것은 아니다. 직접 설치 도구의 실제 공홈 열람 범위는 별도 표에 한정된다.
- 패키지 설치·업데이트·앱 실행·설정 변경·테스트·런타임 QA는 수행하지 않았다. 로컬 목록 읽기와 공개 웹 HTTP 조회, 이 Markdown 작성만 수행했다.

## 설치 경로를 바꿔야 하거나 주의할 항목

| 항목 | 공식 근거에서 확인한 상태 | 새 Mac 이전 판단 |
|---|---|---|
| python@3.9 | 3.9.25, deprecated=true, 사유 deprecated_upstream | 기본은 최신 Python. 3.9는 프로젝트 요구가 있을 때 별도 호환성 검토 |
| gemini-cli | 0.46.0, deprecated=true, 사유 unsupported, replacement antigravity-cli | 기존 설치 명령을 무조건 재사용하지 말고 대체 제품의 기능·계정 호환성을 확인한 뒤 선택. API 대체 필드를 자동 마이그레이션 승인으로 해석하지 않음 |
| alacritty | 0.17.0, disabled=true, 사유 fails_gatekeeper_check | core cask 설치를 기본 성공 경로로 제시하지 않음. 공식 INSTALL.md 경로와 대체 터미널 선택 검토 |
| orca | core API는 Plotly Orca 1.3.1로 **다른 제품** | `brew install --cask stablyai/orca/orca`의 정확한 tap을 유지. vendor 정의 버전은 1.4.197 |
| aerospace | core API 404, vendor tap 0.21.3-Beta | `brew install --cask nikitabobko/tap/aerospace`; Beta를 안정판이라고 부르지 않음 |
| spring-boot | core API 404, Spring 공식 tap 4.1.1 | `brew install spring-io/tap/spring-boot` |
| sdl2 | 기존 URL 404; sdl2-compat API aliases에 sdl2 존재, stable 2.32.72 | SDL3 기반 호환 계층으로 바뀐 점을 기록. 의존성은 상위 도구 설치에 맡김 |
| docker | 기존 cask URL 404; docker-desktop API 4.89.0,238018 | `brew install --cask docker-desktop` 한 번만 설치 |
| bun·lazygit | core에 각각 1.4.0·0.65.0 제공 | core 설치 경로도 존재. 기존 vendor tap과의 일치 여부는 별도 정의 URL 탐색 결과와 구분 |

위 버전·플래그의 항목별 원문 링크는 전수 표와 vendor 보완 표에 있다. 현재 로컬 설치본의 실행 상태나 고장 여부를 의미하지 않는다.

## Formula 전수 조회

| 기존 이름 | 현재 API 이름 | 최신 stable | deprecated / disabled | 공홈 메타데이터 | 실제 조회 근거 |
|---|---|---|---|---|---|
| ada-url | ada-url | 4.0.0 | false / false | [공홈](https://ada-url.com) | [HTTP 200](https://formulae.brew.sh/api/formula/ada-url.json) |
| age | age | 1.3.2 | false / false | [공홈](https://github.com/FiloSottile/age) | [HTTP 200](https://formulae.brew.sh/api/formula/age.json) |
| aom | aom | 3.15.0 | false / false | [공홈](https://aomedia.googlesource.com/aom) | [HTTP 200](https://formulae.brew.sh/api/formula/aom.json) |
| aribb24 | aribb24 | 1.0.4 | false / false | [공홈](https://code.videolan.org/jeeb/aribb24) | [HTTP 200](https://formulae.brew.sh/api/formula/aribb24.json) |
| ast-grep | ast-grep | 0.45.3 | false / false | [공홈](https://ast-grep.github.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/ast-grep.json) |
| autoconf | autoconf | 2.73 | false / false | [공홈](https://www.gnu.org/software/autoconf/) | [HTTP 200](https://formulae.brew.sh/api/formula/autoconf.json) |
| biome | biome | 2.5.12 | false / false | [공홈](https://biomejs.dev/) | [HTTP 200](https://formulae.brew.sh/api/formula/biome.json) |
| brotli | brotli | 1.2.0 | false / false | [공홈](https://github.com/google/brotli) | [HTTP 200](https://formulae.brew.sh/api/formula/brotli.json) |
| bun | bun | 1.4.0 | false / false | [공홈](https://bun.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/bun.json) |
| c-ares | c-ares | 1.34.8 | false / false | [공홈](https://c-ares.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/c-ares.json) |
| ca-certificates | ca-certificates | 2026-08-13 | false / false | [공홈](https://curl.se/docs/caextract.html) | [HTTP 200](https://formulae.brew.sh/api/formula/ca-certificates.json) |
| cairo | cairo | 1.18.4 | false / false | [공홈](https://cairographics.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/cairo.json) |
| certifi | certifi | 2026.7.22 | false / false | [공홈](https://github.com/certifi/python-certifi) | [HTTP 200](https://formulae.brew.sh/api/formula/certifi.json) |
| cjson | cjson | 1.7.19 | false / false | [공홈](https://github.com/DaveGamble/cJSON) | [HTTP 200](https://formulae.brew.sh/api/formula/cjson.json) |
| coreutils | coreutils | 9.11 | false / false | [공홈](https://www.gnu.org/software/coreutils/) | [HTTP 200](https://formulae.brew.sh/api/formula/coreutils.json) |
| dav1d | dav1d | 1.5.4 | false / false | [공홈](https://code.videolan.org/videolan/dav1d) | [HTTP 200](https://formulae.brew.sh/api/formula/dav1d.json) |
| deno | deno | 2.9.6 | false / false | [공홈](https://deno.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/deno.json) |
| eza | eza | 0.23.5 | false / false | [공홈](https://eza.rocks) | [HTTP 200](https://formulae.brew.sh/api/formula/eza.json) |
| fd | fd | 10.5.0 | false / false | [공홈](https://github.com/sharkdp/fd) | [HTTP 200](https://formulae.brew.sh/api/formula/fd.json) |
| ffmpeg | ffmpeg | 9.0.1 | false / false | [공홈](https://ffmpeg.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/ffmpeg.json) |
| fish | fish | 4.9.2 | false / false | [공홈](https://fishshell.com) | [HTTP 200](https://formulae.brew.sh/api/formula/fish.json) |
| flac | flac | 1.5.0 | false / false | [공홈](https://xiph.org/flac/) | [HTTP 200](https://formulae.brew.sh/api/formula/flac.json) |
| fmt | fmt | 12.2.0 | false / false | [공홈](https://fmt.dev/) | [HTTP 200](https://formulae.brew.sh/api/formula/fmt.json) |
| fontconfig | fontconfig | 2.18.3 | false / false | [공홈](https://wiki.freedesktop.org/www/Software/fontconfig/) | [HTTP 200](https://formulae.brew.sh/api/formula/fontconfig.json) |
| freetype | freetype | 2.14.3 | false / false | [공홈](https://www.freetype.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/freetype.json) |
| frei0r | frei0r | 3.5.0 | false / false | [공홈](https://frei0r.dyne.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/frei0r.json) |
| fribidi | fribidi | 1.0.16 | false / false | [공홈](https://github.com/fribidi/fribidi) | [HTTP 200](https://formulae.brew.sh/api/formula/fribidi.json) |
| fzf | fzf | 0.74.3 | false / false | [공홈](https://junegunn.github.io/fzf/) | [HTTP 200](https://formulae.brew.sh/api/formula/fzf.json) |
| gdbm | gdbm | 1.26 | false / false | [공홈](https://www.gnu.org.ua/software/gdbm/) | [HTTP 200](https://formulae.brew.sh/api/formula/gdbm.json) |
| gemini-cli | gemini-cli | 0.46.0 | true / false; unsupported | [공홈](https://geminicli.com) | [HTTP 200](https://formulae.brew.sh/api/formula/gemini-cli.json) |
| gettext | gettext | 1.0 | false / false | [공홈](https://www.gnu.org/software/gettext/) | [HTTP 200](https://formulae.brew.sh/api/formula/gettext.json) |
| gh | gh | 2.100.0 | false / false | [공홈](https://cli.github.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/gh.json) |
| giflib | giflib | 6.1.3 | false / false | [공홈](https://giflib.sourceforge.net/) | [HTTP 200](https://formulae.brew.sh/api/formula/giflib.json) |
| glib | glib | 2.88.3 | false / false | [공홈](https://docs.gtk.org/glib/) | [HTTP 200](https://formulae.brew.sh/api/formula/glib.json) |
| gmp | gmp | 6.3.0 | false / false | [공홈](https://gmplib.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/gmp.json) |
| gnupg | gnupg | 2.5.22 | false / false | [공홈](https://gnupg.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/gnupg.json) |
| gnutls | gnutls | 3.8.13 | false / false | [공홈](https://gnutls.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/gnutls.json) |
| gpgme | gpgme | 2.2.0 | false / false | [공홈](https://www.gnupg.org/related_software/gpgme/) | [HTTP 200](https://formulae.brew.sh/api/formula/gpgme.json) |
| gradle | gradle | 9.7.1 | false / false | [공홈](https://www.gradle.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/gradle.json) |
| gradle-completion | gradle-completion | 9.7.1 | false / false | [공홈](https://gradle.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/gradle-completion.json) |
| graphite2 | graphite2 | 1.3.15 | false / false | [공홈](https://graphite.sil.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/graphite2.json) |
| harfbuzz | harfbuzz | 14.4.0 | false / false | [공홈](https://github.com/harfbuzz/harfbuzz) | [HTTP 200](https://formulae.brew.sh/api/formula/harfbuzz.json) |
| hdrhistogram_c | hdrhistogram_c | 0.11.10 | false / false | [공홈](https://github.com/HdrHistogram/HdrHistogram_c) | [HTTP 200](https://formulae.brew.sh/api/formula/hdrhistogram_c.json) |
| highway | highway | 1.4.0 | false / false | [공홈](https://github.com/google/highway) | [HTTP 200](https://formulae.brew.sh/api/formula/highway.json) |
| httpie | httpie | 3.2.4 | false / false | [공홈](https://httpie.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/httpie.json) |
| icu4c@78 | icu4c@78 | 78.3 | false / false | [공홈](https://icu.unicode.org/home) | [HTTP 200](https://formulae.brew.sh/api/formula/icu4c@78.json) |
| imagemagick | imagemagick | 7.1.2-31 | false / false | [공홈](https://imagemagick.org) | [HTTP 200](https://formulae.brew.sh/api/formula/imagemagick.json) |
| imath | imath | 3.2.3 | false / false | [공홈](https://imath.readthedocs.io/en/latest/) | [HTTP 200](https://formulae.brew.sh/api/formula/imath.json) |
| isl | isl | 0.28 | false / false | [공홈](https://libisl.sourceforge.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/isl.json) |
| jasper | jasper | 4.2.9 | false / false | [공홈](https://ece.engr.uvic.ca/~frodo/jasper/) | [HTTP 200](https://formulae.brew.sh/api/formula/jasper.json) |
| jpeg-turbo | jpeg-turbo | 3.2.0 | false / false | [공홈](https://www.libjpeg-turbo.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/jpeg-turbo.json) |
| jpeg-xl | jpeg-xl | 0.12.0 | false / false | [공홈](https://jpeg.org/jpegxl/index.html) | [HTTP 200](https://formulae.brew.sh/api/formula/jpeg-xl.json) |
| jq | jq | 1.8.2 | false / false | [공홈](https://jqlang.github.io/jq/) | [HTTP 200](https://formulae.brew.sh/api/formula/jq.json) |
| kotlin-language-server | kotlin-language-server | 1.3.13 | false / false | [공홈](https://github.com/fwcd/kotlin-language-server) | [HTTP 200](https://formulae.brew.sh/api/formula/kotlin-language-server.json) |
| lame | lame | 4.0 | false / false | [공홈](https://lame.sourceforge.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/lame.json) |
| lazygit | lazygit | 0.65.0 | false / false | [공홈](https://github.com/jesseduffield/lazygit/) | [HTTP 200](https://formulae.brew.sh/api/formula/lazygit.json) |
| leptonica | leptonica | 1.87.0 | false / false | [공홈](http://www.leptonica.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/leptonica.json) |
| libarchive | libarchive | 3.8.9 | false / false | [공홈](https://www.libarchive.org) | [HTTP 200](https://formulae.brew.sh/api/formula/libarchive.json) |
| libass | libass | 0.17.5 | false / false | [공홈](https://github.com/libass/libass) | [HTTP 200](https://formulae.brew.sh/api/formula/libass.json) |
| libassuan | libassuan | 3.0.2 | false / false | [공홈](https://www.gnupg.org/related_software/libassuan/) | [HTTP 200](https://formulae.brew.sh/api/formula/libassuan.json) |
| libb2 | libb2 | 0.98.1 | false / false | [공홈](https://blake2.net/) | [HTTP 200](https://formulae.brew.sh/api/formula/libb2.json) |
| libbluray | libbluray | 1.5.0 | false / false | [공홈](https://www.videolan.org/developers/libbluray.html) | [HTTP 200](https://formulae.brew.sh/api/formula/libbluray.json) |
| libde265 | libde265 | 1.1.2 | false / false | [공홈](https://github.com/strukturag/libde265) | [HTTP 200](https://formulae.brew.sh/api/formula/libde265.json) |
| libdeflate | libdeflate | 1.26 | false / false | [공홈](https://github.com/ebiggers/libdeflate) | [HTTP 200](https://formulae.brew.sh/api/formula/libdeflate.json) |
| libevent | libevent | 2.1.13 | false / false | [공홈](https://libevent.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libevent.json) |
| libffi | libffi | 3.8.0 | false / false | [공홈](https://sourceware.org/libffi/) | [HTTP 200](https://formulae.brew.sh/api/formula/libffi.json) |
| libgcrypt | libgcrypt | 1.12.3 | false / false | [공홈](https://gnupg.org/related_software/libgcrypt/) | [HTTP 200](https://formulae.brew.sh/api/formula/libgcrypt.json) |
| libgit2 | libgit2 | 1.9.7 | false / false | [공홈](https://libgit2.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libgit2.json) |
| libgpg-error | libgpg-error | 1.61 | false / false | [공홈](https://www.gnupg.org/related_software/libgpg-error/) | [HTTP 200](https://formulae.brew.sh/api/formula/libgpg-error.json) |
| libheif | libheif | 1.23.3 | false / false | [공홈](https://www.libde265.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libheif.json) |
| libidn2 | libidn2 | 2.3.8 | false / false | [공홈](https://www.gnu.org/software/libidn/#libidn2) | [HTTP 200](https://formulae.brew.sh/api/formula/libidn2.json) |
| libksba | libksba | 1.8.1 | false / false | [공홈](https://www.gnupg.org/related_software/libksba/) | [HTTP 200](https://formulae.brew.sh/api/formula/libksba.json) |
| liblqr | liblqr | 0.4.3 | false / false | [공홈](https://liblqr.wikidot.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/liblqr.json) |
| libmicrohttpd | libmicrohttpd | 1.0.10 | false / false | [공홈](https://www.gnu.org/software/libmicrohttpd/) | [HTTP 200](https://formulae.brew.sh/api/formula/libmicrohttpd.json) |
| libmpc | libmpc | 1.4.1 | false / false | [공홈](https://www.multiprecision.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libmpc.json) |
| libnghttp2 | libnghttp2 | 1.70.0 | false / false | [공홈](https://nghttp2.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libnghttp2.json) |
| libnghttp3 | libnghttp3 | 1.18.0 | false / false | [공홈](https://nghttp2.org/nghttp3/) | [HTTP 200](https://formulae.brew.sh/api/formula/libnghttp3.json) |
| libngtcp2 | libngtcp2 | 1.25.0 | false / false | [공홈](https://nghttp2.org/ngtcp2/) | [HTTP 200](https://formulae.brew.sh/api/formula/libngtcp2.json) |
| libogg | libogg | 1.3.6 | false / false | [공홈](https://www.xiph.org/ogg/) | [HTTP 200](https://formulae.brew.sh/api/formula/libogg.json) |
| libomp | libomp | 23.1.0 | false / false | [공홈](https://openmp.llvm.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libomp.json) |
| libpng | libpng | 1.6.58 | false / false | [공홈](https://www.libpng.org/pub/png/libpng.html) | [HTTP 200](https://formulae.brew.sh/api/formula/libpng.json) |
| libraw | libraw | 0.22.2 | false / false | [공홈](https://www.libraw.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libraw.json) |
| librist | librist | 0.2.20 | false / false | [공홈](https://code.videolan.org/rist/) | [HTTP 200](https://formulae.brew.sh/api/formula/librist.json) |
| libsamplerate | libsamplerate | 0.2.2 | false / false | [공홈](https://github.com/libsndfile/libsamplerate) | [HTTP 200](https://formulae.brew.sh/api/formula/libsamplerate.json) |
| libsndfile | libsndfile | 1.2.2 | false / false | [공홈](https://libsndfile.github.io/libsndfile/) | [HTTP 200](https://formulae.brew.sh/api/formula/libsndfile.json) |
| libsodium | libsodium | 1.0.22 | false / false | [공홈](https://libsodium.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libsodium.json) |
| libsoxr | libsoxr | 0.1.3 | false / false | [공홈](https://sourceforge.net/projects/soxr/) | [HTTP 200](https://formulae.brew.sh/api/formula/libsoxr.json) |
| libssh | libssh | 0.12.2 | false / false | [공홈](https://www.libssh.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libssh.json) |
| libssh2 | libssh2 | 1.11.1 | false / false | [공홈](https://libssh2.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libssh2.json) |
| libtasn1 | libtasn1 | 4.21.0 | false / false | [공홈](https://www.gnu.org/software/libtasn1/) | [HTTP 200](https://formulae.brew.sh/api/formula/libtasn1.json) |
| libtensorflow | libtensorflow | 2.21.0 | false / false | [공홈](https://www.tensorflow.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libtensorflow.json) |
| libtiff | libtiff | 4.7.2 | false / false | [공홈](https://libtiff.gitlab.io/libtiff/) | [HTTP 200](https://formulae.brew.sh/api/formula/libtiff.json) |
| libtool | libtool | 2.6.2 | false / false | [공홈](https://www.gnu.org/software/libtool/) | [HTTP 200](https://formulae.brew.sh/api/formula/libtool.json) |
| libudfread | libudfread | 1.2.0 | false / false | [공홈](https://code.videolan.org/videolan/libudfread) | [HTTP 200](https://formulae.brew.sh/api/formula/libudfread.json) |
| libunibreak | libunibreak | 7.0 | false / false | [공홈](https://github.com/adah1972/libunibreak) | [HTTP 200](https://formulae.brew.sh/api/formula/libunibreak.json) |
| libunistring | libunistring | 1.4.2 | false / false | [공홈](https://www.gnu.org/software/libunistring/) | [HTTP 200](https://formulae.brew.sh/api/formula/libunistring.json) |
| libusb | libusb | 1.0.30 | false / false | [공홈](https://libusb.info/) | [HTTP 200](https://formulae.brew.sh/api/formula/libusb.json) |
| libuv | libuv | 1.52.1 | false / false | [공홈](https://libuv.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libuv.json) |
| libvidstab | libvidstab | 1.1.2 | false / false | [공홈](https://github.com/georgmartius/vid.stab) | [HTTP 200](https://formulae.brew.sh/api/formula/libvidstab.json) |
| libvmaf | libvmaf | 3.2.0 | false / false | [공홈](https://github.com/Netflix/vmaf) | [HTTP 200](https://formulae.brew.sh/api/formula/libvmaf.json) |
| libvorbis | libvorbis | 1.3.7 | false / false | [공홈](https://xiph.org/vorbis/) | [HTTP 200](https://formulae.brew.sh/api/formula/libvorbis.json) |
| libvpx | libvpx | 1.17.0 | false / false | [공홈](https://www.webmproject.org/code/) | [HTTP 200](https://formulae.brew.sh/api/formula/libvpx.json) |
| libx11 | libx11 | 1.8.13 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libx11.json) |
| libxau | libxau | 1.0.12 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libxau.json) |
| libxcb | libxcb | 1.17.0 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libxcb.json) |
| libxdmcp | libxdmcp | 1.1.5 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libxdmcp.json) |
| libxext | libxext | 1.3.7 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libxext.json) |
| libxrender | libxrender | 0.9.12 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/libxrender.json) |
| libyaml | libyaml | 0.2.5 | false / false | [공홈](https://github.com/yaml/libyaml) | [HTTP 200](https://formulae.brew.sh/api/formula/libyaml.json) |
| little-cms2 | little-cms2 | 2.19.1 | false / false | [공홈](https://www.littlecms.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/little-cms2.json) |
| llhttp | llhttp | 9.4.3 | false / false | [공홈](https://llhttp.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/llhttp.json) |
| lpeg | lpeg | 1.1.0 | false / false | [공홈](https://www.inf.puc-rio.br/~roberto/lpeg/) | [HTTP 200](https://formulae.brew.sh/api/formula/lpeg.json) |
| lsd | lsd | 1.2.0 | false / false | [공홈](https://github.com/lsd-rs/lsd) | [HTTP 200](https://formulae.brew.sh/api/formula/lsd.json) |
| luajit | luajit | 2.1.1788460057 | false / false | [공홈](https://luajit.org/luajit.html) | [HTTP 200](https://formulae.brew.sh/api/formula/luajit.json) |
| luv | luv | 1.52.1-0 | false / false | [공홈](https://github.com/luvit/luv) | [HTTP 200](https://formulae.brew.sh/api/formula/luv.json) |
| lz4 | lz4 | 1.10.0 | false / false | [공홈](https://lz4.github.io/lz4/) | [HTTP 200](https://formulae.brew.sh/api/formula/lz4.json) |
| lzo | lzo | 2.10 | false / false | [공홈](https://www.oberhumer.com/opensource/lzo/) | [HTTP 200](https://formulae.brew.sh/api/formula/lzo.json) |
| m4 | m4 | 1.4.21 | false / false | [공홈](https://www.gnu.org/software/m4/) | [HTTP 200](https://formulae.brew.sh/api/formula/m4.json) |
| mbedtls | mbedtls | 4.2.0 | false / false | [공홈](https://www.trustedfirmware.org/projects/mbed-tls/) | [HTTP 200](https://formulae.brew.sh/api/formula/mbedtls.json) |
| mdq | mdq | 0.10.0 | false / false | [공홈](https://github.com/yshavit/mdq) | [HTTP 200](https://formulae.brew.sh/api/formula/mdq.json) |
| merve | merve | 1.2.2 | false / false | [공홈](https://github.com/nodejs/merve) | [HTTP 200](https://formulae.brew.sh/api/formula/merve.json) |
| mingw-w64 | mingw-w64 | 14.0.0 | false / false | [공홈](https://sourceforge.net/projects/mingw-w64/) | [HTTP 200](https://formulae.brew.sh/api/formula/mingw-w64.json) |
| mkcert | mkcert | 1.4.4 | false / false | [공홈](https://github.com/FiloSottile/mkcert) | [HTTP 200](https://formulae.brew.sh/api/formula/mkcert.json) |
| mpdecimal | mpdecimal | 4.0.1 | false / false | [공홈](https://www.bytereef.org/mpdecimal/) | [HTTP 200](https://formulae.brew.sh/api/formula/mpdecimal.json) |
| mpfr | mpfr | 4.2.2 | false / false | [공홈](https://www.mpfr.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/mpfr.json) |
| mpg123 | mpg123 | 1.33.7 | false / false | [공홈](https://www.mpg123.de/) | [HTTP 200](https://formulae.brew.sh/api/formula/mpg123.json) |
| nbytes | nbytes | 0.1.4 | false / false | [공홈](https://github.com/nodejs/nbytes) | [HTTP 200](https://formulae.brew.sh/api/formula/nbytes.json) |
| ncurses | ncurses | 6.6 | false / false | [공홈](https://invisible-island.net/ncurses/announce.html) | [HTTP 200](https://formulae.brew.sh/api/formula/ncurses.json) |
| neovim | neovim | 0.12.5 | false / false | [공홈](https://neovim.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/neovim.json) |
| nettle | nettle | 4.0 | false / false | [공홈](https://www.lysator.liu.se/~nisse/nettle/) | [HTTP 200](https://formulae.brew.sh/api/formula/nettle.json) |
| node | node | 26.8.1 | false / false | [공홈](https://nodejs.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/node.json) |
| npth | npth | 1.8 | false / false | [공홈](https://gnupg.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/npth.json) |
| nspr | nspr | 4.40 | false / false | [공홈](https://hg.mozilla.org/projects/nspr) | [HTTP 200](https://formulae.brew.sh/api/formula/nspr.json) |
| nss | nss | 3.128 | false / false | [공홈](https://firefox-source-docs.mozilla.org/security/nss/index.html) | [HTTP 200](https://formulae.brew.sh/api/formula/nss.json) |
| oniguruma | oniguruma | 6.9.10 | false / false | [공홈](https://github.com/kkos/oniguruma/) | [HTTP 200](https://formulae.brew.sh/api/formula/oniguruma.json) |
| opencore-amr | opencore-amr | 0.1.6 | false / false | [공홈](https://opencore-amr.sourceforge.net/) | [HTTP 200](https://formulae.brew.sh/api/formula/opencore-amr.json) |
| openexr | openexr | 3.4.15 | false / false | [공홈](https://www.openexr.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/openexr.json) |
| openjdk | openjdk | 26.0.2.1 | false / false | [공홈](https://openjdk.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/openjdk.json) |
| openjdk@21 | openjdk@21 | 21.0.12.1 | false / false | [공홈](https://openjdk.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/openjdk@21.json) |
| openjpeg | openjpeg | 2.5.4 | false / false | [공홈](https://www.openjpeg.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/openjpeg.json) |
| openjph | openjph | 0.31.0 | false / false | [공홈](https://github.com/aous72/OpenJPH) | [HTTP 200](https://formulae.brew.sh/api/formula/openjph.json) |
| openssl@3 | openssl@3 | 3.6.4 | false / false | [공홈](https://openssl-library.org) | [HTTP 200](https://formulae.brew.sh/api/formula/openssl@3.json) |
| opus | opus | 1.6.1 | false / false | [공홈](https://www.opus-codec.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/opus.json) |
| p11-kit | p11-kit | 0.26.5 | false / false | [공홈](https://p11-glue.github.io/p11-glue/p11-kit.html) | [HTTP 200](https://formulae.brew.sh/api/formula/p11-kit.json) |
| p7zip | p7zip | 17.06 | false / false | [공홈](https://github.com/p7zip-project/p7zip) | [HTTP 200](https://formulae.brew.sh/api/formula/p7zip.json) |
| pango | pango | 1.58.2 | false / false | [공홈](https://www.gtk.org/docs/architecture/pango) | [HTTP 200](https://formulae.brew.sh/api/formula/pango.json) |
| pcre2 | pcre2 | 10.48 | false / false | [공홈](https://www.pcre.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/pcre2.json) |
| pinentry | pinentry | 1.3.3 | false / false | [공홈](https://www.gnupg.org/related_software/pinentry/) | [HTTP 200](https://formulae.brew.sh/api/formula/pinentry.json) |
| pixman | pixman | 0.46.4 | false / false | [공홈](https://cairographics.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/pixman.json) |
| pkgconf | pkgconf | 3.0.7 | false / false | [공홈](https://github.com/pkgconf/pkgconf) | [HTTP 200](https://formulae.brew.sh/api/formula/pkgconf.json) |
| poppler | poppler | 26.09.0 | false / false | [공홈](https://poppler.freedesktop.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/poppler.json) |
| pyenv | pyenv | 2.8.5 | false / false | [공홈](https://github.com/pyenv/pyenv) | [HTTP 200](https://formulae.brew.sh/api/formula/pyenv.json) |
| pyenv-virtualenv | pyenv-virtualenv | 1.4.0 | false / false | [공홈](https://github.com/pyenv/pyenv-virtualenv) | [HTTP 200](https://formulae.brew.sh/api/formula/pyenv-virtualenv.json) |
| python@3.13 | python@3.13 | 3.13.15 | false / false | [공홈](https://www.python.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/python@3.13.json) |
| python@3.14 | python@3.14 | 3.14.7 | false / false | [공홈](https://www.python.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/python@3.14.json) |
| python@3.9 | python@3.9 | 3.9.25 | true / false; deprecated_upstream | [공홈](https://www.python.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/python@3.9.json) |
| rav1e | rav1e | 0.8.1 | false / false | [공홈](https://github.com/xiph/rav1e) | [HTTP 200](https://formulae.brew.sh/api/formula/rav1e.json) |
| rbenv | rbenv | 1.3.2 | false / false | [공홈](https://rbenv.org) | [HTTP 200](https://formulae.brew.sh/api/formula/rbenv.json) |
| readline | readline | 8.3.3 | false / false | [공홈](https://tiswww.case.edu/php/chet/readline/rltop.html) | [HTTP 200](https://formulae.brew.sh/api/formula/readline.json) |
| ripgrep | ripgrep | 15.2.0 | false / false | [공홈](https://github.com/BurntSushi/ripgrep) | [HTTP 200](https://formulae.brew.sh/api/formula/ripgrep.json) |
| rubberband | rubberband | 4.0.0 | false / false | [공홈](https://breakfastquay.com/rubberband/) | [HTTP 200](https://formulae.brew.sh/api/formula/rubberband.json) |
| ruby | ruby | 4.0.6 | false / false | [공홈](https://www.ruby-lang.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/ruby.json) |
| ruby-build | ruby-build | 20260902 | false / false | [공홈](https://rbenv.org/man/ruby-build.1) | [HTTP 200](https://formulae.brew.sh/api/formula/ruby-build.json) |
| rustup | rustup | 1.29.1 | false / false | [공홈](https://rust-lang.github.io/rustup/) | [HTTP 200](https://formulae.brew.sh/api/formula/rustup.json) |
| sdl2 | 미확인 | 미확인 | 미확인 | [공홈](https://www.libsdl.org/) | [HTTP 404](https://formulae.brew.sh/api/formula/sdl2.json) |
| sevenzip | sevenzip | 26.03 | false / false | [공홈](https://7-zip.org) | [HTTP 200](https://formulae.brew.sh/api/formula/sevenzip.json) |
| shared-mime-info | shared-mime-info | 2.5.1 | false / false | [공홈](https://wiki.freedesktop.org/www/Software/shared-mime-info) | [HTTP 200](https://formulae.brew.sh/api/formula/shared-mime-info.json) |
| simdjson | simdjson | 4.6.11 | false / false | [공홈](https://simdjson.org) | [HTTP 200](https://formulae.brew.sh/api/formula/simdjson.json) |
| simdutf | simdutf | 9.1.0 | false / false | [공홈](https://simdutf.github.io/simdutf/) | [HTTP 200](https://formulae.brew.sh/api/formula/simdutf.json) |
| snappy | snappy | 1.2.2 | false / false | [공홈](https://google.github.io/snappy/) | [HTTP 200](https://formulae.brew.sh/api/formula/snappy.json) |
| sops | sops | 3.13.3 | false / false | [공홈](https://getsops.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/sops.json) |
| speex | speex | 1.2.1 | false / false | [공홈](https://speex.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/speex.json) |
| spring-boot | 미확인 | 미확인 | 미확인 | [공홈](https://spring.io/projects/spring-boot) | [HTTP 404](https://formulae.brew.sh/api/formula/spring-boot.json) |
| sqlite | sqlite | 3.53.4 | false / false | [공홈](https://sqlite.org/index.html) | [HTTP 200](https://formulae.brew.sh/api/formula/sqlite.json) |
| srt | srt | 1.5.7 | false / false | [공홈](https://www.srtalliance.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/srt.json) |
| stow | stow | 2.4.1 | false / false | [공홈](https://www.gnu.org/software/stow/) | [HTTP 200](https://formulae.brew.sh/api/formula/stow.json) |
| svt-av1 | svt-av1 | 4.2.0 | false / false | [공홈](https://gitlab.com/AOMediaCodec/SVT-AV1) | [HTTP 200](https://formulae.brew.sh/api/formula/svt-av1.json) |
| telnet | telnet | 308 | false / false | [공홈](https://opensource.apple.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/telnet.json) |
| tesseract | tesseract | 5.5.3 | false / false | [공홈](https://tesseract-ocr.github.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/tesseract.json) |
| theora | theora | 1.2.0 | false / false | [공홈](https://www.theora.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/theora.json) |
| tmux | tmux | 3.7c | false / false | [공홈](https://tmux.github.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/tmux.json) |
| tree | tree | 2.3.2 | false / false | [공홈](https://oldmanprogrammer.net/source.php?dir=projects/tree) | [HTTP 200](https://formulae.brew.sh/api/formula/tree.json) |
| tree-sitter | tree-sitter | 0.27.0 | false / false | [공홈](https://tree-sitter.github.io/) | [HTTP 200](https://formulae.brew.sh/api/formula/tree-sitter.json) |
| unbound | unbound | 1.26.0 | false / false | [공홈](https://www.unbound.net) | [HTTP 200](https://formulae.brew.sh/api/formula/unbound.json) |
| unibilium | unibilium | 2.1.4 | false / false | [공홈](https://github.com/neovim/unibilium) | [HTTP 200](https://formulae.brew.sh/api/formula/unibilium.json) |
| utf8proc | utf8proc | 2.11.3 | false / false | [공홈](https://juliastrings.github.io/utf8proc/) | [HTTP 200](https://formulae.brew.sh/api/formula/utf8proc.json) |
| uvwasi | uvwasi | 0.0.23 | false / false | [공홈](https://github.com/nodejs/uvwasi) | [HTTP 200](https://formulae.brew.sh/api/formula/uvwasi.json) |
| webp | webp | 1.6.0 | false / false | [공홈](https://developers.google.com/speed/webp/) | [HTTP 200](https://formulae.brew.sh/api/formula/webp.json) |
| wget | wget | 1.25.0 | false / false | [공홈](https://www.gnu.org/software/wget/) | [HTTP 200](https://formulae.brew.sh/api/formula/wget.json) |
| wimlib | wimlib | 1.14.5 | false / false | [공홈](https://wimlib.net/) | [HTTP 200](https://formulae.brew.sh/api/formula/wimlib.json) |
| x264 | x264 | r3222 | false / false | [공홈](https://www.videolan.org/developers/x264.html) | [HTTP 200](https://formulae.brew.sh/api/formula/x264.json) |
| x265 | x265 | 4.3 | false / false | [공홈](https://github.com/Multicorewareinc/x265) | [HTTP 200](https://formulae.brew.sh/api/formula/x265.json) |
| xorgproto | xorgproto | 2025.1 | false / false | [공홈](https://www.x.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/xorgproto.json) |
| xvid | xvid | 1.3.7 | false / false | [공홈](https://labs.xvid.com/) | [HTTP 200](https://formulae.brew.sh/api/formula/xvid.json) |
| xz | xz | 5.8.3 | false / false | [공홈](https://tukaani.org/xz/) | [HTTP 200](https://formulae.brew.sh/api/formula/xz.json) |
| yazi | yazi | 26.9.1 | false / false | [공홈](https://yazi-rs.github.io) | [HTTP 200](https://formulae.brew.sh/api/formula/yazi.json) |
| yq | yq | 4.53.6 | false / false | [공홈](https://github.com/mikefarah/yq) | [HTTP 200](https://formulae.brew.sh/api/formula/yq.json) |
| yt-dlp | yt-dlp | 2026.8.19 | false / false | [공홈](https://github.com/yt-dlp/yt-dlp) | [HTTP 200](https://formulae.brew.sh/api/formula/yt-dlp.json) |
| zeromq | zeromq | 4.3.5 | false / false | [공홈](https://zeromq.org/) | [HTTP 200](https://formulae.brew.sh/api/formula/zeromq.json) |
| zimg | zimg | 3.0.6 | false / false | [공홈](https://github.com/sekrit-twc/zimg) | [HTTP 200](https://formulae.brew.sh/api/formula/zimg.json) |
| zoxide | zoxide | 0.10.0 | false / false | [공홈](https://github.com/ajeetdsouza/zoxide) | [HTTP 200](https://formulae.brew.sh/api/formula/zoxide.json) |
| zsh-syntax-highlighting | zsh-syntax-highlighting | 0.8.0 | false / false | [공홈](https://github.com/zsh-users/zsh-syntax-highlighting) | [HTTP 200](https://formulae.brew.sh/api/formula/zsh-syntax-highlighting.json) |
| zstd | zstd | 1.5.7 | false / false | [공홈](https://facebook.github.io/zstd/) | [HTTP 200](https://formulae.brew.sh/api/formula/zstd.json) |

## Cask 전수 조회

| 기존 이름 | API 제품명 | 최신 버전 | deprecated / disabled | 공홈 메타데이터 | 실제 조회 근거 |
|---|---|---|---|---|---|
| aerospace | 미확인 | 미확인 | 미확인 | [공홈](https://github.com/nikitabobko/AeroSpace) | [HTTP 404](https://formulae.brew.sh/api/cask/aerospace.json) |
| alacritty | Alacritty | 0.17.0 | false / true; fails_gatekeeper_check | [공홈](https://github.com/alacritty/alacritty/) | [HTTP 200](https://formulae.brew.sh/api/cask/alacritty.json) |
| android-studio | Android Studio | 2026.1.4.7,quail4 | false / false | [공홈](https://developer.android.com/studio/) | [HTTP 200](https://formulae.brew.sh/api/cask/android-studio.json) |
| docker | 미확인 | 미확인 | 미확인 | [공홈](https://www.docker.com/products/docker-desktop) | [HTTP 404](https://formulae.brew.sh/api/cask/docker.json) |
| docker-desktop | Docker Desktop, Docker Community Edition, Docker CE | 4.89.0,238018 | false / false | [공홈](https://www.docker.com/products/docker-desktop) | [HTTP 200](https://formulae.brew.sh/api/cask/docker-desktop.json) |
| flutter | Flutter SDK | 3.47.2 | false / false | [공홈](https://flutter.dev/) | [HTTP 200](https://formulae.brew.sh/api/cask/flutter.json) |
| font-jetbrains-mono-nerd-font | JetBrainsMono Nerd Font families (JetBrains Mono) | 3.5.1 | false / false | [공홈](https://github.com/ryanoasis/nerd-fonts) | [HTTP 200](https://formulae.brew.sh/api/cask/font-jetbrains-mono-nerd-font.json) |
| font-meslo-lg-nerd-font | MesloLG Nerd Font families (Meslo LG) | 3.5.1 | false / false | [공홈](https://github.com/ryanoasis/nerd-fonts) | [HTTP 200](https://formulae.brew.sh/api/cask/font-meslo-lg-nerd-font.json) |
| font-symbols-only-nerd-font | Symbols Nerd Font (Symbols Only) | 3.5.1 | false / false | [공홈](https://github.com/ryanoasis/nerd-fonts) | [HTTP 200](https://formulae.brew.sh/api/cask/font-symbols-only-nerd-font.json) |
| ghostty | Ghostty | 1.3.1 | false / false | [공홈](https://ghostty.org/) | [HTTP 200](https://formulae.brew.sh/api/cask/ghostty.json) |
| marta | Marta File Manager | 0.8.2 | false / false | [공홈](https://marta.sh/) | [HTTP 200](https://formulae.brew.sh/api/cask/marta.json) |
| orca (다른 제품, 적용 제외) | Orca | 1.3.1 | false / true; fails_gatekeeper_check | [공홈](https://github.com/plotly/orca/) | [HTTP 200](https://formulae.brew.sh/api/cask/orca.json) |
| raycast | Raycast | 2.2.0.0 | false / false | [공홈](https://raycast.com/) | [HTTP 200](https://formulae.brew.sh/api/cask/raycast.json) |

## 직접 설치 도구의 공식 문서 실제 열람

전용 설치 URL, 공식 저장소 README, 프로젝트 첫 화면을 구분했다. 제목은 제품 고유명으로 원문을 유지했다. HTTP 200이어도 아래 범위보다 넓게 설치 조건을 검증한 것은 아니다.

| 도구 | 열람 범위 | 결과 | 조회 문서 |
|---|---|---|---|
| aerospace | 설치·다운로드 문서 | HTTP 200 | [AeroSpace Guide](https://nikitabobko.github.io/AeroSpace/guide) |
| age | 공식 저장소·README | HTTP 200 | [GitHub - FiloSottile/age: A simple, modern and secure encryption tool (and Go library) with small explicit keys, no config options, and UNIX-style composability. · GitHub](https://github.com/FiloSottile/age) |
| alacritty | 공식 저장소·README | HTTP 200 | [alacritty/INSTALL.md at master · alacritty/alacritty · GitHub](https://github.com/alacritty/alacritty/blob/master/INSTALL.md) |
| android-studio | 설치·다운로드 문서 | HTTP 200 | [Install Android Studio &nbsp;\|&nbsp; Android Developers](https://developer.android.com/studio/install) |
| ast-grep | 설치·다운로드 문서 | HTTP 200 | [Quick Start \| ast-grep](https://ast-grep.github.io/guide/quick-start.html) |
| biome | 설치·다운로드 문서 | HTTP 200 | [Getting Started \| Biome](https://biomejs.dev/guides/getting-started/) |
| bun | 설치·다운로드 문서 | HTTP 200 | [Installation \| Bun Docs](https://bun.com/docs/installation) |
| docker | 설치·다운로드 문서 | HTTP 200 | [Install Docker Desktop on Mac \| Docker Docs](https://docs.docker.com/desktop/setup/install/mac-install/) |
| docker-desktop | 설치·다운로드 문서 | HTTP 200 | [Install Docker Desktop on Mac \| Docker Docs](https://docs.docker.com/desktop/setup/install/mac-install/) |
| eza | 공식 공홈 | HTTP 200 | [eza \| A modern, maintained replacement for ls, written in rust](https://eza.rocks/) |
| fd | 공식 저장소·README | HTTP 200 | [GitHub - sharkdp/fd: A simple, fast and user-friendly alternative to &#39;find&#39; · GitHub](https://github.com/sharkdp/fd) |
| ffmpeg | 설치·다운로드 문서 | HTTP 200 | [Download FFmpeg](https://ffmpeg.org/download.html) |
| fish | 설치·다운로드 문서 | HTTP 200 | [Introduction &#8212; fish-shell 4.9.2 documentation](https://fishshell.com/docs/current/) |
| flutter | 설치·다운로드 문서 | HTTP 200 | [Install Flutter](https://docs.flutter.dev/install) |
| font-jetbrains-mono-nerd-font | 공식 저장소·README | HTTP 200 | [GitHub - ryanoasis/nerd-fonts: Iconic font aggregator, collection, &amp; patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, &amp; more · GitHub](https://github.com/ryanoasis/nerd-fonts) |
| font-meslo-lg-nerd-font | 공식 저장소·README | HTTP 200 | [GitHub - ryanoasis/nerd-fonts: Iconic font aggregator, collection, &amp; patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, &amp; more · GitHub](https://github.com/ryanoasis/nerd-fonts) |
| font-symbols-only-nerd-font | 공식 저장소·README | HTTP 200 | [GitHub - ryanoasis/nerd-fonts: Iconic font aggregator, collection, &amp; patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, &amp; more · GitHub](https://github.com/ryanoasis/nerd-fonts) |
| fzf | 설치·다운로드 문서 | HTTP 200 | [GitHub - junegunn/fzf: :cherry_blossom: A command-line fuzzy finder · GitHub](https://github.com/junegunn/fzf) |
| gemini-cli | 공식 공홈 | HTTP 200 | [Build, debug & deploy with AI \| Gemini CLI](https://geminicli.com/) |
| gh | 설치·다운로드 문서 | HTTP 200 | [GitHub - cli/cli: GitHub’s official command line tool · GitHub](https://github.com/cli/cli) |
| ghostty | 설치·다운로드 문서 | HTTP 200 | [Binaries and Packages - Install](https://ghostty.org/docs/install/binary) |
| gradle | 설치·다운로드 문서 | HTTP 200 | [Installing Gradle](https://docs.gradle.org/current/userguide/installation.html) |
| httpie | 공식 공홈 | HTTP 200 | [macOS - HTTPie 3.2.4 (latest) docs](https://httpie.io/docs/cli/macos) |
| imagemagick | 설치·다운로드 문서 | HTTP 200 | [Redirecting...](https://imagemagick.org/script/download.php/) |
| jq | 설치·다운로드 문서 | HTTP 200 | [Download jq](https://jqlang.org/download/) |
| kotlin-language-server | 공식 저장소·README | HTTP 200 | [GitHub - fwcd/kotlin-language-server: Kotlin code completion, diagnostics and more for any editor/IDE using the Language Server Protocol · GitHub](https://github.com/fwcd/kotlin-language-server) |
| lazygit | 공식 저장소·README | HTTP 200 | [GitHub - jesseduffield/lazygit: simple terminal UI for git commands · GitHub](https://github.com/jesseduffield/lazygit/) |
| libtensorflow | 설치·다운로드 문서 | HTTP 200 | [TensorFlow for C 설치](https://www.tensorflow.org/install/lang_c?hl=ko) |
| lsd | 공식 저장소·README | HTTP 200 | [GitHub - lsd-rs/lsd: The next gen ls command · GitHub](https://github.com/lsd-rs/lsd) |
| marta | 공식 공홈 | HTTP 200 | [Marta File Manager](https://marta.sh/) |
| mdq | 공식 저장소·README | HTTP 200 | [GitHub - yshavit/mdq: like jq but for Markdown: find specific elements in a md doc · GitHub](https://github.com/yshavit/mdq) |
| mingw-w64 | 설치·다운로드 문서 | HTTP 200 | [Pre-built Toolchains - mingw-w64](https://www.mingw-w64.org/downloads/) |
| mkcert | 공식 저장소·README | HTTP 200 | [GitHub - FiloSottile/mkcert: A simple zero-config tool to make locally trusted development certificates with any names you&#39;d like. · GitHub](https://github.com/FiloSottile/mkcert) |
| neovim | 설치·다운로드 문서 | HTTP 200 | [Install - Neovim](https://neovim.io/doc/install/) |
| node | 설치·다운로드 문서 | HTTP 200 | [Node.js — Download Node.js®](https://nodejs.org/en/download) |
| orca | 공식 공홈 | HTTP 200 | [Orca — The agent development environment](https://www.onorca.dev/) |
| p7zip | 공식 저장소·README | HTTP 200 | [GitHub - p7zip-project/p7zip: A new p7zip fork with additional codecs and improvements (forked from https://sourceforge.net/projects/sevenzip/ AND https://sourceforge.net/projects/p7zip/). · GitHub](https://github.com/p7zip-project/p7zip) |
| poppler | 공식 공홈 | HTTP 200 | [Poppler](https://poppler.freedesktop.org/) |
| pyenv | 공식 저장소·README | HTTP 200 | [GitHub - pyenv/pyenv: Simple Python version management · GitHub](https://github.com/pyenv/pyenv) |
| pyenv-virtualenv | 공식 저장소·README | HTTP 200 | [GitHub - pyenv/pyenv-virtualenv: a pyenv plugin to manage virtualenv (a.k.a. python-virtualenv) · GitHub](https://github.com/pyenv/pyenv-virtualenv) |
| python@3.9 | 설치·다운로드 문서 | HTTP 200 | [Download Python \| Python.org](https://www.python.org/downloads/) |
| raycast | 공식 공홈 | HTTP 200 | [Raycast - Your shortcut to everything](https://www.raycast.com/) |
| rbenv | 공식 공홈 | HTTP 200 | [rbenv - the Ruby version manager](https://rbenv.org/) |
| ripgrep | 공식 저장소·README | HTTP 200 | [GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories for a regex pattern while respecting your gitignore · GitHub](https://github.com/BurntSushi/ripgrep) |
| ruby | 설치·다운로드 문서 | HTTP 200 | [Installing Ruby \| Ruby](https://www.ruby-lang.org/en/documentation/installation/) |
| rustup | 설치·다운로드 문서 | HTTP 200 | [Installation - The rustup book](https://rust-lang.github.io/rustup/installation/index.html) |
| sevenzip | 설치·다운로드 문서 | HTTP 200 | [Download](https://7-zip.org/download.html) |
| sops | 공식 공홈 | HTTP 200 | [SOPS: Secrets OPerationS](https://getsops.io/) |
| spring-boot | 설치·다운로드 문서 | HTTP 200 | [Installing Spring Boot :: Spring Boot](https://docs.spring.io/spring-boot/installing.html) |
| stow | 공식 공홈 | TypeError: fetch failed | [공식 URL](https://www.gnu.org/software/stow/) |
| telnet | 공식 공홈 | HTTP 200 | [Apple Open Source](https://opensource.apple.com/) |
| tmux | 공식 공홈 | HTTP 200 | [공식 URL](https://tmux.github.io/) |
| tree | 공식 공홈 | HTTP 200 | [Home - Old Man Programmer](https://oldmanprogrammer.net/source.php?dir=projects/tree) |
| wget | 공식 공홈 | TypeError: fetch failed | [공식 URL](https://www.gnu.org/software/wget/) |
| wimlib | 공식 공홈 | HTTP 200 | [wimlib - Main page](https://wimlib.net/) |
| yazi | 설치·다운로드 문서 | HTTP 200 | [Installation \| Yazi](https://yazi-rs.github.io/docs/installation/) |
| yq | 공식 저장소·README | HTTP 200 | [GitHub - mikefarah/yq: yq is a portable command-line YAML, JSON, XML, CSV, TOML, HCL  and properties processor · GitHub](https://github.com/mikefarah/yq) |
| yt-dlp | 공식 저장소·README | HTTP 200 | [GitHub - yt-dlp/yt-dlp: A feature-rich command-line audio/video downloader · GitHub](https://github.com/yt-dlp/yt-dlp) |
| zoxide | 공식 저장소·README | HTTP 200 | [GitHub - ajeetdsouza/zoxide: A smarter cd command. Supports all major shells. · GitHub](https://github.com/ajeetdsouza/zoxide) |
| zsh-syntax-highlighting | 공식 저장소·README | HTTP 200 | [GitHub - zsh-users/zsh-syntax-highlighting: Fish shell like syntax highlighting for Zsh. · GitHub](https://github.com/zsh-users/zsh-syntax-highlighting) |

## vendor tap과 이름 변경 보완 근거

| 대상 | 실제 응답에서 읽은 정보 | 조회 결과와 URL |
|---|---|---|
| spring-tap | SpringBoot; version 4.1.1; homepage spring.io/projects/spring-boot; disable/deprecate 선언 없음 | [HTTP 200](https://raw.githubusercontent.com/spring-io/homebrew-tap/HEAD/spring-boot.rb) |
| aerospace-tap | AeroSpace; version 0.21.3-Beta; macOS Ventura 이상; disable/deprecate 선언 없음 | [HTTP 200](https://raw.githubusercontent.com/nikitabobko/homebrew-tap/HEAD/Casks/aerospace.rb) |
| orca-tap | Orca; version 1.4.197; homepage onorca.dev; arm64/x64 별도 DMG; macOS Big Sur 이상; auto_updates true; disable/deprecate 선언 없음 | [HTTP 200](https://raw.githubusercontent.com/stablyai/homebrew-orca/HEAD/Casks/orca.rb) |
| sdl2-compat | name sdl2-compat; aliases [sdl2]; stable 2.32.72; dependencies [sdl3]; deprecated=false; disabled=false | [HTTP 200](https://formulae.brew.sh/api/formula/sdl2-compat.json) |
| bun-tap | 추정한 파일 경로가 404. tap 전체나 제품 지원 중단을 의미하지 않음 | [HTTP 404](https://raw.githubusercontent.com/oven-sh/homebrew-bun/HEAD/bun.rb) |
| lazygit-tap | 추정한 파일 경로가 404. tap 전체나 제품 지원 중단을 의미하지 않음 | [HTTP 404](https://raw.githubusercontent.com/jesseduffield/homebrew-lazygit/HEAD/Formula/lazygit.rb) |

## 접근 실패와 미확인 경계

- 최초 sandbox HTTP 시도는 DNS ENOTFOUND로 실패했다. 이후 공개 자료 읽기 전용 네트워크 요청으로 위 결과를 얻었다.
- 웹 도구에서 [API 안내 루트](https://formulae.brew.sh/api/)는 safe-open 오류였다. [Node API](https://formulae.brew.sh/api/formula/node.json)는 웹 도구에서도 실제 열람했다.
- spring-boot: [조회 URL](https://formulae.brew.sh/api/formula/spring-boot.json) — HTTP 404.
- sdl2: [조회 URL](https://formulae.brew.sh/api/formula/sdl2.json) — HTTP 404.
- docker: [조회 URL](https://formulae.brew.sh/api/cask/docker.json) — HTTP 404.
- aerospace: [조회 URL](https://formulae.brew.sh/api/cask/aerospace.json) — HTTP 404.
- bun-tap: [조회 URL](https://raw.githubusercontent.com/oven-sh/homebrew-bun/HEAD/bun.rb) — HTTP 404.
- lazygit-tap: [조회 URL](https://raw.githubusercontent.com/jesseduffield/homebrew-lazygit/HEAD/Formula/lazygit.rb) — HTTP 404.
- wget: [조회 URL](https://www.gnu.org/software/wget/) — TypeError: fetch failed.
- stow: [조회 URL](https://www.gnu.org/software/stow/) — TypeError: fetch failed.

실패한 stow/wget 공홈은 설치문서 본문 근거가 없으며 Homebrew API 메타데이터만 현재 확인했다. 모든 링크는 수집 시점 기록이며 이후 릴리스·지원 정책·페이지 위치가 달라질 수 있다. 새 Mac 실행 성공 여부는 이 문서의 증거 범위 밖이다.

