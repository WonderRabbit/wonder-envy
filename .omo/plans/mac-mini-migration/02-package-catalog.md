# Homebrew 전체 패키지 이전 목록

후속 확정된 런타임 정책은 [SDKMAN·nvm·pyenv·uv 설치 계획](11-runtime-managers.md)을 우선한다. 아래 Homebrew Node·Python·JDK·pyenv-virtualenv 절은 기존 설치 카탈로그이며 그대로 모두 재설치하라는 뜻이 아니다. 기본 Java는 SDKMAN, Node는 nvm, Python은 pyenv와 uv로 구성한다.

새 Mac의 실제 설치 경로와 지원 종료·이름 변경 여부는 [최신 공식 출처와 설치 예외](09-official-sources.md)를 우선한다. 아래 전체 목록은 기존 Mac의 설치 영수증 기록이며 Gemini CLI·Alacritty의 최신 공식 API 예외를 별도로 반영했다.

관측일: 2026-09-06. Formula 203종과 Caskroom 13개 디렉터리를 전부 기록했다. `docker`와 `docker-desktop`은 같은 앱의 중복 설치 흔적이므로 새 Mac에서는 하나만 설치한다. 모든 명령은 사용자가 새 Mac mini에서 실행할 절차이며 이 조사에서는 실행하지 않았다.

기존 버전은 관측 기록이다. 기본 정책은 최신 안정 버전 설치이며 같은 버전 재현은 요구하지 않는다. 프로젝트가 특정 Python/JDK 버전을 명시할 때에만 해당 버전 패키지를 별도로 추가한다. 직접 설치 Formula 47종, 의존성 영수증이 존재하는 Formula 142종, 직접 요청 false만 있고 의존성 표지가 없는 Formula 14종이다. 복수 버전의 설치 사유가 다르면 한 버전이라도 의존성 표지가 있는 경우 의존성으로 묶었다.

공홈 URL은 로컬 formula 파일, 로컬 tap 정의, 업데이트를 끈 `brew info` 메타데이터에서 추출했다. 일반 항목의 공홈 웹페이지나 링크 유효성은 확인하지 않았다. Gemini CLI·Alacritty는 2026-09-06 공식 API를 추가로 열람했다. 나머지 설치 명령은 로컬 메타데이터를 토대로 적은 경로이며 최신 공식 조회의 예외를 함께 적용한다.

## 개발 언어와 빌드 도구

### 패키지 bun

- 관측 버전: `1.2.14`
- 설치 구분: 직접 설치; tap: `oven-sh/bun`
- 공홈: [공식 프로젝트](https://bun.sh/)
- URL 근거: `/opt/homebrew/Cellar/bun/1.2.14/.brew/bun.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/bun/1.2.14/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install oven-sh/bun/bun`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 node

- 관측 버전: `24.2.0`, `25.6.1`, `25.6.1_1`, `26.3.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://nodejs.org/)
- URL 근거: `/opt/homebrew/Cellar/node/26.3.0/.brew/node.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/node/24.2.0/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/node/25.6.1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/node/25.6.1_1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/node/26.3.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install node`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 ruby

- 관측 버전: `3.4.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.ruby-lang.org/)
- URL 근거: `/opt/homebrew/Cellar/ruby/3.4.1/.brew/ruby.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ruby/3.4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install ruby`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 rbenv

- 관측 버전: `1.3.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://rbenv.org)
- URL 근거: `/opt/homebrew/Cellar/rbenv/1.3.0/.brew/rbenv.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/rbenv/1.3.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install rbenv`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 pyenv

- 관측 버전: `2.5.3`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/pyenv/pyenv)
- URL 근거: `/opt/homebrew/Cellar/pyenv/2.5.3/.brew/pyenv.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pyenv/2.5.3/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install pyenv`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 pyenv-virtualenv

- 관측 버전: `1.2.4`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/pyenv/pyenv-virtualenv)
- URL 근거: `/opt/homebrew/Cellar/pyenv-virtualenv/1.2.4/.brew/pyenv-virtualenv.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pyenv-virtualenv/1.2.4/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install pyenv-virtualenv`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 python@3.9

- 관측 버전: `3.9.23`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.python.org/)
- URL 근거: `/opt/homebrew/Cellar/python@3.9/3.9.23/.brew/python@3.9.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/python@3.9/3.9.23/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install python`
- 이전 조건: 기본은 최신 Python(`brew install python`)이다. `brew install python@3.9`는 프로젝트의 명시적인 요구가 있고 제공되는 경우에만 사용하는 호환성 선택지다.

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 위 이전 조건을 적용한 뒤 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 gradle

- 관측 버전: `9.2.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gradle.org/)
- URL 근거: `/opt/homebrew/Cellar/gradle/9.2.1/.brew/gradle.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gradle/9.2.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install gradle`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 spring-boot

- 관측 버전: `3.5.5`
- 설치 구분: 직접 설치; tap: `spring-io/tap`
- 공홈: [공식 프로젝트](https://spring.io/projects/spring-boot)
- URL 근거: `/opt/homebrew/Cellar/spring-boot/3.5.5/.brew/spring-boot.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/spring-boot/3.5.5/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install spring-io/tap/spring-boot`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 mingw-w64

- 관측 버전: `14.0.0_1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://sourceforge.net/projects/mingw-w64/)
- URL 근거: `/opt/homebrew/Cellar/mingw-w64/14.0.0_1/.brew/mingw-w64.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mingw-w64/14.0.0_1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install mingw-w64`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 rustup

- 관측 버전: `1.29.0_2`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://rust-lang.github.io/rustup/)
- URL 근거: `/opt/homebrew/Cellar/rustup/1.29.0_2/.brew/rustup.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/rustup/1.29.0_2/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install rustup`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 libtensorflow

- 관측 버전: `2.18.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.tensorflow.org/)
- URL 근거: `/opt/homebrew/Cellar/libtensorflow/2.18.0/.brew/libtensorflow.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libtensorflow/2.18.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install libtensorflow`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

## 코드 편집과 개발 보조

### 패키지 ast-grep

- 관측 버전: `0.44.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://ast-grep.github.io/)
- URL 근거: `/opt/homebrew/Cellar/ast-grep/0.44.1/.brew/ast-grep.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ast-grep/0.44.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install ast-grep`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 biome

- 관측 버전: `2.5.4`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://biomejs.dev/)
- URL 근거: `/opt/homebrew/Cellar/biome/2.5.4/.brew/biome.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/biome/2.5.4/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install biome`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 gemini-cli

- 관측 버전: `0.46.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/google-gemini/gemini-cli)
- URL 근거: `/opt/homebrew/Cellar/gemini-cli/0.46.0/.brew/gemini-cli.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gemini-cli/0.46.0/INSTALL_RECEIPT.json`
- 최신 공식 상태: [Homebrew API](https://formulae.brew.sh/api/formula/gemini-cli.json)에 `deprecated: true`, `deprecation_reason: unsupported`, 대체 cask `antigravity-cli`가 기록되어 있다(2026-09-06 열람).
- 새 설치 경로: `brew install --cask antigravity-cli` (공식 API가 지목한 대체 제품이며 기존 Gemini CLI와 같은 도구로 간주하지 않음).

1. 기존 Gemini CLI 설정과 사용 목적을 보관하고 최신 기본 설치 목록에서는 제외한다.
2. [최신 공식 출처](09-official-sources.md)에서 대체 제품의 설치 안내를 확인한 뒤 필요한 경우 위 대체 설치 명령을 사용한다.
3. 계정과 설정을 대체 도구 방식으로 구성한다. Gemini CLI 설정의 자동 호환성은 확인되지 않았다.

### 패키지 gh

- 관측 버전: `2.94.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://cli.github.com/)
- URL 근거: `/opt/homebrew/Cellar/gh/2.94.0/.brew/gh.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gh/2.94.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install gh`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 jq

- 관측 버전: `1.7.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://jqlang.github.io/jq/)
- URL 근거: `/opt/homebrew/Cellar/jq/1.7.1/.brew/jq.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/jq/1.7.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install jq`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 kotlin-language-server

- 관측 버전: `1.3.13`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/fwcd/kotlin-language-server)
- URL 근거: `/opt/homebrew/Cellar/kotlin-language-server/1.3.13/.brew/kotlin-language-server.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/kotlin-language-server/1.3.13/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install kotlin-language-server`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 lazygit

- 관측 버전: `0.45.0`
- 설치 구분: 직접 설치; tap: `jesseduffield/lazygit`
- 공홈: [공식 프로젝트](https://github.com/jesseduffield/lazygit/)
- URL 근거: `/opt/homebrew/Cellar/lazygit/0.45.0/.brew/lazygit.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lazygit/0.45.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install jesseduffield/lazygit/lazygit`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 mdq

- 관측 버전: `0.10.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/yshavit/mdq)
- URL 근거: `/opt/homebrew/Cellar/mdq/0.10.0/.brew/mdq.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mdq/0.10.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install mdq`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 neovim

- 관측 버전: `0.11.2`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://neovim.io/)
- URL 근거: `/opt/homebrew/Cellar/neovim/0.11.2/.brew/neovim.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/neovim/0.11.2/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install neovim`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 yq

- 관측 버전: `4.47.2`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/mikefarah/yq)
- URL 근거: `/opt/homebrew/Cellar/yq/4.47.2/.brew/yq.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/yq/4.47.2/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install yq`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

## 터미널과 파일 작업

### 패키지 eza

- 관측 버전: `0.20.16`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/eza-community/eza)
- URL 근거: `/opt/homebrew/Cellar/eza/0.20.16/.brew/eza.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/eza/0.20.16/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install eza`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 fd

- 관측 버전: `10.2.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/sharkdp/fd)
- URL 근거: `/opt/homebrew/Cellar/fd/10.2.0/.brew/fd.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fd/10.2.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install fd`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 fish

- 관측 버전: `4.1.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://fishshell.com)
- URL 근거: `/opt/homebrew/Cellar/fish/4.1.1/.brew/fish.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fish/4.1.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install fish`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 fzf

- 관측 버전: `0.60.2`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/junegunn/fzf)
- URL 근거: `/opt/homebrew/Cellar/fzf/0.60.2/.brew/fzf.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fzf/0.60.2/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install fzf`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 lsd

- 관측 버전: `1.1.5`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/lsd-rs/lsd)
- URL 근거: `/opt/homebrew/Cellar/lsd/1.1.5/.brew/lsd.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lsd/1.1.5/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install lsd`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 ripgrep

- 관측 버전: `14.1.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/BurntSushi/ripgrep)
- URL 근거: `/opt/homebrew/Cellar/ripgrep/14.1.1/.brew/ripgrep.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ripgrep/14.1.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install ripgrep`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 stow

- 관측 버전: `2.4.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/stow/)
- URL 근거: `/opt/homebrew/Cellar/stow/2.4.1/.brew/stow.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/stow/2.4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install stow`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 기존 설치 기록 tmux — 이전 제외

- 관측 버전: `3.5a`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tmux.github.io/)
- URL 근거: `/opt/homebrew/Cellar/tmux/3.5a/.brew/tmux.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/tmux/3.5a/INSTALL_RECEIPT.json`
- 이전 결정: 사용자 요청에 따라 설치·설정 복원 제외. 대체 도구는 Herdr.

1. 기존 설치 사실만 기록으로 보존하며 새 Mac에는 tmux를 설치하지 않는다.
2. `.tmux.conf`, tmux 플러그인, 셸 자동 attach·자동 시작을 복원하지 않는다.
3. 세션·pane 운영은 Ghostty 안의 Herdr로 구성한다. 기존 tmux 세션·키 바인딩·플러그인이 Herdr로 자동 변환되는 것은 아니다.

### 패키지 tree

- 관측 버전: `2.2.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://oldmanprogrammer.net/source.php?dir=projects/tree)
- URL 근거: `/opt/homebrew/Cellar/tree/2.2.1/.brew/tree.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/tree/2.2.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install tree`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 yazi

- 관측 버전: `25.2.11`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/sxyazi/yazi)
- URL 근거: `/opt/homebrew/Cellar/yazi/25.2.11/.brew/yazi.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/yazi/25.2.11/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install yazi`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 zoxide

- 관측 버전: `0.9.7`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/ajeetdsouza/zoxide)
- URL 근거: `/opt/homebrew/Cellar/zoxide/0.9.7/.brew/zoxide.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/zoxide/0.9.7/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install zoxide`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 zsh-syntax-highlighting

- 관측 버전: `0.8.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/zsh-users/zsh-syntax-highlighting)
- URL 근거: `/opt/homebrew/Cellar/zsh-syntax-highlighting/0.8.0/.brew/zsh-syntax-highlighting.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/zsh-syntax-highlighting/0.8.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install zsh-syntax-highlighting`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

## 네트워크와 보안

### 패키지 age

- 관측 버전: `1.3.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/FiloSottile/age)
- URL 근거: `/opt/homebrew/Cellar/age/1.3.1/.brew/age.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/age/1.3.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install age`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 httpie

- 관측 버전: `3.2.4_4`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://httpie.io/)
- URL 근거: `/opt/homebrew/Cellar/httpie/3.2.4_4/.brew/httpie.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/httpie/3.2.4_4/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install httpie`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 mkcert

- 관측 버전: `1.4.4`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/FiloSottile/mkcert)
- URL 근거: `/opt/homebrew/Cellar/mkcert/1.4.4/.brew/mkcert.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mkcert/1.4.4/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install mkcert`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 sops

- 관측 버전: `3.11.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://getsops.io/)
- URL 근거: `/opt/homebrew/Cellar/sops/3.11.0/.brew/sops.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/sops/3.11.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install sops`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 telnet

- 관측 버전: `306`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://opensource.apple.com/)
- URL 근거: `/opt/homebrew/Cellar/telnet/306/.brew/telnet.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/telnet/306/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install telnet`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 wget

- 관측 버전: `1.25.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/wget/)
- URL 근거: `/opt/homebrew/Cellar/wget/1.25.0/.brew/wget.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/wget/1.25.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install wget`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

## 미디어와 문서 및 압축

### 패키지 ffmpeg

- 관측 버전: `8.0.1`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://ffmpeg.org/)
- URL 근거: `/opt/homebrew/Cellar/ffmpeg/8.0.1/.brew/ffmpeg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ffmpeg/8.0.1/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install ffmpeg`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 imagemagick

- 관측 버전: `7.1.1-47`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://imagemagick.org/index.php)
- URL 근거: `/opt/homebrew/Cellar/imagemagick/7.1.1-47/.brew/imagemagick.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/imagemagick/7.1.1-47/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install imagemagick`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 p7zip

- 관측 버전: `17.06`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/p7zip-project/p7zip)
- URL 근거: `/opt/homebrew/Cellar/p7zip/17.06/.brew/p7zip.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/p7zip/17.06/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install sevenzip`
- 이전 조건: 관측된 p7zip은 구형 구현이다. 새 Mac에서는 sevenzip을 우선 사용하고 p7zip은 기존 스크립트의 명시적 요구가 있을 때만 검토한다.

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 위 이전 조건을 적용한 뒤 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 sevenzip

- 관측 버전: `24.09`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://7-zip.org)
- URL 근거: `/opt/homebrew/Cellar/sevenzip/24.09/.brew/sevenzip.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/sevenzip/24.09/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install sevenzip`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 poppler

- 관측 버전: `25.06.0`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://poppler.freedesktop.org/)
- URL 근거: `/opt/homebrew/Cellar/poppler/25.06.0/.brew/poppler.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/poppler/25.06.0/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install poppler`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 wimlib

- 관측 버전: `1.14.5`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://wimlib.net/)
- URL 근거: `/opt/homebrew/Cellar/wimlib/1.14.5/.brew/wimlib.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/wimlib/1.14.5/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install wimlib`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

### 패키지 yt-dlp

- 관측 버전: `2025.12.8`
- 설치 구분: 직접 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/yt-dlp/yt-dlp)
- URL 근거: `/opt/homebrew/Cellar/yt-dlp/2025.12.8/.brew/yt-dlp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/yt-dlp/2025.12.8/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install yt-dlp`

1. 이 도구를 사용하는 프로젝트와 별도 설정 파일의 이전 필요성을 정리한다.
2. 새 Mac의 Homebrew 준비 후 위 명령으로 최신 안정판을 설치한다.
3. 사용 중인 설정·플러그인만 옮기고 이전 Mac의 Cellar 바이너리는 복사하지 않는다.

## 상위 도구가 복원하는 의존성과 비직접 패키지

### 패키지 ada-url

- 관측 버전: `3.4.4`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/ada-url/ada)
- URL 근거: `/opt/homebrew/Cellar/ada-url/3.4.4/.brew/ada-url.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ada-url/3.4.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install ada-url`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 aom

- 관측 버전: `3.13.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://aomedia.googlesource.com/aom)
- URL 근거: `/opt/homebrew/Cellar/aom/3.13.1/.brew/aom.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/aom/3.13.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install aom`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 aribb24

- 관측 버전: `1.0.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://code.videolan.org/jeeb/aribb24)
- URL 근거: `/opt/homebrew/Cellar/aribb24/1.0.4/.brew/aribb24.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/aribb24/1.0.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install aribb24`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 autoconf

- 관측 버전: `2.72`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/autoconf/)
- URL 근거: `/opt/homebrew/Cellar/autoconf/2.72/.brew/autoconf.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/autoconf/2.72/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install autoconf`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 brotli

- 관측 버전: `1.2.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/google/brotli)
- URL 근거: `/opt/homebrew/Cellar/brotli/1.2.0/.brew/brotli.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/brotli/1.2.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install brotli`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 c-ares

- 관측 버전: `1.34.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://c-ares.org/)
- URL 근거: `/opt/homebrew/Cellar/c-ares/1.34.6/.brew/c-ares.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/c-ares/1.34.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install c-ares`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 ca-certificates

- 관측 버전: `2026-05-14`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://curl.se/docs/caextract.html)
- URL 근거: `/opt/homebrew/Cellar/ca-certificates/2026-05-14/.brew/ca-certificates.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ca-certificates/2026-05-14/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install ca-certificates`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 cairo

- 관측 버전: `1.18.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://cairographics.org/)
- URL 근거: `/opt/homebrew/Cellar/cairo/1.18.4/.brew/cairo.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/cairo/1.18.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install cairo`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 certifi

- 관측 버전: `2025.11.12`, `2025.8.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/certifi/python-certifi)
- URL 근거: `/opt/homebrew/Cellar/certifi/2025.8.3/.brew/certifi.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/certifi/2025.11.12/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/certifi/2025.8.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install certifi`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 cjson

- 관측 버전: `1.7.19`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/DaveGamble/cJSON)
- URL 근거: `/opt/homebrew/Cellar/cjson/1.7.19/.brew/cjson.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/cjson/1.7.19/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install cjson`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 coreutils

- 관측 버전: `9.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/coreutils/)
- URL 근거: `/opt/homebrew/Cellar/coreutils/9.6/.brew/coreutils.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/coreutils/9.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install coreutils`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 dav1d

- 관측 버전: `1.5.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://code.videolan.org/videolan/dav1d)
- URL 근거: `/opt/homebrew/Cellar/dav1d/1.5.2/.brew/dav1d.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/dav1d/1.5.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install dav1d`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 deno

- 관측 버전: `2.6.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://deno.com/)
- URL 근거: `/opt/homebrew/Cellar/deno/2.6.3/.brew/deno.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/deno/2.6.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install deno`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 flac

- 관측 버전: `1.5.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://xiph.org/flac/)
- URL 근거: `/opt/homebrew/Cellar/flac/1.5.0/.brew/flac.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/flac/1.5.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install flac`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 fmt

- 관측 버전: `12.1.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://fmt.dev/)
- URL 근거: `/opt/homebrew/Cellar/fmt/12.1.0/.brew/fmt.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fmt/12.1.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install fmt`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 fontconfig

- 관측 버전: `2.17.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://wiki.freedesktop.org/www/Software/fontconfig/)
- URL 근거: `/opt/homebrew/Cellar/fontconfig/2.17.1/.brew/fontconfig.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fontconfig/2.17.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install fontconfig`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 freetype

- 관측 버전: `2.14.1_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.freetype.org/)
- URL 근거: `/opt/homebrew/Cellar/freetype/2.14.1_1/.brew/freetype.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/freetype/2.14.1_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install freetype`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 frei0r

- 관측 버전: `2.5.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://frei0r.dyne.org/)
- URL 근거: `/opt/homebrew/Cellar/frei0r/2.5.0/.brew/frei0r.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/frei0r/2.5.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install frei0r`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 fribidi

- 관측 버전: `1.0.16`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/fribidi/fribidi)
- URL 근거: `/opt/homebrew/Cellar/fribidi/1.0.16/.brew/fribidi.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/fribidi/1.0.16/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install fribidi`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gdbm

- 관측 버전: `1.24`, `1.25`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org.ua/software/gdbm/)
- URL 근거: `/opt/homebrew/Cellar/gdbm/1.25/.brew/gdbm.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gdbm/1.24/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/gdbm/1.25/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gdbm`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gettext

- 관측 버전: `0.26_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/gettext/)
- URL 근거: `/opt/homebrew/Cellar/gettext/0.26_1/.brew/gettext.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gettext/0.26_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gettext`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 giflib

- 관측 버전: `5.2.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://giflib.sourceforge.net/)
- URL 근거: `/opt/homebrew/Cellar/giflib/5.2.2/.brew/giflib.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/giflib/5.2.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install giflib`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 glib

- 관측 버전: `2.86.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://docs.gtk.org/glib/)
- URL 근거: `/opt/homebrew/Cellar/glib/2.86.2/.brew/glib.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/glib/2.86.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install glib`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gmp

- 관측 버전: `6.3.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gmplib.org/)
- URL 근거: `/opt/homebrew/Cellar/gmp/6.3.0/.brew/gmp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gmp/6.3.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gmp`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gnupg

- 관측 버전: `2.4.8`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gnupg.org/)
- URL 근거: `/opt/homebrew/Cellar/gnupg/2.4.8/.brew/gnupg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gnupg/2.4.8/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gnupg`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gnutls

- 관측 버전: `3.8.11`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gnutls.org/)
- URL 근거: `/opt/homebrew/Cellar/gnutls/3.8.11/.brew/gnutls.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gnutls/3.8.11/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gnutls`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gpgme

- 관측 버전: `1.24.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnupg.org/related_software/gpgme/)
- URL 근거: `/opt/homebrew/Cellar/gpgme/1.24.3/.brew/gpgme.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gpgme/1.24.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gpgme`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 gradle-completion

- 관측 버전: `9.2.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gradle.org/)
- URL 근거: `/opt/homebrew/Cellar/gradle-completion/9.2.0/.brew/gradle-completion.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/gradle-completion/9.2.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install gradle-completion`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 graphite2

- 관측 버전: `1.3.14`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://graphite.sil.org/)
- URL 근거: `/opt/homebrew/Cellar/graphite2/1.3.14/.brew/graphite2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/graphite2/1.3.14/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install graphite2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 harfbuzz

- 관측 버전: `12.2.0_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/harfbuzz/harfbuzz)
- URL 근거: `/opt/homebrew/Cellar/harfbuzz/12.2.0_1/.brew/harfbuzz.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/harfbuzz/12.2.0_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install harfbuzz`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 hdrhistogram_c

- 관측 버전: `0.11.9`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/HdrHistogram/HdrHistogram_c)
- URL 근거: `/opt/homebrew/Cellar/hdrhistogram_c/0.11.9/.brew/hdrhistogram_c.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/hdrhistogram_c/0.11.9/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install hdrhistogram_c`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 highway

- 관측 버전: `1.3.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/google/highway)
- URL 근거: `/opt/homebrew/Cellar/highway/1.3.0/.brew/highway.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/highway/1.3.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install highway`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 icu4c@78

- 관측 버전: `78.3`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://icu.unicode.org/home)
- URL 근거: `/opt/homebrew/Cellar/icu4c@78/78.3/.brew/icu4c@78.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/icu4c@78/78.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install icu4c@78`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 imath

- 관측 버전: `3.2.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://imath.readthedocs.io/en/latest/)
- URL 근거: `/opt/homebrew/Cellar/imath/3.2.2/.brew/imath.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/imath/3.2.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install imath`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 isl

- 관측 버전: `0.27`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libisl.sourceforge.io/)
- URL 근거: `/opt/homebrew/Cellar/isl/0.27/.brew/isl.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/isl/0.27/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install isl`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 jasper

- 관측 버전: `4.2.4`, `4.2.5`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://ece.engr.uvic.ca/~frodo/jasper/)
- URL 근거: `/opt/homebrew/Cellar/jasper/4.2.5/.brew/jasper.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/jasper/4.2.4/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/jasper/4.2.5/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install jasper`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 jpeg-turbo

- 관측 버전: `3.1.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libjpeg-turbo.org/)
- URL 근거: `/opt/homebrew/Cellar/jpeg-turbo/3.1.3/.brew/jpeg-turbo.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/jpeg-turbo/3.1.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install jpeg-turbo`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 jpeg-xl

- 관측 버전: `0.11.1_3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://jpeg.org/jpegxl/index.html)
- URL 근거: `/opt/homebrew/Cellar/jpeg-xl/0.11.1_3/.brew/jpeg-xl.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/jpeg-xl/0.11.1_3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install jpeg-xl`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 lame

- 관측 버전: `3.100`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://lame.sourceforge.io/)
- URL 근거: `/opt/homebrew/Cellar/lame/3.100/.brew/lame.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lame/3.100/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install lame`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 leptonica

- 관측 버전: `1.86.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](http://www.leptonica.org/)
- URL 근거: `/opt/homebrew/Cellar/leptonica/1.86.0/.brew/leptonica.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/leptonica/1.86.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install leptonica`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libarchive

- 관측 버전: `3.8.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libarchive.org)
- URL 근거: `/opt/homebrew/Cellar/libarchive/3.8.3/.brew/libarchive.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libarchive/3.8.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libarchive`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libass

- 관측 버전: `0.17.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/libass/libass)
- URL 근거: `/opt/homebrew/Cellar/libass/0.17.4/.brew/libass.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libass/0.17.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libass`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libassuan

- 관측 버전: `3.0.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnupg.org/related_software/libassuan/)
- URL 근거: `/opt/homebrew/Cellar/libassuan/3.0.2/.brew/libassuan.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libassuan/3.0.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libassuan`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libb2

- 관측 버전: `0.98.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://blake2.net/)
- URL 근거: `/opt/homebrew/Cellar/libb2/0.98.1/.brew/libb2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libb2/0.98.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libb2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libbluray

- 관측 버전: `1.4.0_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.videolan.org/developers/libbluray.html)
- URL 근거: `/opt/homebrew/Cellar/libbluray/1.4.0_1/.brew/libbluray.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libbluray/1.4.0_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libbluray`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libde265

- 관측 버전: `1.0.15`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/strukturag/libde265)
- URL 근거: `/opt/homebrew/Cellar/libde265/1.0.15/.brew/libde265.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libde265/1.0.15/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libde265`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libdeflate

- 관측 버전: `1.25`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/ebiggers/libdeflate)
- URL 근거: `/opt/homebrew/Cellar/libdeflate/1.25/.brew/libdeflate.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libdeflate/1.25/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libdeflate`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libevent

- 관측 버전: `2.1.12_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libevent.org/)
- URL 근거: `/opt/homebrew/Cellar/libevent/2.1.12_1/.brew/libevent.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libevent/2.1.12_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libevent`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libffi

- 관측 버전: `3.5.2`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://sourceware.org/libffi/)
- URL 근거: `/opt/homebrew/Cellar/libffi/3.5.2/.brew/libffi.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libffi/3.5.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libffi`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libgcrypt

- 관측 버전: `1.11.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gnupg.org/related_software/libgcrypt/)
- URL 근거: `/opt/homebrew/Cellar/libgcrypt/1.11.1/.brew/libgcrypt.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libgcrypt/1.11.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libgcrypt`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libgit2

- 관측 버전: `1.9.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libgit2.github.com/)
- URL 근거: `/opt/homebrew/Cellar/libgit2/1.9.0/.brew/libgit2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libgit2/1.9.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libgit2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libgpg-error

- 관측 버전: `1.55`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnupg.org/related_software/libgpg-error/)
- URL 근거: `/opt/homebrew/Cellar/libgpg-error/1.55/.brew/libgpg-error.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libgpg-error/1.55/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libgpg-error`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libheif

- 관측 버전: `1.19.5_1`, `1.19.8`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libde265.org/)
- URL 근거: `/opt/homebrew/Cellar/libheif/1.19.8/.brew/libheif.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libheif/1.19.5_1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/libheif/1.19.8/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libheif`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libidn2

- 관측 버전: `2.3.8`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/libidn/#libidn2)
- URL 근거: `/opt/homebrew/Cellar/libidn2/2.3.8/.brew/libidn2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libidn2/2.3.8/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libidn2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libksba

- 관측 버전: `1.6.7`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnupg.org/related_software/libksba/)
- URL 근거: `/opt/homebrew/Cellar/libksba/1.6.7/.brew/libksba.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libksba/1.6.7/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libksba`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 liblqr

- 관측 버전: `0.4.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://liblqr.wikidot.com/)
- URL 근거: `/opt/homebrew/Cellar/liblqr/0.4.3/.brew/liblqr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/liblqr/0.4.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install liblqr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libmicrohttpd

- 관측 버전: `1.0.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/libmicrohttpd/)
- URL 근거: `/opt/homebrew/Cellar/libmicrohttpd/1.0.2/.brew/libmicrohttpd.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libmicrohttpd/1.0.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libmicrohttpd`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libmpc

- 관측 버전: `1.4.1`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.multiprecision.org/)
- URL 근거: `/opt/homebrew/Cellar/libmpc/1.4.1/.brew/libmpc.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libmpc/1.4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libmpc`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libnghttp2

- 관측 버전: `1.69.0`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://nghttp2.org/)
- URL 근거: `/opt/homebrew/Cellar/libnghttp2/1.69.0/.brew/libnghttp2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libnghttp2/1.69.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libnghttp2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libnghttp3

- 관측 버전: `1.15.0`, `1.16.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://nghttp2.org/nghttp3/)
- URL 근거: `/opt/homebrew/Cellar/libnghttp3/1.16.0/.brew/libnghttp3.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libnghttp3/1.15.0/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/libnghttp3/1.16.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libnghttp3`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libngtcp2

- 관측 버전: `1.20.0`, `1.23.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://nghttp2.org/ngtcp2/)
- URL 근거: `/opt/homebrew/Cellar/libngtcp2/1.23.0/.brew/libngtcp2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libngtcp2/1.20.0/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/libngtcp2/1.23.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libngtcp2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libogg

- 관측 버전: `1.3.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.xiph.org/ogg/)
- URL 근거: `/opt/homebrew/Cellar/libogg/1.3.6/.brew/libogg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libogg/1.3.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libogg`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libomp

- 관측 버전: `19.1.7`, `20.1.7`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://openmp.llvm.org/)
- URL 근거: `/opt/homebrew/Cellar/libomp/20.1.7/.brew/libomp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libomp/19.1.7/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/libomp/20.1.7/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libomp`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libpng

- 관측 버전: `1.6.51`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](http://www.libpng.org/pub/png/libpng.html)
- URL 근거: `/opt/homebrew/Cellar/libpng/1.6.51/.brew/libpng.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libpng/1.6.51/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libpng`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libraw

- 관측 버전: `0.21.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libraw.org/)
- URL 근거: `/opt/homebrew/Cellar/libraw/0.21.4/.brew/libraw.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libraw/0.21.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libraw`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 librist

- 관측 버전: `0.2.11`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://code.videolan.org/rist/)
- URL 근거: `/opt/homebrew/Cellar/librist/0.2.11/.brew/librist.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/librist/0.2.11/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install librist`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libsamplerate

- 관측 버전: `0.2.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/libsndfile/libsamplerate)
- URL 근거: `/opt/homebrew/Cellar/libsamplerate/0.2.2/.brew/libsamplerate.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libsamplerate/0.2.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libsamplerate`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libsndfile

- 관측 버전: `1.2.2_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libsndfile.github.io/libsndfile/)
- URL 근거: `/opt/homebrew/Cellar/libsndfile/1.2.2_1/.brew/libsndfile.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libsndfile/1.2.2_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libsndfile`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libsodium

- 관측 버전: `1.0.20`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libsodium.org/)
- URL 근거: `/opt/homebrew/Cellar/libsodium/1.0.20/.brew/libsodium.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libsodium/1.0.20/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libsodium`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libsoxr

- 관측 버전: `0.1.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://sourceforge.net/projects/soxr/)
- URL 근거: `/opt/homebrew/Cellar/libsoxr/0.1.3/.brew/libsoxr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libsoxr/0.1.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libsoxr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libssh

- 관측 버전: `0.11.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libssh.org/)
- URL 근거: `/opt/homebrew/Cellar/libssh/0.11.3/.brew/libssh.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libssh/0.11.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libssh`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libssh2

- 관측 버전: `1.11.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libssh2.org/)
- URL 근거: `/opt/homebrew/Cellar/libssh2/1.11.1/.brew/libssh2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libssh2/1.11.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libssh2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libtasn1

- 관측 버전: `4.20.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/libtasn1/)
- URL 근거: `/opt/homebrew/Cellar/libtasn1/4.20.0/.brew/libtasn1.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libtasn1/4.20.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libtasn1`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libtiff

- 관측 버전: `4.7.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libtiff.gitlab.io/libtiff/)
- URL 근거: `/opt/homebrew/Cellar/libtiff/4.7.1/.brew/libtiff.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libtiff/4.7.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libtiff`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libtool

- 관측 버전: `2.5.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/libtool/)
- URL 근거: `/opt/homebrew/Cellar/libtool/2.5.4/.brew/libtool.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libtool/2.5.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libtool`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libudfread

- 관측 버전: `1.2.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://code.videolan.org/videolan/libudfread)
- URL 근거: `/opt/homebrew/Cellar/libudfread/1.2.0/.brew/libudfread.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libudfread/1.2.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libudfread`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libunibreak

- 관측 버전: `6.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/adah1972/libunibreak)
- URL 근거: `/opt/homebrew/Cellar/libunibreak/6.1/.brew/libunibreak.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libunibreak/6.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libunibreak`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libunistring

- 관측 버전: `1.4.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/libunistring/)
- URL 근거: `/opt/homebrew/Cellar/libunistring/1.4.1/.brew/libunistring.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libunistring/1.4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libunistring`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libusb

- 관측 버전: `1.0.29`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libusb.info/)
- URL 근거: `/opt/homebrew/Cellar/libusb/1.0.29/.brew/libusb.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libusb/1.0.29/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libusb`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libuv

- 관측 버전: `1.52.1`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://libuv.org/)
- URL 근거: `/opt/homebrew/Cellar/libuv/1.52.1/.brew/libuv.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libuv/1.52.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libuv`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libvidstab

- 관측 버전: `1.1.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](http://public.hronopik.de/vid.stab/)
- URL 근거: `/opt/homebrew/Cellar/libvidstab/1.1.1/.brew/libvidstab.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libvidstab/1.1.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libvidstab`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libvmaf

- 관측 버전: `3.0.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/Netflix/vmaf)
- URL 근거: `/opt/homebrew/Cellar/libvmaf/3.0.0/.brew/libvmaf.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libvmaf/3.0.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libvmaf`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libvorbis

- 관측 버전: `1.3.7`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://xiph.org/vorbis/)
- URL 근거: `/opt/homebrew/Cellar/libvorbis/1.3.7/.brew/libvorbis.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libvorbis/1.3.7/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libvorbis`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libvpx

- 관측 버전: `1.15.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.webmproject.org/code/)
- URL 근거: `/opt/homebrew/Cellar/libvpx/1.15.2/.brew/libvpx.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libvpx/1.15.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libvpx`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libx11

- 관측 버전: `1.8.12`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libx11/1.8.12/.brew/libx11.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libx11/1.8.12/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libx11`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libxau

- 관측 버전: `1.0.12`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libxau/1.0.12/.brew/libxau.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libxau/1.0.12/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libxau`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libxcb

- 관측 버전: `1.17.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libxcb/1.17.0/.brew/libxcb.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libxcb/1.17.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libxcb`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libxdmcp

- 관측 버전: `1.1.5`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libxdmcp/1.1.5/.brew/libxdmcp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libxdmcp/1.1.5/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libxdmcp`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libxext

- 관측 버전: `1.3.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libxext/1.3.6/.brew/libxext.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libxext/1.3.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libxext`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libxrender

- 관측 버전: `0.9.12`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/libxrender/0.9.12/.brew/libxrender.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libxrender/0.9.12/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libxrender`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 libyaml

- 관측 버전: `0.2.5`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/yaml/libyaml)
- URL 근거: `/opt/homebrew/Cellar/libyaml/0.2.5/.brew/libyaml.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/libyaml/0.2.5/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install libyaml`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 little-cms2

- 관측 버전: `2.17`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.littlecms.com/)
- URL 근거: `/opt/homebrew/Cellar/little-cms2/2.17/.brew/little-cms2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/little-cms2/2.17/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install little-cms2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 llhttp

- 관측 버전: `9.3.1`, `9.4.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://llhttp.org/)
- URL 근거: `/opt/homebrew/Cellar/llhttp/9.4.1/.brew/llhttp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/llhttp/9.3.1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/llhttp/9.4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install llhttp`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 lpeg

- 관측 버전: `1.1.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.inf.puc-rio.br/~roberto/lpeg/)
- URL 근거: `/opt/homebrew/Cellar/lpeg/1.1.0/.brew/lpeg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lpeg/1.1.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install lpeg`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 luajit

- 관측 버전: `2.1.1734355927`, `2.1.1748459687`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://luajit.org/luajit.html)
- URL 근거: `/opt/homebrew/Cellar/luajit/2.1.1748459687/.brew/luajit.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/luajit/2.1.1734355927/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/luajit/2.1.1748459687/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install luajit`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 luv

- 관측 버전: `1.51.0-1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/luvit/luv)
- URL 근거: `/opt/homebrew/Cellar/luv/1.51.0-1/.brew/luv.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/luv/1.51.0-1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install luv`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 lz4

- 관측 버전: `1.10.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://lz4.github.io/lz4/)
- URL 근거: `/opt/homebrew/Cellar/lz4/1.10.0/.brew/lz4.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lz4/1.10.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install lz4`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 lzo

- 관측 버전: `2.10`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.oberhumer.com/opensource/lzo/)
- URL 근거: `/opt/homebrew/Cellar/lzo/2.10/.brew/lzo.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/lzo/2.10/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install lzo`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 m4

- 관측 버전: `1.4.19`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnu.org/software/m4)
- URL 근거: `/opt/homebrew/Cellar/m4/1.4.19/.brew/m4.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/m4/1.4.19/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install m4`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 mbedtls

- 관측 버전: `3.6.2`, `3.6.3.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tls.mbed.org/)
- URL 근거: `/opt/homebrew/Cellar/mbedtls/3.6.3.1/.brew/mbedtls.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mbedtls/3.6.2/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/mbedtls/3.6.3.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install mbedtls`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 merve

- 관측 버전: `1.2.2_1`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/nodejs/merve)
- URL 근거: `/opt/homebrew/Cellar/merve/1.2.2_1/.brew/merve.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/merve/1.2.2_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install merve`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 mpdecimal

- 관측 버전: `4.0.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.bytereef.org/mpdecimal/)
- URL 근거: `/opt/homebrew/Cellar/mpdecimal/4.0.1/.brew/mpdecimal.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mpdecimal/4.0.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install mpdecimal`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 mpfr

- 관측 버전: `4.2.2`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.mpfr.org/)
- URL 근거: `/opt/homebrew/Cellar/mpfr/4.2.2/.brew/mpfr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mpfr/4.2.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install mpfr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 mpg123

- 관측 버전: `1.33.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.mpg123.de/)
- URL 근거: `/opt/homebrew/Cellar/mpg123/1.33.3/.brew/mpg123.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/mpg123/1.33.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install mpg123`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 nbytes

- 관측 버전: `0.1.4`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/nodejs/nbytes)
- URL 근거: `/opt/homebrew/Cellar/nbytes/0.1.4/.brew/nbytes.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/nbytes/0.1.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install nbytes`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 ncurses

- 관측 버전: `6.5`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://invisible-island.net/ncurses/announce.html)
- URL 근거: `/opt/homebrew/Cellar/ncurses/6.5/.brew/ncurses.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ncurses/6.5/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install ncurses`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 nettle

- 관측 버전: `3.10.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.lysator.liu.se/~nisse/nettle/)
- URL 근거: `/opt/homebrew/Cellar/nettle/3.10.2/.brew/nettle.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/nettle/3.10.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install nettle`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 npth

- 관측 버전: `1.8`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gnupg.org/)
- URL 근거: `/opt/homebrew/Cellar/npth/1.8/.brew/npth.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/npth/1.8/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install npth`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 nspr

- 관측 버전: `4.36`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://hg.mozilla.org/projects/nspr)
- URL 근거: `/opt/homebrew/Cellar/nspr/4.36/.brew/nspr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/nspr/4.36/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install nspr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 nss

- 관측 버전: `3.108`, `3.113`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://firefox-source-docs.mozilla.org/security/nss/index.html)
- URL 근거: `/opt/homebrew/Cellar/nss/3.113/.brew/nss.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/nss/3.108/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/nss/3.113/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install nss`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 oniguruma

- 관측 버전: `6.9.10`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/kkos/oniguruma/)
- URL 근거: `/opt/homebrew/Cellar/oniguruma/6.9.10/.brew/oniguruma.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/oniguruma/6.9.10/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install oniguruma`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 opencore-amr

- 관측 버전: `0.1.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://opencore-amr.sourceforge.net/)
- URL 근거: `/opt/homebrew/Cellar/opencore-amr/0.1.6/.brew/opencore-amr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/opencore-amr/0.1.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install opencore-amr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 openexr

- 관측 버전: `3.4.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.openexr.com/)
- URL 근거: `/opt/homebrew/Cellar/openexr/3.4.4/.brew/openexr.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openexr/3.4.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openexr`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 openjdk

- 관측 버전: `25.0.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://openjdk.org/)
- URL 근거: `/opt/homebrew/Cellar/openjdk/25.0.1/.brew/openjdk.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openjdk/25.0.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openjdk`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 openjdk@21

- 관측 버전: `21.0.9`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://openjdk.org/)
- URL 근거: `/opt/homebrew/Cellar/openjdk@21/21.0.9/.brew/openjdk@21.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openjdk@21/21.0.9/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openjdk@21`
- 이전 조건: 버전 고정 패키지를 일괄 복원하지 않는다. 기본 언어 환경은 최신 Python/JDK로 구성하고 이 버전은 프로젝트가 명시적으로 요구할 때만 추가한다.

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다. 버전·이름 조건은 위 설명을 따른다.

### 패키지 openjpeg

- 관측 버전: `2.5.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.openjpeg.org/)
- URL 근거: `/opt/homebrew/Cellar/openjpeg/2.5.4/.brew/openjpeg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openjpeg/2.5.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openjpeg`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 openjph

- 관측 버전: `0.25.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/aous72/OpenJPH)
- URL 근거: `/opt/homebrew/Cellar/openjph/0.25.3/.brew/openjph.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openjph/0.25.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openjph`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 openssl@3

- 관측 버전: `3.6.1`, `3.6.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://openssl-library.org)
- URL 근거: `/opt/homebrew/Cellar/openssl@3/3.6.2/.brew/openssl@3.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/openssl@3/3.6.1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/openssl@3/3.6.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install openssl@3`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 opus

- 관측 버전: `1.5.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.opus-codec.org/)
- URL 근거: `/opt/homebrew/Cellar/opus/1.5.2/.brew/opus.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/opus/1.5.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install opus`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 p11-kit

- 관측 버전: `0.25.10`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://p11-glue.freedesktop.org)
- URL 근거: `/opt/homebrew/Cellar/p11-kit/0.25.10/.brew/p11-kit.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/p11-kit/0.25.10/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install p11-kit`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 pango

- 관측 버전: `1.57.0_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gtk.org/docs/architecture/pango)
- URL 근거: `/opt/homebrew/Cellar/pango/1.57.0_1/.brew/pango.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pango/1.57.0_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install pango`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 pcre2

- 관측 버전: `10.47`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.pcre.org/)
- URL 근거: `/opt/homebrew/Cellar/pcre2/10.47/.brew/pcre2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pcre2/10.47/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install pcre2`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 pinentry

- 관측 버전: `1.3.1_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.gnupg.org/related_software/pinentry/)
- URL 근거: `/opt/homebrew/Cellar/pinentry/1.3.1_1/.brew/pinentry.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pinentry/1.3.1_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install pinentry`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 pixman

- 관측 버전: `0.46.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://cairographics.org/)
- URL 근거: `/opt/homebrew/Cellar/pixman/0.46.4/.brew/pixman.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pixman/0.46.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install pixman`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 pkgconf

- 관측 버전: `2.5.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/pkgconf/pkgconf)
- URL 근거: `/opt/homebrew/Cellar/pkgconf/2.5.1/.brew/pkgconf.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/pkgconf/2.5.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install pkgconf`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 python@3.13

- 관측 버전: `3.13.7`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.python.org/)
- URL 근거: `/opt/homebrew/Cellar/python@3.13/3.13.7/.brew/python@3.13.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/python@3.13/3.13.7/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install python@3.13`
- 이전 조건: 버전 고정 패키지를 일괄 복원하지 않는다. 기본 언어 환경은 최신 Python/JDK로 구성하고 이 버전은 프로젝트가 명시적으로 요구할 때만 추가한다.

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다. 버전·이름 조건은 위 설명을 따른다.

### 패키지 python@3.14

- 관측 버전: `3.14.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.python.org/)
- URL 근거: `/opt/homebrew/Cellar/python@3.14/3.14.2/.brew/python@3.14.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/python@3.14/3.14.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install python@3.14`
- 이전 조건: 버전 고정 패키지를 일괄 복원하지 않는다. 기본 언어 환경은 최신 Python/JDK로 구성하고 이 버전은 프로젝트가 명시적으로 요구할 때만 추가한다.

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다. 버전·이름 조건은 위 설명을 따른다.

### 패키지 rav1e

- 관측 버전: `0.8.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/xiph/rav1e)
- URL 근거: `/opt/homebrew/Cellar/rav1e/0.8.1/.brew/rav1e.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/rav1e/0.8.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install rav1e`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 readline

- 관측 버전: `8.3.3`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tiswww.case.edu/php/chet/readline/rltop.html)
- URL 근거: `/opt/homebrew/Cellar/readline/8.3.3/.brew/readline.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/readline/8.3.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install readline`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 rubberband

- 관측 버전: `4.0.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://breakfastquay.com/rubberband/)
- URL 근거: `/opt/homebrew/Cellar/rubberband/4.0.0/.brew/rubberband.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/rubberband/4.0.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install rubberband`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 ruby-build

- 관측 버전: `20241225.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/rbenv/ruby-build)
- URL 근거: `/opt/homebrew/Cellar/ruby-build/20241225.2/.brew/ruby-build.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/ruby-build/20241225.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install ruby-build`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 sdl2

- 관측 버전: `2.32.10`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.libsdl.org/)
- URL 근거: `/opt/homebrew/Cellar/sdl2/2.32.10/.brew/sdl2.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/sdl2/2.32.10/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install sdl2-compat`
- 이전 조건: 설치 흔적 이름은 sdl2이지만 현재 로컬 brew info는 sdl2-compat로 표시한다. 이름 변경 기록이며 상위 도구가 선택한 의존성을 따른다.

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다. 버전·이름 조건은 위 설명을 따른다.

### 패키지 shared-mime-info

- 관측 버전: `2.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://wiki.freedesktop.org/www/Software/shared-mime-info)
- URL 근거: `/opt/homebrew/Cellar/shared-mime-info/2.4/.brew/shared-mime-info.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/shared-mime-info/2.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install shared-mime-info`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 simdjson

- 관측 버전: `4.6.4`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://simdjson.org)
- URL 근거: `/opt/homebrew/Cellar/simdjson/4.6.4/.brew/simdjson.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/simdjson/4.6.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install simdjson`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 simdutf

- 관측 버전: `9.0.0`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://simdutf.github.io/simdutf/)
- URL 근거: `/opt/homebrew/Cellar/simdutf/9.0.0/.brew/simdutf.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/simdutf/9.0.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install simdutf`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 snappy

- 관측 버전: `1.2.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://google.github.io/snappy/)
- URL 근거: `/opt/homebrew/Cellar/snappy/1.2.2/.brew/snappy.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/snappy/1.2.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install snappy`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 speex

- 관측 버전: `1.2.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://speex.org/)
- URL 근거: `/opt/homebrew/Cellar/speex/1.2.1/.brew/speex.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/speex/1.2.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install speex`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 sqlite

- 관측 버전: `3.51.2_1`, `3.53.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://sqlite.org/index.html)
- URL 근거: `/opt/homebrew/Cellar/sqlite/3.53.2/.brew/sqlite.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/sqlite/3.51.2_1/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/sqlite/3.53.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install sqlite`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 srt

- 관측 버전: `1.5.4`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.srtalliance.org/)
- URL 근거: `/opt/homebrew/Cellar/srt/1.5.4/.brew/srt.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/srt/1.5.4/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install srt`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 svt-av1

- 관측 버전: `3.1.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://gitlab.com/AOMediaCodec/SVT-AV1)
- URL 근거: `/opt/homebrew/Cellar/svt-av1/3.1.2/.brew/svt-av1.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/svt-av1/3.1.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install svt-av1`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 tesseract

- 관측 버전: `5.5.1_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tesseract-ocr.github.io/)
- URL 근거: `/opt/homebrew/Cellar/tesseract/5.5.1_1/.brew/tesseract.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/tesseract/5.5.1_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install tesseract`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 theora

- 관측 버전: `1.2.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.theora.org/)
- URL 근거: `/opt/homebrew/Cellar/theora/1.2.0/.brew/theora.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/theora/1.2.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install theora`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 tree-sitter

- 관측 버전: `0.24.6`, `0.25.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tree-sitter.github.io/)
- URL 근거: `/opt/homebrew/Cellar/tree-sitter/0.25.6/.brew/tree-sitter.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/tree-sitter/0.24.6/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/tree-sitter/0.25.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install tree-sitter`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 unbound

- 관측 버전: `1.24.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.unbound.net)
- URL 근거: `/opt/homebrew/Cellar/unbound/1.24.2/.brew/unbound.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/unbound/1.24.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install unbound`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 unibilium

- 관측 버전: `2.1.2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/neovim/unibilium)
- URL 근거: `/opt/homebrew/Cellar/unibilium/2.1.2/.brew/unibilium.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/unibilium/2.1.2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install unibilium`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 utf8proc

- 관측 버전: `2.10.0`, `2.9.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://juliastrings.github.io/utf8proc/)
- URL 근거: `/opt/homebrew/Cellar/utf8proc/2.9.0/.brew/utf8proc.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/utf8proc/2.10.0/INSTALL_RECEIPT.json`, `/opt/homebrew/Cellar/utf8proc/2.9.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install utf8proc`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 uvwasi

- 관측 버전: `0.0.23`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/nodejs/uvwasi)
- URL 근거: `/opt/homebrew/Cellar/uvwasi/0.0.23/.brew/uvwasi.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/uvwasi/0.0.23/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install uvwasi`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 webp

- 관측 버전: `1.6.0`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://developers.google.com/speed/webp/)
- URL 근거: `/opt/homebrew/Cellar/webp/1.6.0/.brew/webp.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/webp/1.6.0/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install webp`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 x264

- 관측 버전: `r3222`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.videolan.org/developers/x264.html)
- URL 근거: `/opt/homebrew/Cellar/x264/r3222/.brew/x264.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/x264/r3222/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install x264`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 x265

- 관측 버전: `4.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://bitbucket.org/multicoreware/x265_git)
- URL 근거: `/opt/homebrew/Cellar/x265/4.1/.brew/x265.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/x265/4.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install x265`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 xorgproto

- 관측 버전: `2024.1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://www.x.org/)
- URL 근거: `/opt/homebrew/Cellar/xorgproto/2024.1/.brew/xorgproto.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/xorgproto/2024.1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install xorgproto`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 xvid

- 관측 버전: `1.3.7`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://labs.xvid.com/)
- URL 근거: `/opt/homebrew/Cellar/xvid/1.3.7/.brew/xvid.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/xvid/1.3.7/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install xvid`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 xz

- 관측 버전: `5.8.3`
- 설치 구분: 직접 요청 아님(의존성 표지 없음); tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://tukaani.org/xz/)
- URL 근거: `/opt/homebrew/Cellar/xz/5.8.3/.brew/xz.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/xz/5.8.3/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install xz`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 zeromq

- 관측 버전: `4.3.5_2`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://zeromq.org/)
- URL 근거: `/opt/homebrew/Cellar/zeromq/4.3.5_2/.brew/zeromq.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/zeromq/4.3.5_2/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install zeromq`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 zimg

- 관측 버전: `3.0.6`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://github.com/sekrit-twc/zimg)
- URL 근거: `/opt/homebrew/Cellar/zimg/3.0.6/.brew/zimg.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/zimg/3.0.6/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install zimg`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

### 패키지 zstd

- 관측 버전: `1.5.7_1`
- 설치 구분: 의존성 설치; tap: `homebrew/core`
- 공홈: [공식 프로젝트](https://facebook.github.io/zstd/)
- URL 근거: `/opt/homebrew/Cellar/zstd/1.5.7_1/.brew/zstd.rb` (로컬 정의, 웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Cellar/zstd/1.5.7_1/INSTALL_RECEIPT.json`
- 최신 설치 명령(필요 시 참고용): `brew install zstd`

1. 이 항목은 직접 복원 목록에서 제외하고 사용 중인 상위 도구를 먼저 설치한다.
2. 상위 도구 재설치로 필요한 최신 의존성을 복원한다. 위 명령은 프로젝트가 직접 요구할 때만 사용한다.
3. 이전 버전 Cellar나 라이브러리 파일은 복사하지 않는다.

## 앱과 글꼴 설치 패키지

### 앱 또는 글꼴 aerospace

- 디렉터리 관측 버전: `0.18.5-Beta`
- 영수증 기록 버전: `0.18.5-Beta` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `nikitabobko/tap`
- 공홈: [공식 프로젝트](https://github.com/nikitabobko/AeroSpace)
- URL 근거: `/opt/homebrew/Library/Taps/nikitabobko/homebrew-tap/Casks/aerospace.rb` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/aerospace/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask nikitabobko/tap/aerospace`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다(프로젝트가 배포하는 Beta 명명 체계를 따름).
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 alacritty

- 디렉터리 관측 버전: `0.14.0`
- 영수증 기록 버전: `0.14.0` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://github.com/alacritty/alacritty/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/alacritty/.metadata/INSTALL_RECEIPT.json`
- 최신 공식 상태: [Homebrew API](https://formulae.brew.sh/api/cask/alacritty.json)에 `disabled: true`, `disable_reason: fails_gatekeeper_check`, 비활성화 날짜 `2026-09-01`이 기록되어 있다(2026-09-06 열람).
- 설치 명령 상태: `brew install --cask alacritty`는 비활성 cask이므로 기본 설치 절차에서 제외한다. 대체 공식 설치 명령은 이 문서에서 확정하지 않는다.

1. 기존 Alacritty 설정을 보관한다.
2. [공식 프로젝트](https://github.com/alacritty/alacritty/)의 현재 macOS 설치 안내를 따른다. 사용할 수 있는 배포 경로가 정해지기 전에는 기존에 사용하는 다른 터미널을 먼저 설치한다.
3. 설치한 터미널에 사용자 설정을 적용한다. Gatekeeper 우회는 이 이전 절차에 포함하지 않는다.

### 앱 또는 글꼴 android-studio

- 디렉터리 관측 버전: `2024.2.2.14`
- 영수증 기록 버전: `2024.2.2.14` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://developer.android.com/studio/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/android-studio/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask android-studio`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 docker

- 디렉터리 관측 버전: `4.40.0,187762`
- 영수증 기록 버전: `4.38.0,181591` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://www.docker.com/products/docker-desktop)
- URL 근거: `/opt/homebrew/Caskroom/docker/.metadata/4.40.0,187762/20250425074539.503/Casks/docker-desktop.rb` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/docker/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask docker-desktop`

1. docker와 docker-desktop은 같은 Docker Desktop 설치 흔적으로 취급하고 하나만 복원한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 docker-desktop

- 디렉터리 관측 버전: `4.40.0,187762`
- 영수증 기록 버전: `4.38.0,181591` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://www.docker.com/products/docker-desktop)
- URL 근거: `/opt/homebrew/Caskroom/docker-desktop/.metadata/4.40.0,187762/20250425074539.503/Casks/docker-desktop.rb` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/docker-desktop/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask docker-desktop`

1. docker와 docker-desktop은 같은 Docker Desktop 설치 흔적으로 취급하고 하나만 복원한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 flutter

- 디렉터리 관측 버전: `3.29.0`
- 영수증 기록 버전: `3.27.1` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://flutter.dev/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/flutter/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask flutter`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 font-jetbrains-mono-nerd-font

- 디렉터리 관측 버전: `3.3.0`
- 영수증 기록 버전: `3.3.0` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://github.com/ryanoasis/nerd-fonts)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/font-jetbrains-mono-nerd-font/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask font-jetbrains-mono-nerd-font`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 터미널·편집기 설정에서 해당 글꼴 이름을 다시 지정한다.

### 앱 또는 글꼴 font-meslo-lg-nerd-font

- 디렉터리 관측 버전: `3.3.0`
- 영수증 기록 버전: `3.3.0` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://github.com/ryanoasis/nerd-fonts)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/font-meslo-lg-nerd-font/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask font-meslo-lg-nerd-font`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 터미널·편집기 설정에서 해당 글꼴 이름을 다시 지정한다.

### 앱 또는 글꼴 font-symbols-only-nerd-font

- 디렉터리 관측 버전: `3.3.0`
- 영수증 기록 버전: `3.3.0` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://github.com/ryanoasis/nerd-fonts)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/font-symbols-only-nerd-font/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask font-symbols-only-nerd-font`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 터미널·편집기 설정에서 해당 글꼴 이름을 다시 지정한다.

### 앱 또는 글꼴 ghostty

- 디렉터리 관측 버전: `1.2.0`
- 영수증 기록 버전: `1.2.0` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://ghostty.org/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/ghostty/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask ghostty`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 marta

- 디렉터리 관측 버전: `0.8.2`
- 영수증 기록 버전: `0.8.2` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://marta.sh/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/marta/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask marta`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 orca

- 디렉터리 관측 버전: `1.4.133`
- 영수증 기록 버전: `1.4.133` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `stablyai/orca`
- 공홈: [공식 프로젝트](https://onorca.dev/)
- URL 근거: `/opt/homebrew/Library/Taps/stablyai/homebrew-orca/Casks/orca.rb` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/orca/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask stablyai/orca/orca`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.

### 앱 또는 글꼴 raycast

- 디렉터리 관측 버전: `1.99.4`
- 영수증 기록 버전: `1.99.4` (앱 자체 업데이트 이후 실제 앱 버전과 다를 수 있음)
- 설치 구분: 직접 설치; tap: `homebrew/cask`
- 공홈: [공식 프로젝트](https://raycast.com/)
- URL 근거: `HOMEBREW_NO_AUTO_UPDATE=1 brew info --installed --json=v2 의 casks[].homepage` (웹 열람 없음)
- 영수증 근거: `/opt/homebrew/Caskroom/raycast/.metadata/INSTALL_RECEIPT.json`
- 최신 설치 명령: `brew install --cask raycast`

1. 기존 앱에서 사용자 설정 또는 내보내기 파일을 보관한다.
2. 위 명령으로 최신 안정판을 설치한다.
3. 필요한 사용자 설정을 옮기고 로그인 및 macOS 권한은 새 Mac에서 다시 설정한다.
