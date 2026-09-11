# 사용자 Python 경로의 추가 CLI

관측일: 2026-09-06. `~/Library/Python/3.9/bin` 파일명과 `~/Library/Python/3.9/lib/python/site-packages/*.dist-info/METADATA`의 이름·버전·공홈 필드를 읽었다. 해당 CLI나 디버거·서버를 실행하지 않았다. Python 3.9를 새 Mac에서 재현할 필요는 없다. 후속 확정에 따라 Python은 pyenv가 설치하고 uv가 환경·패키지를 관리한다. [상세 계획](11-runtime-managers.md)을 우선한다.

## IPython

- 현재 `ipython`, `ipython3` 진입점이 존재하며 `ipython-8.18.1.dist-info/METADATA`에 8.18.1이 기록되어 있다.
- 공홈: [IPython 공식 설치 문서](https://ipython.readthedocs.io/en/stable/install/install.html).

1. 최신 지원 Python과 uv를 먼저 설치한다.
2. 독립 전역 REPL이 필요하면 새 Mac에서 `uv tool install --python "$(pyenv which python)" ipython`으로 최신 버전을 설치한다. 프로젝트 라이브러리를 사용할 REPL은 해당 프로젝트 환경에 IPython을 설치한다.
3. `~/.ipython`의 사용자 설정·startup 파일은 선별 보관한다. 이 디렉터리 존재는 확인했지만 내부 사용자 코드의 의존성은 분석하지 않았다.
4. 기존 `~/Library/Python/3.9/bin`을 새 PATH에 추가하지 않는다. 새 패키지가 생성한 진입점을 사용한다.

## Jupyter Core와 Jupyter Client

- `jupyter_core` 5.7.2, `jupyter_client` 8.6.3 메타데이터가 존재한다.
- 관측 명령: `jupyter`, `jupyter-kernel`, `jupyter-kernelspec`, `jupyter-migrate`, `jupyter-run`, `jupyter-troubleshoot`.
- [Jupyter 공식 설치 문서](https://jupyter.org/install)는 JupyterLab·Notebook 설치 경로를 각각 제공한다. 위 명령 존재만으로 JupyterLab 서버가 설치되어 있다고 단정하지 않는다.

1. 새 프로젝트 환경에서 필요한 경우 `uv pip install jupyter-core jupyter-client`로 최신 기반 패키지를 설치한다. 먼저 `uv venv --python "$(pyenv which python)"`로 새 프로젝트 가상환경을 만든다. macOS 시스템 Python에 설치하라는 뜻이 아니다.
2. 노트북 UI도 사용하려면 해당 환경에 최신 `jupyterlab` 또는 `notebook`을 추가한다. 둘을 무조건 추가할 필요는 없다.
3. `~/.jupyter`의 설정과 실제 `.ipynb` 파일을 자료로 옮긴다. 기존 kernelspec의 `argv`가 옛 인터프리터를 가리킬 수 있으므로 새 환경 기준으로 커널을 재등록한다.
4. runtime 디렉터리·connection 파일·서버 토큰·소켓은 복사하지 않는다. 본 조사에서는 서버를 시작하지 않았다.

## debugpy

- `debugpy` 진입점과 `debugpy-1.8.13.dist-info/METADATA`가 존재한다.
- 공홈: [Microsoft debugpy 공식 저장소](https://github.com/microsoft/debugpy).

1. VS Code Python 확장의 번들 사용과 프로젝트 패키지 사용을 구분한다. IDE 확장만 쓰는 경우 별도 전역 설치를 강제하지 않는다.
2. 프로젝트에 독립 패키지가 필요한 경우 새 가상환경에서 `uv pip install debugpy`로 최신 버전을 설치한다.
3. 프로젝트 `.vscode/launch.json`의 인터프리터·소스 매핑·절대경로를 새 프로젝트 경로에 맞춘다.
4. 기존 디버깅 포트와 실행 상태를 이전하지 않는다. attach·listen·디버깅 시험은 하지 않는다.

## Pygments와 pygmentize

- `pygmentize` 진입점과 Pygments 2.19.1 메타데이터가 존재한다.
- 공홈: [Pygments 공식 설치 안내](https://pygments.org/download/).

1. 최신 Python 및 uv를 준비한다.
2. 전역 명령이 필요한 경우 `uv tool install --python "$(pyenv which python)" pygments`로 최신 배포를 설치한다. 다른 도구의 의존성으로만 쓰는 경우 상위 패키지 설치에 맡긴다.
3. 사용자 lexer·formatter·스타일 모듈이 있다면 소스와 등록 방법을 함께 보관한다. 이번 조사에서 사용자 플러그인 존재는 확정하지 않았다.
4. Python 3.9용 script와 site-packages를 그대로 복원하지 않는다.

## 추가 런타임 흔적

`/usr/local/n/versions/node/20.14.0`이 발견되어 구 Node 관리자인 `n`의 기존 설치 흔적을 확인했다. 이 디렉터리도 기본 최신 Node 설치로 대체하며 프로젝트 명시 요구가 없으면 재현하지 않는다.

`~/.local/share/uv/python`에는 `cpython-3.11-macos-aarch64-none`와 `cpython-3.11.15-macos-aarch64-none`이 있다. 이름만으로 활성 Python을 판정하지 않는다. `.go/bin`, `go/bin`은 조사한 홈에서 없었고 `.pub-cache`에는 기본 `bin` 디렉터리가 없었다. 따라서 해당 경로에서 추가 Go/Dart 전역 CLI는 관측되지 않았다.

이 문서의 10개 실행 파일은 [6개 전역 디렉터리 대응표](08-executable-map.md)의 942개에 포함되지 않는다. 두 범위를 합치면 관측된 이름·경로 항목은 952개이며, 같은 제품의 보조 명령·중복 링크가 포함된 수치다.
