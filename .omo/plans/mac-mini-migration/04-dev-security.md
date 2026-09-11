# 개발 런타임과 인증·백그라운드 항목 이전 계획

## 적용 원칙

2026-09-06 파일 존재·디렉터리 이름·안전한 설정 항목을 읽어 작성했다. 기존 런타임 버전은 참고 기록이며 Mac mini 설치 목표가 아니다. 최신 안정 버전 또는 지원되는 LTS를 기본으로 설치하고, 프로젝트가 버전을 명시한 경우에만 추가 설치한다. 아래 절차는 향후 이전 계획이며 조사 중에는 설치·서비스 실행·테스트·QA를 수행하지 않았다.

각 `~`는 해당 Mac의 사용자 홈이다. 인증 파일의 내용, 이메일·접속 호스트·토큰·개인키를 읽거나 문서에 넣지 않았다. Homebrew 전체 패키지 목록은 별도 패키지 문서를 따른다.

사용자 후속 결정: Java는 SDKMAN, Node는 nvm, Python 설치·전환은 pyenv, Python 가상환경·의존성은 uv다. [공식 문서 기반 상세 설치 계획](11-runtime-managers.md)을 우선한다.

## pyenv와 Python

### 현재 근거

`~/.pyenv/versions`에 `3.7.9`, `3.9.10`, `3.10.13`, `3.10.16`, `3.11.8`, `3.11.11`, `3.13.2` 디렉터리가 있다. `ex3-quest-01`은 `3.11.8/envs/ex3-quest-01`을 가리키는 절대 링크다. `.zshrc:228–230`에 pyenv PATH 및 초기화 참조가 있다.

### 이전 순서

1. 최신 pyenv와 Python 빌드 의존성을 [공식 안내](https://github.com/pyenv/pyenv)에 따라 설치한다.
2. 새 Mac의 기본 Python은 설치 시점 최신 안정 릴리스를 선택한다. pyenv 초기화는 `.zshrc`에 한 번만 둔다.
3. 프로젝트의 `.python-version`, `pyproject.toml`, 의존성 잠금 파일을 옮기고 필요한 Python 버전을 프로젝트 단위로 추가한다.
4. 가상환경은 uv로 새로 만든다. `uv venv --python "$(pyenv which python)"`로 pyenv가 고른 실제 Python을 지정한다. `ex3-quest-01`의 링크나 기존 `.pyenv/versions` 바이너리는 복사하지 않는다. 이 가상환경의 의존성 명세 유무는 미확인이다.
5. 기본 Python PATH는 pyenv shims가 관리하고 Conda 자동 활성화·uv 전역 Python 링크를 추가하지 않는다. 활성 `.venv`가 pyenv보다 우선할 수 있으므로 Python 변경 시 기존 가상환경도 별도로 다룬다. pyenv-virtualenv는 기본 설치 대상이 아니다.

## Conda

`.zshrc:237–250`에 `/Users/oneyoon/anaconda3`를 사용하는 초기화 블록이 있지만 조사한 `~/anaconda3` 경로는 존재하지 않았다. 실제 다른 위치의 Conda 설치까지 전수 탐색하지 않았으므로 '미설치 확정'으로 해석하지 않는다.

1. Conda를 요구하는 프로젝트가 있을 때만 최신 Apple Silicon용 배포판을 [공식 macOS 설치 안내](https://docs.conda.io/projects/conda/en/stable/user-guide/install/macos.html)에 따라 설치한다.
2. `environment.yml` 등 선언형 환경 파일로 환경을 다시 만든다. 기존 base 디렉터리 복사는 하지 않는다.
3. 기존 `anaconda3` 절대 경로 블록을 자동 복원하지 않는다. 새 설치 경로로 초기화를 구성하고 기본 셸에서 불필요한 base 자동 활성화를 피한다.

## rbenv와 Ruby

`~/.rbenv/versions/3.1.4`가 있으며 `.zshrc:84,226`에 rbenv 참조가 있다. 두 참조가 모두 실행되는지는 확인하지 않았다.

1. [공식 설치 안내](https://github.com/rbenv/rbenv)에 따라 최신 rbenv와 ruby-build를 설치한다.
2. 최신 안정 Ruby를 기본으로 설치한다. 프로젝트 `.ruby-version`·Gemfile이 요구할 때만 추가 버전을 설치한다.
3. rbenv 초기화를 한 번 등록하고 Gemfile·lockfile을 기반으로 Bundler 및 gem을 다시 설치한다. 기존 Ruby 바이너리와 native extension을 복사하지 않는다.

## SDKMAN과 JDK

`~/.sdkman/candidates/java`에는 `17.0.18-librca`, `21.0.6-librca`, `21.0.7-tem`이 있다. `current`는 `21.0.6-librca`의 절대 경로를 가리킨다. 별도로 `~/Library/Java/JavaVirtualMachines/azul-17.0.9`가 있다. `.zshrc:254–255`와 `.bash_profile:4–5`에 SDKMAN 참조가 있다.

1. [SDKMAN 설치 안내](https://sdkman.io/install/)에 따라 최신 관리자를 설치한다.
2. 설치 시점 최신 정식 JDK의 Apple Silicon 배포판을 기본으로 설치·선택한다. 프로젝트 또는 운영 환경이 장기 지원을 요구하면 최신 지원 LTS를 호환성 선택으로 사용한다. 배포판 선택과 기본값 지정은 [공식 사용법](https://sdkman.io/usage/)을 따른다.
3. `.sdkman/candidates/java`와 예전 `current` 절대 링크를 복사하지 않는다. `.sdkmanrc`, Gradle toolchain, Maven 설정이 요구하는 버전만 추가한다.
4. IntelliJ/Android Studio의 프로젝트 JDK와 Gradle JDK 설정은 새 경로로 재지정한다. 시스템 JDK, SDKMAN JDK, IDE 번들 JDK가 모두 존재할 수 있으므로 `JAVA_HOME`의 주체를 한 곳으로 정한다.
5. Azul 17 폴더는 기존 흔적 기록으로 남긴다. 프로젝트 요구가 없으면 새 Mac에 자동 재설치하지 않는다.

## rustup과 Rust

`~/.rustup/toolchains/stable-aarch64-apple-darwin`과 `~/.rustup/settings.toml`이 있다. 버전 숫자는 실행 조회하지 않았다.

1. [Rust 공식 설치 안내](https://rust-lang.org/tools/install/)에 따라 rustup으로 최신 stable Apple Silicon 도구체인을 설치한다.
2. 프로젝트의 `rust-toolchain.toml`, Cargo.toml, Cargo.lock을 옮긴다. 명시된 추가 toolchain·target만 새로 설치한다.
3. 기존 `.rustup/toolchains`와 빌드 산출물을 복사하지 않는다. Cargo로 별도 설치했던 CLI는 패키지 조사 결과에 따라 새 버전으로 재설치한다.
4. 셸 PATH에 새 Cargo bin을 등록한다. 레지스트리 인증 파일이 별도로 필요하면 사용자 인증 절차로 재설정하며 값은 문서화하지 않는다.

## Node 관리자의 확인 범위

조사한 `~/.nvm/versions/node`, `~/.fnm/node-versions`, `~/.local/share/fnm/node-versions`, `~/.asdf/installs`, `~/.local/share/mise/installs`, `~/.volta/tools/image`에서는 버전 디렉터리가 관찰되지 않았다. 이 사실만으로 Node 자체 미설치나 다른 위치의 관리자 부재를 확정하지 않는다.

Node는 사용자 결정에 따라 nvm으로 관리한다. [공식 문서 기반 설치·전환 계획](11-runtime-managers.md)을 따른다. 최신 정식 배포를 기본으로 두고 프로젝트가 요구하면 지원 LTS를 추가한다. fnm·mise·n은 기본 설치 대상이 아니다. `/usr/local/n/versions/node/20.14.0`은 기존 설치 기록으로만 남긴다.

## Android SDK

### 현재 근거

`~/Library/Android/sdk`에 다음 디렉터리가 있다.

| 종류 | 관찰된 이름 |
|---|---|
| SDK Platforms | `android-34`, `android-35` |
| Build Tools | `34.0.0`, `35.0.0`, `35.0.1` |
| NDK | `26.3.11579264`, `27.0.12077973` |
| CMake | `3.22.1` |
| Command-line Tools | `latest` |
| System Images | `android-35` |

`platform-tools`, `emulator`, `licenses`도 존재한다. 시스템 이미지 ABI·AVD 목록·개별 설치 상태는 조사하지 않았다.

### 이전 순서

1. 최신 안정 Android Studio를 설치한다. 새 SDK 위치는 기본 `~/Library/Android/sdk`를 사용한다.
2. SDK Manager에서 최신 안정 플랫폼·Platform Tools·Build Tools·Command-line Tools를 설치한다. [공식 SDK 관리 안내](https://developer.android.com/tools/sdkmanager)
3. 프로젝트의 `compileSdk`, `ndkVersion`, CMake 지정이 요구하는 경우에만 이전 버전을 추가 설치한다. SDK 폴더 전체를 복사하지 않는다.
4. 새 설치 과정에서 필요한 SDK 라이선스 동의를 진행한다. 기존 licenses 폴더를 무조건 복원하는 방식으로 대체하지 않는다.
5. 셸 SDK 경로는 `$HOME/Library/Android/sdk`로 등록하고 `platform-tools` 및 필요한 현재 Command-line Tools 경로를 추가한다. 기존 `.zshrc:90`의 `tools` 경로는 최신 구성에 필요한지 따져 새로 작성한다.
6. 프로젝트 `local.properties`의 `sdk.dir`와 IDE SDK 위치를 새 경로로 바꾼다. 프로젝트 소스에 다른 사용자의 절대 홈을 고정하지 않는다.
7. 에뮬레이터가 필요하면 새 Mac 아키텍처에 맞는 최신 안정 시스템 이미지와 AVD를 새로 만든다. 이번 계획에는 에뮬레이터 실행 단계가 없다.

## Flutter와 Dart

`/opt/homebrew/share/flutter`는 `/opt/homebrew/Caskroom/flutter/3.29.0/flutter`를 가리키지만 그 안의 `version` 파일은 `3.32.2-0.0.pre.55`다. 패키지 디렉터리 이름과 SDK 내부 버전이 일치하지 않는다. `~/.config/flutter/tool_state`도 있으며 본문은 읽지 않았다.

1. [Flutter 공식 수동 설치 안내](https://docs.flutter.dev/install/manual)에 따라 최신 stable Apple Silicon SDK를 설치한다. Homebrew 설치와 수동 SDK 설치 중 한 경로를 사용한다.
2. 이전 prerelease SDK와 Caskroom 디렉터리를 복사하지 않는다. SDK 경로가 안정적으로 유지되는 새 위치를 PATH에 등록한다.
3. 프로젝트 pubspec 및 lockfile을 옮기고 패키지를 새 SDK에서 설치한다. 프로젝트가 명시적으로 특정 Flutter를 요구할 때만 별도 버전을 추가한다.
4. IDE Flutter SDK 위치와 Android SDK 연동 경로를 새 설치에 맞춘다. `tool_state`는 필수 사용자 설정으로 보지 않는다.

## Docker Desktop

`~/.docker`에 `config.json`, `daemon.json`, `contexts`, `buildx`, `cli-plugins`, `completions`, `mcp`, `models`, `sandboxes` 등이 있다. 인증 설정 내용과 실제 컨테이너·이미지·볼륨은 조회하지 않았다.

1. [공식 Mac 설치 안내](https://docs.docker.com/desktop/setup/install/mac-install/)에 따라 최신 Apple Silicon Docker Desktop을 설치한다.
2. Compose 파일·Dockerfile·프로젝트의 선언형 설정을 우선 옮긴다. Docker CLI 링크와 completion은 새 앱 설치 위치 기준으로 등록한다.
3. `daemon.json`의 사용자 옵션을 새 버전에서 필요한 항목만 복원한다. 소켓 경로·기존 런타임 디렉터리·이전 빌더 상태를 그대로 복사하지 않는다.
4. Docker Hub와 사설 레지스트리는 새 Mac에서 다시 로그인한다. `config.json`과 credential helper는 Keychain 및 앱 설치에 의존할 수 있으므로 파일 복사만으로 인증이 이전된다고 가정하지 않는다.
5. 영속 볼륨 데이터가 필요하면 별도 데이터 이전 대상으로 관리한다. 이번 조사에서 보유 여부를 확인하지 않았으므로 삭제·초기화하지 않는다. 데이터 백업은 [Docker 공식 백업 문서](https://docs.docker.com/desktop/settings-and-maintenance/backup-and-restore/)의 볼륨·이미지·VM 데이터 구분을 따른다.

## Git

`~/.gitconfig`, `~/.config/git/ignore`가 있다. 계정·이메일·credential helper·include 대상의 내용은 읽지 않았다.

1. 최신 Git을 설치한다. 사용자 설정의 범위와 include는 [공식 git-config 문서](https://git-scm.com/docs/git-config)를 기준으로 한다.
2. `.gitconfig`와 ignore 파일을 보호된 경로로 옮기고 새 Mac의 사용자 설정에 반영한다.
3. include/includeIf, core.excludesFile, 편집기, signing 설정의 절대 경로를 새 홈으로 수정한다. 공개 계획 문서에는 사용자 이메일과 내부 저장소 주소를 넣지 않는다.
4. HTTPS 인증은 새 Mac에서 해당 서비스와 credential helper로 다시 로그인한다. SSH 또는 GPG 서명을 쓰는 저장소는 아래 별도 절차를 따른다.

## SSH

`~/.ssh/config`, `known_hosts`, `known_hosts.old`와 개인키·공개키 파일 세 쌍이 존재한다. 개인키 및 호스트 설정 내용은 읽지 않았다.

1. 새 Mac의 기본 SSH를 사용한다. 키 관리는 [OpenSSH 공식 ssh-keygen 문서](https://man.openbsd.org/ssh-keygen)를 참고한다.
2. 기본 이전 방식은 새 Mac 전용 키를 만들고 사용하는 서비스의 SSH 키 관리 화면에 공개키를 추가하는 것이다. 기존 Mac의 키는 이번 이전 작업에서 삭제하거나 폐기하지 않는다.
3. 기존 키를 유지해야 하는 조직 정책이나 접속 환경이라면 암호화된 직접 전송으로 해당 키만 옮긴다. 개인키를 Obsidian 문서·Git 저장소·공개 공유 폴더에 넣지 않는다.
4. 새 `~/.ssh` 디렉터리 권한은 `700`, 개인키와 config는 `600`으로 둔다. 접속 대상·사용자·IdentityFile 경로는 사용자가 새 Mac에 비공개로 복원한다.
5. 기존 `agent` 소켓은 복사하지 않는다. 필요할 때 새 Mac의 ssh-agent·Keychain 등록을 구성한다. 접속 시험 명령은 이 계획에 포함하지 않는다.

## GPG

`~/.gnupg/common.conf`, `public-keys.d`, `trustdb.gpg`가 있다. 조사한 `gpg.conf`, `gpg-agent.conf`는 관찰되지 않았다. 개인키 보유 여부와 서명 사용 여부는 확인하지 않았다.

1. GPG 서명이 필요한 경우 최신 GnuPG 및 필요한 macOS pinentry를 설치한다. [공식 GnuPG 문서](https://www.gnupg.org/documentation/manuals/gnupg/)
2. 실제 필요한 서명 키가 있는지 사용자가 기존 장치의 키 관리 화면에서 확인한 후, 해당 키의 공식 내보내기·가져오기 절차를 암호화된 매체로 진행한다. 문서에는 키 내용을 기록하지 않는다.
3. trustdb 파일 존재만으로 비밀키가 있다고 판단하지 않는다. 별도 하드웨어 키를 쓴다면 새 Mac의 해당 장치 연동 절차를 따른다.
4. Git signing 설정과 pinentry 실행 경로를 새 설치 위치에 맞춘다. 실행 중 agent 소켓은 옮기지 않는다.

## 사용자 LaunchAgents

현재 `~/Library/LaunchAgents`에 아래 여덟 plist가 있다. 파일명만 확인했으며 내용·실행 상태·네트워크 목적지는 읽지 않았다.

| 파일명 | 이전 처리 |
|---|---|
| `at.studio.AsideUpdater.wake.plist` | Aside 최신 앱 설치가 생성하도록 한다. |
| `at.studio.asidekeystone.agent.plist` | Aside 업데이트 구성으로 새로 설치한다. |
| `at.studio.asidekeystone.xpcservice.plist` | Aside 업데이트 구성으로 새로 설치한다. |
| `com.google.GoogleUpdater.wake.plist` | 필요한 Google 앱의 최신 설치 프로그램에 맡긴다. |
| `com.google.keystone.agent.plist` | 기존 Google 업데이트 흔적으로 기록하고 수동 복원하지 않는다. |
| `com.google.keystone.xpcservice.plist` | 기존 Google 업데이트 흔적으로 기록하고 수동 복원하지 않는다. |
| `com.microsoft.OneDriveMigrationLauncher.plist` | OneDrive를 계속 사용할 때 최신 앱의 설정 절차로 구성한다. |
| `kr.co.iniline.crossex-service.plist` | 해당 보안 모듈을 요구하는 서비스 이용 시 공식 배포 경로에서 새로 설치한다. |

파일명에서 추정한 제품 귀속이며 현재 실행 상태를 뜻하지 않는다. 기존 plist의 ProgramArguments·사용자 홈·앱 버전 경로가 새 환경과 일치한다고 가정하지 않고, 앱 설치 후 macOS 로그인 항목과 백그라운드 허용 설정에서 필요한 항목을 사용자가 관리한다. plist 복사나 launchctl 실행은 이번 작업에서 하지 않는다.

## 확인하지 않은 영역

활성 런타임 선택 결과, Homebrew와 런타임 관리자의 실제 PATH 우선순위, 조직별 인증 정책, Keychain 내부, SSH·GPG 키 내용, Docker 영속 데이터, 프로젝트별 버전 요구, AVD 세부 구성은 미확인이다. 기존 디렉터리 이름은 설치 흔적의 근거이며 실행 가능성이나 현재 사용 여부의 증거는 아니다.
