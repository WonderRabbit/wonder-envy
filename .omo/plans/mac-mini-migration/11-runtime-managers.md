# SDKMAN·nvm·pyenv·uv 기반 런타임 설치 계획

> 2026-09-11 후속 적용: 기본 셸과 개발 환경은 Fish로 변경했다. 아래 과거 Zsh 운영 방침은 [계획 16](16-fish-catppuccin-lsd.md)이 대체한다. nvm·SDKMAN은 Bass로 연동하고 테마는 Catppuccin Mocha를 사용한다.

## 결정과 적용 범위

2026-09-06 사용자 결정에 따라 Java는 SDKMAN, Node.js는 nvm으로 관리한다. 후속 요청의 `penv`는 사용자가 `pyenv`로 확인했다. Python 인터프리터 설치·전환은 pyenv, 프로젝트 가상환경·의존성·도구 관리는 uv로 역할을 나눈다. 새 Mac mini에서 최신 정식 버전을 우선 설치하며 기존 버전은 재현하지 않는다. 이 문서가 기존 이전 문서의 런타임 선택 안내보다 우선한다.

공식 설치·사용법·설정 문서를 검색하고 실제 페이지를 읽어 작성했다. 아래 명령과 설정은 **새 Mac mini에서 이후 적용할 계획**이다. 현재 Mac의 설치·업데이트·셸 초기화·테스트·QA는 실행하지 않았다. 명령 출력 예시로 동작 성공을 꾸미지 않는다.

| 구분 | 설치·버전 관리자 | 사용자 기본 위치 | 프로젝트 선언 | 프로젝트 사용 방식 |
| --- | --- | --- | --- | --- |
| Java | SDKMAN | `~/.sdkman` | `.sdkmanrc` | `sdk env` |
| Node.js | nvm | `~/.nvm` | `.nvmrc` | `nvm use` |
| Python 인터프리터 | pyenv | `~/.pyenv/versions` | `.python-version` | `pyenv local`·`global`·`shell` |
| Python 환경·패키지 | uv | 프로젝트 `.venv`, 사용자 uv 도구 환경 | `pyproject.toml`, `uv.lock` | `uv sync`·`uv run`·`uv tool` |

셸은 기존 환경과 같은 Zsh, 아키텍처는 Apple Silicon을 기본으로 한다. 최신 정식 배포와 LTS는 같지 않을 수 있다. 기존의 최신 우선 결정을 유지하고, 운영·프로젝트가 LTS를 요구할 때만 예외를 둔다. Node의 Current/LTS 구분은 [Node 공식 릴리스 정책](https://nodejs.org/en/about/previous-releases)을 따른다.

## 1. 기존 환경에서 가져올 것과 제외할 것

이전 조사에서 확인한 설치 흔적에 기반한 전환표다. 현 장치의 파일을 삭제하라는 지시가 아니다.

| 현재 흔적 | 새 Mac 처리 |
| --- | --- |
| SDKMAN의 여러 JDK·`current` 절대 링크 | 설정 의도만 보관하고 최신 JDK를 재설치 |
| Homebrew Node, `/usr/local/n/versions/node/20.14.0` | 기본 Node로 복원하지 않음 |
| `~/.local/bin/{node,npm,npx}` → Hermes 내부 Node | 옛 링크를 가져오지 않음; 일반 셸 Node는 nvm이 선택 |
| 여러 prefix의 npm 전역 도구 | 패키지 이름을 기준으로 nvm의 기본 Node에서 최신 재설치 |
| pyenv 7개 Python·`ex3-quest-01` | `.python-version`과 프로젝트 의존성 명세를 가져오고 uv 환경 재생성 |
| Conda의 남은 셸 초기화 | 기본 셸에 복원하지 않음; Conda 전용 프로젝트는 별도 전환 대상 |
| pipx 설치 uv·Poetry | uv는 독립 설치, Poetry는 필요한 경우 `uv tool install poetry` |
| `~/Library/Python/3.9/bin` | 복원하지 않고 uv 도구 환경에서 진입점 재생성 |

새 셸에서는 예전 pyenv 버전 디렉터리의 수동 PATH·Conda 자동 활성화·옛 Python bin·Homebrew Node 고정 경로·수동 `JAVA_HOME` 고정값을 제외한다. Homebrew가 다른 도구의 의존성으로 Node·Python·JDK를 설치하는 것은 가능하다. 이를 억지로 삭제하지 않고 개발 셸과 IDE의 기본 런타임만 위 관리자별 역할에 맡긴다. pyenv shims는 최신 pyenv 초기화로 새로 구성한다.

## 2. 선행 준비와 설치 순서

1. 새 Mac에서 Apple Command Line Tools와 Homebrew를 준비한다. 기존 [기반 설치 절차](07-transfer-order.md)의 2단계를 따른다.
2. 최신 uv 독립 실행 파일을 설치하고 공통 사용자 bin PATH를 마련한다.
3. nvm 공식 설치자를 실행하고 Node를 설치한다.
4. SDKMAN을 설치하고 JDK를 선택한 뒤 pyenv와 Python 빌드 의존성을 설치한다.
5. 마지막에 셸 초기화 블록을 한 번씩만 남기고 프로젝트 선언·IDE·AI CLI 연결을 적용한다.

아래 설치자들은 셸 설정을 수정할 수 있다. 설치자가 추가한 블록과 이 문서의 예시를 중복해서 붙이지 않는다. dotfiles가 심볼릭 링크라면 실제 원본 파일을 편집한다. 현재 장치에서는 `.zshrc → ~/dotfiles/.zshrc`였다.

## 3. Java를 SDKMAN으로 관리

### 3.1 관리자 설치

[SDKMAN 공식 설치 문서](https://sdkman.io/install/)의 macOS 경로다.

```sh
curl -s "https://get.sdkman.io" | bash
```

설치 후 새 터미널을 열거나, 설치 시점의 같은 Zsh에서 초기화한다.

```sh
source "$HOME/.sdkman/bin/sdkman-init.sh"
```

기존 `.sdkman/candidates`를 복사하지 않는다. `~/.sdkman/etc/config`의 사용자 선호만 병합한다. Beta 채널은 사용하지 않는 기본값으로 둔다.

### 3.2 JDK 선택과 기본값

1. `sdk list java`로 설치 시점의 후보를 조회한다.
2. 공식 정식 JDK 중 최신 feature release를 제공하는 배포를 선택한다. 기존 Liberica·Temurin·Azul 이름이나 구버전을 그대로 고정하지 않는다. EA·preview는 제외한다.
3. 후보의 Identifier를 아래 `<JDK_ID>`에 넣는다. 이 표기는 실제 값으로 교체해야 하며 그대로 실행하는 명령이 아니다.

```sh
sdk install java <JDK_ID>
sdk default java <JDK_ID>
sdk use java <JDK_ID>
```

`default`는 이후 셸의 기본값, `use`는 현재 셸의 선택이다. `sdk install java`는 공식 문서의 기본 stable 설치 경로지만, 그 기본 후보가 모든 공급자 중 가장 높은 feature release라는 의미로 해석하지 않는다. 최신 우선 정책에서는 후보 목록에서 Identifier를 명시한다. [SDKMAN 사용법](https://sdkman.io/usage/)

### 3.3 프로젝트별 JDK

프로젝트에서 선택한 JDK를 사용 중인 상태로 다음을 수행한다.

```sh
sdk env init
```

생성된 `.sdkmanrc`의 `java=` 값을 그 프로젝트의 실제 Identifier로 유지한다. 기존 파일이 있으면 새로 덮어쓰지 않고 그 요구를 따른다. 새 장치에서 필요한 JDK를 준비하고 적용하는 순서는 다음과 같다.

```sh
sdk env install
sdk env
```

프로젝트 밖에서는 `sdk env clear`로 기본값으로 돌아간다. 초기 계획은 명시적 전환으로 두며, 자동 전환을 원할 때만 `~/.sdkman/etc/config`의 `sdkman_auto_env=true`를 사용한다. [환경 전환 공식 설명](https://sdkman.io/usage/#env-command)

IntelliJ·Android Studio의 Project SDK와 Gradle JVM은 `~/.sdkman/candidates/java/<JDK_ID>`를 선택한다. IDE 번들 JDK는 IDE 자체 실행용일 수 있다. Gradle toolchain·프로젝트 wrapper 요구를 전역 최신 JDK로 무조건 바꾸지 않는다.

### 3.4 나중의 업데이트

`sdk selfupdate`는 관리자 업데이트, `sdk update`는 후보 정보 갱신이다. 새 JDK는 후보 선택 → 설치 → default 지정 순서로 추가한다. `.sdkmanrc`의 프로젝트 고정값은 별도 변경이며 기존 JDK 제거는 이 계획에 포함하지 않는다.

## 4. Node.js를 nvm으로 관리

### 4.1 관리자 설치

[nvm 공식 README](https://github.com/nvm-sh/nvm#install--update-script)의 조회일 설치자 버전은 `v0.40.7`이다. 실제 설치일에는 공식 README가 제공하는 최신 태그를 사용한다. Node 버전을 이 태그로 고정한다는 뜻은 아니다.

```sh
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.7/install.sh | bash
```

nvm의 Homebrew 설치는 upstream 지원 경로가 아니므로 여기서는 사용하지 않는다. nvm은 셸 함수이며 GUI 앱에 자동 적용되는 시스템 실행 파일이 아니다.

### 4.2 최신 Node와 기본값

새 터미널에서 다음 순서로 구성한다.

```sh
nvm install node
nvm alias default node
nvm use default
```

`node`는 최신 정식 릴리스, default의 `node` 별칭은 최신 **설치된** 버전을 뜻한다. 자동 다운로드 업데이트는 아니다. LTS가 필요한 프로젝트에만 `nvm install --lts`를 추가한다.

### 4.3 프로젝트별 전환

`.nvmrc`에 프로젝트에서 선택한 정확한 `vMAJOR.MINOR.PATCH`를 한 줄로 기록한다. 기존 프로젝트는 기존 선언을 유지한다.

```sh
nvm install
nvm use
```

기본 nvm은 디렉터리 이동만으로 자동 전환하지 않는다. 초기 계획은 명시적 `nvm use`다. 프로젝트를 떠난 뒤에는 `nvm use default`로 복귀한다.

### 4.4 npm 전역 도구와 충돌 방지

전역 패키지는 Node 버전별로 분리된다. 기본 Node를 선택한 뒤 필요한 패키지를 최신 설치한다. `sudo npm`과 사용자 지정 전역 prefix는 사용하지 않는다. 기존 `.npmrc`의 `prefix=`, 환경 변수 `NPM_CONFIG_PREFIX`·`PREFIX`는 nvm과 충돌하므로 새 설정에 가져오지 않는다. 해당 값의 현재 존재 여부는 이번에 재조회하지 않았다.

새 버전에서도 항상 필요한 패키지명은 `~/.nvm/default-packages`에 한 줄씩 넣을 수 있다. 예를 들어 npm 경로로 관리할 Codex와 Mermaid CLI만 선택했다면 다음 내용이다.

```text
@openai/codex
@mermaid-js/mermaid-cli
```

Codex를 독립 설치자로 관리한다면 위 Codex 행은 제외한다. Node 변경 뒤 AI CLI가 사라진 경우 다른 Node에 설치된 전역 패키지일 수 있다. 새 Node에서 필요한 이름을 재설치한다. [전역 패키지·설정 호환성 근거](https://github.com/nvm-sh/nvm#default-global-packages-from-file-while-installing)

## 5. Python을 pyenv와 uv로 관리

### 5.1 uv 독립 설치

uv는 Python을 먼저 설치하지 않아도 되는 독립 배포를 선택한다. 기존 pipx 또는 Homebrew uv 설치 계획을 이 방식으로 대체한다. [uv 공식 설치 안내](https://docs.astral.sh/uv/getting-started/installation/)

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

설치자가 출력한 PATH 안내를 따른다. macOS 기본 사용자 실행 경로는 보통 `~/.local/bin`이며 XDG 사용자 설정이 있으면 달라질 수 있다. 독립 설치본의 이후 업데이트는 `uv self update`다.

### 5.2 pyenv와 Python 빌드 의존성 설치

[pyenv 공식 macOS 설치 안내](https://github.com/pyenv/pyenv#installation)에 따라 Homebrew의 최신 정식 pyenv를 설치한다. HEAD 개발판은 선택하지 않는다.

```sh
brew install pyenv
brew install openssl@3 readline sqlite3 xz tcl-tk@8 libb2 zstd zlib pkgconfig
```

두 번째 줄은 열람한 [공식 권장 빌드 환경](https://github.com/pyenv/pyenv/wiki#suggested-build-environment)의 macOS 예시다. `tcl-tk@8`은 빌드 의존성 호환 선택이며 Python 버전을 과거로 고정한다는 뜻이 아니다. 설치일의 공식 목록과 선택한 Python의 요구가 달라지면 그 목록을 따른다. pyenv는 보통 Python을 소스 빌드하므로 다운로드형 uv Python보다 설치 시간이 길 수 있다. 빌드는 향후 설치의 일부이며 이번 문서 작성에서는 실행하지 않는다.

`pyenv-virtualenv`는 추가하지 않는다. 가상환경 관리 주체는 uv다. 새 Zsh 초기화 예시는 6절에 있다.

### 5.3 최신 Python과 사용자 기본값

최신 pyenv가 알고 있는 정식 Python 3 계열을 설치하고 사용자 기본값으로 선택한다.

```sh
pyenv install 3
pyenv global 3
```

`install 3`은 알려진 최신 버전, `global 3`은 설치된 최신 버전으로 해석한다. 프로젝트에서는 정확한 `major.minor.patch`를 사용한다. 실제 숫자는 설치 시 선택된 버전으로 기록한다. `pyenv latest -k 3`은 설치 후보 식별 명령이며 Python 프로그램을 실행하는 명령이 아니다. [pyenv 명령 참조](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md)

Homebrew Python·예전 uv Python·시스템 Python은 pyenv 설치본으로 간주하지 않는다. 원본 Mac의 `.pyenv/versions`와 가상환경 링크는 복사하지 않는다.

### 5.4 uv가 pyenv Python을 사용하도록 설정

`~/.config/uv/uv.toml`의 기본 계획은 다음과 같다.

```toml
python-preference = "only-system"
python-downloads = "never"
```

uv는 pyenv 설치본도 **system Python**으로 분류한다. 여기서 system은 macOS 내장 Python만 뜻하지 않는다. 따라서 기존 uv 전용 초안의 `only-managed`는 이 조합과 맞지 않아 대체했다. `never`는 uv가 별도 Python을 다운로드하지 않게 한다. [분류 공식 설명](https://docs.astral.sh/uv/concepts/python-versions/#managed-and-system-python-installations), [설정 참조](https://docs.astral.sh/uv/reference/settings/#python-preference)

이 설정만으로 pyenv 출처가 보장되지는 않는다. Homebrew 등도 system 범주이므로 환경 생성 시 **pyenv가 고른 실제 실행 파일**을 명시한다. 오래된 `UV_PYTHON`, `UV_PYTHON_PREFERENCE` 같은 환경 변수나 프로젝트 설정이 사용자 기본값을 재정의하지 않도록 새 설정에 반영한다. 프로젝트 설정은 사용자 설정보다 우선할 수 있다. [설정 우선순위](https://docs.astral.sh/uv/concepts/configuration-files/)

### 5.5 새 프로젝트 구성

`<PYTHON_VERSION>`은 설치된 정확한 숫자로 바꾸는 자리 표시자다. 새 프로젝트 폴더에서 다음 순서로 구성한다.

```sh
pyenv local <PYTHON_VERSION>
uv init --python "$(pyenv which python)"
uv venv --python "$(pyenv which python)"
uv sync
```

`pyenv local`이 작성한 `.python-version`은 pyenv와 uv가 함께 읽는다. `uv init` 이후에도 파일 내용은 정확한 숫자 한 줄로 유지한다. pyenv와 uv 양쪽에서 서로 다른 표기나 값을 반복해서 쓰지 않는다. `pyproject.toml`의 `requires-python`은 패키지 호환 범위, `.python-version`은 로컬 인터프리터 선택이다. [uv 프로젝트 가이드](https://docs.astral.sh/uv/guides/projects/)

이 순서는 새 폴더 기준이다. 기존 `pyproject.toml`이 있는 프로젝트에 `uv init`을 반복하지 않는다.

### 5.6 기존 프로젝트 이전

1. 소스·`.python-version`·`pyproject.toml`·`uv.lock`을 보관한다. 기존 `.venv`는 복사하지 않는다.
2. 버전 파일의 Python을 pyenv로 설치한다. 예전 파일에 `ex3-quest-01` 같은 pyenv-virtualenv 환경명이 있으면 실제 Python 숫자로 바꾸고 의존성 명세를 별도로 확보한다.
3. 예전 가상환경을 활성화하지 않은 새 셸에서 다음 순서로 구성한다.

```sh
pyenv install <PYTHON_VERSION>
pyenv local <PYTHON_VERSION>
uv venv --python "$(pyenv which python)"
uv sync --locked
```

이미 설치된 Python은 설치 단계를 건너뛴다. `--locked`가 선언과 잠금 파일 불일치로 중단되면 무조건 잠금을 갱신하지 않는다. 최신 우선은 새 기본 환경의 정책이며 기존 프로젝트의 호환성 요구를 삭제하는 뜻이 아니다.

requirements 기반 프로젝트는 가상환경 생성 후 `uv pip install -r requirements.txt`를 사용한다. 기존 Poetry 프로젝트는 Poetry를 uv tool로 설치해 기존 방식을 유지하거나, 의존성 명세를 uv 형식으로 전환하는 작업을 별도로 한다. `uv sync`가 poetry.lock을 그대로 재현한다고 가정하지 않는다. [가상환경 공식 문서](https://docs.astral.sh/uv/pip/environments/)

### 5.7 셸 Python과 프로젝트 가상환경

가상환경을 활성화하지 않은 상태의 `python`은 pyenv shim이 현재 디렉터리의 버전 선언을 기준으로 선택한다. `pyenv shell <PYTHON_VERSION>`은 해당 셸에서 local/global보다 우선하며 `pyenv shell --unset`으로 해제한다.

프로젝트 의존성과 함께 작업할 때는 `uv run python`을 사용하거나 다음과 같이 가상환경을 활성화한다.

```sh
source .venv/bin/activate
```

끝나면 `deactivate`한다. 활성 `.venv`는 PATH에서 pyenv보다 앞설 수 있다. 그 상태에서 `pyenv local`만 바꿔도 기존 가상환경의 인터프리터가 교체되지는 않는다. Python 변경 시 프로젝트 환경을 새로 구성해야 한다.

`uv python install`, `uv python pin --global`, `uv python install --default`는 이 조합의 기본 단계에서 제외한다. 전역 Python은 pyenv가 관리하고 uv가 별도 전역 링크를 만들지 않게 한다.

### 5.8 전역 Python CLI

전역 도구는 기본 pyenv Python을 선택한 프로젝트 밖 셸에서 설치한다.

```sh
uv tool install --python "$(pyenv which python)" poetry
uv tool install --python "$(pyenv which python)" ipython
uv tool install --python "$(pyenv which python)" pygments
```

필요한 항목만 선택한다. 각 도구는 별도 환경을 갖고, 프로젝트 라이브러리를 써야 하는 IPython·Jupyter는 프로젝트 의존성으로 둔다. `uv tool upgrade --all`은 도구 패키지 업데이트이며 pyenv 기본값 변경이 기존 도구의 Python을 자동 교체하지는 않는다. 도구 인터프리터를 바꿀 때는 공식 tool 명령의 `--python` 지정으로 환경을 다시 구성한다. [uv 전역 도구 공식 안내](https://docs.astral.sh/uv/guides/tools/)

### 5.9 업데이트와 보관

- 관리자: Homebrew pyenv는 `brew upgrade pyenv`, 독립 uv는 `uv self update`.
- Python: 새로운 정식 버전을 pyenv에 추가한 뒤 global 또는 프로젝트 local을 선택한다.
- 프로젝트: Python 변경에 필요한 가상환경·의존성·잠금 변경은 별도 작업이다.
- 보관: 기존 인터프리터를 참조하는 uv tool 환경·프로젝트 `.venv`가 남아 있을 수 있으므로 옛 버전 삭제는 자동화하지 않는다.
- `uv python upgrade`는 uv 관리 Python용이며 pyenv 설치본 업데이트에 쓰지 않는다.

## 6. Zsh 초기화 배치

Fish를 추가 설치하는 후속 요청은 [12 문서](12-fish-posh-herdr-aside-paseo.md)에 반영했다. 아래는 Zsh용이며 Fish에 그대로 복사하지 않는다. pyenv는 Fish 네이티브 초기화를 쓰고 nvm·SDKMAN은 Zsh 개발 프로필 또는 명시된 선택적 연결 방식을 따른다.

다음은 새 Mac 설정 파일에 반영할 예시다. 설치자가 이미 넣은 동일 블록은 다시 넣지 않는다. 기존 Mac의 실제 설정은 변경하지 않았다.

### ~/.zprofile

```sh
eval "$(/opt/homebrew/bin/brew shellenv)"
```

### ~/.zshrc

일반 PATH 설정을 먼저 두고 nvm·SDKMAN 초기화를 나중에 둔다. SDKMAN 초기화는 파일 끝에 배치한다.

```sh
export PATH="$HOME/.local/bin:$PATH"

export PYENV_ROOT="$HOME/.pyenv"
[[ -d "$PYENV_ROOT/bin" ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - zsh)"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

export SDKMAN_DIR="$HOME/.sdkman"
[[ -s "$SDKMAN_DIR/bin/sdkman-init.sh" ]] && source "$SDKMAN_DIR/bin/sdkman-init.sh"
```

pyenv shim 초기화는 위처럼 한 번 적용하고 uv에는 별도 shim 초기화를 추가하지 않는다. uv 설치자가 사용자 bin 경로를 이미 처리했다면 첫 PATH 행도 중복하지 않는다. 이 블록 뒤에서 Homebrew shellenv나 Hermes bin 경로를 다시 앞에 추가하지 않는다.

## 7. IDE·AI CLI·MCP 연결

| 소비자 | 적용 방식 |
| --- | --- |
| IntelliJ·Android Studio | SDKMAN JDK의 실제 Identifier 디렉터리를 Project SDK·Gradle JVM에 연결 |
| VS Code Python | 프로젝트 `.venv/bin/python` 선택 |
| VS Code·Node 기반 도구 | nvm으로 선택한 Node를 사용; GUI가 대화형 Zsh를 읽는다고 가정하지 않음 |
| npm 설치 Codex·Mermaid 등 | 기본 nvm Node에 설치; Node 버전 변경 시 필요한 전역 CLI 재설치 |
| MCP의 Node 서버 | 호스트가 상속한 Node 경로 또는 명시적 nvm 런처를 사용하도록 구성 |
| MCP의 Python 서버 | `uv`·`uvx` 위치와 pyenv Python 실제 경로 지정; GUI의 pyenv 셸 초기화 상속을 가정하지 않음 |

MCP의 `command`에 셸 함수인 `nvm`을 실행 파일처럼 적지 않는다. 비대화형 호스트는 `.zshrc`를 자동 읽지 않을 수 있다. 필요하면 별도 셸 런처에서 nvm을 초기화한 뒤 실제 Node 명령을 실행하도록 구성하되 이 문서에서는 런처를 만들거나 실행하지 않는다. 특정 Node 버전의 절대경로를 직접 등록하면 업데이트 시 MCP 설정도 함께 수정해야 한다. uv tool 명령은 사용자 설정을 읽으므로 프로젝트 uv 설정만으로 MCP 도구 환경을 제어한다고 가정하지 않는다.

## 8. 향후 설치 체크리스트

- [ ] 새 Mac에 SDKMAN·nvm 공식 배포·Homebrew pyenv·uv 독립 배포를 설치한다.
- [ ] 최신 정식 JDK Identifier·Node 릴리스·CPython 버전을 선택한다.
- [ ] Zsh 초기화를 정리하고 예전 prefix·Conda·Hermes 링크를 복원에서 제외하고 최신 pyenv shims를 초기화한다.
- [ ] `.sdkmanrc`·`.nvmrc`·`.python-version`과 프로젝트 잠금 파일을 보관한다.
- [ ] 프로젝트별 환경·필요한 전역 CLI·IDE·MCP 경로를 구성한다.

이 체크리스트는 설치 계획이며 이번에 실행한 확인·테스트 항목이 아니다. 실제 새 Mac의 버전·장치 권한·프로젝트 호환성·실행 결과는 미확인이다.

## 9. 공식 자료 열람 기록

설치·버전 전환·프로젝트 구성·업데이트에 관한 아래 자료를 실제 열람했다. 문서의 예제 버전은 최신 숫자 보장의 근거로 사용하지 않았다.

| 출처 | 사용한 내용 |
| --- | --- |
| [pyenv 설치](https://github.com/pyenv/pyenv) | macOS Homebrew·Zsh shims |
| [pyenv 명령](https://github.com/pyenv/pyenv/blob/master/COMMANDS.md) | install·global·local·shell·which |
| [pyenv 빌드 환경](https://github.com/pyenv/pyenv/wiki#suggested-build-environment) | macOS 빌드 의존성 |
| [SDKMAN 설치](https://sdkman.io/install/) | macOS·Zsh 설치 및 초기화 |
| [SDKMAN 사용법](https://sdkman.io/usage/) | Identifier·default/use·env·설정·업데이트 |
| [nvm 공식 README](https://github.com/nvm-sh/nvm) | 설치자·Node 별칭·nvmrc·전역 패키지·prefix 충돌 |
| [Node 릴리스](https://nodejs.org/en/about/previous-releases) | 최신 정식과 LTS 구분 |
| [uv 설치](https://docs.astral.sh/uv/getting-started/installation/) | 독립 설치 및 self update |
| [uv Python 설치](https://docs.astral.sh/uv/guides/install-python/) | pyenv 병용 시 제외할 managed Python 설치 기능 |
| [uv Python 버전](https://docs.astral.sh/uv/concepts/python-versions/) | global pin·탐색·patch 업데이트 |
| [uv 설정 파일](https://docs.astral.sh/uv/concepts/configuration-files/) | 사용자 경로·설정 우선순위 |
| [uv 설정 참조](https://docs.astral.sh/uv/reference/settings/#python-preference) | only-system·python-downloads |
| [uv 명령 참조](https://docs.astral.sh/uv/reference/cli/#uv-python-install) | 설치 대상 결정·내장 다운로드 목록 |
| [uv 프로젝트](https://docs.astral.sh/uv/guides/projects/) | init·sync·lock |
| [uv 가상환경](https://docs.astral.sh/uv/pip/environments/) | venv·활성화·pip 인터페이스 |
| [uv 전역 도구](https://docs.astral.sh/uv/guides/tools/) | tool install·upgrade·환경 분리 |

`sdkman.io/usage/configuration/`와 `/usage/config/`는 읽을 수 있는 본문을 얻지 못했으므로 근거로 사용하지 않았다. 설정 설명은 실제 열람에 성공한 `/usage/`의 Configuration 절을 기준으로 했다.
