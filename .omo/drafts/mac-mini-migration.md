---
slug: mac-mini-migration
status: complete
intent: clear
review_required: false
pending-action: none
approach: 최신 도구 신규 설치와 사용자 설정 선별 이전을 위한 읽기 전용 조사 및 Markdown 계획 작성
---

# Mac mini 이전 조사 기록

## 요청과 결정

- 현재 디렉터리 하위에 카테고리별·도구별 상세 Markdown을 생성한다.
- 사용자 후속 결정: 기존 버전 재현 불필요, 최신 버전 우선.
- 추가 확정: Java SDKMAN, Node nvm, Python 인터프리터 pyenv와 환경·패키지 uv. `penv`는 사용자가 pyenv로 정정했다. 공식 설치·사용법을 재조사한 11-runtime-managers.md 및 기존 연결 문서에 반영했다.
- 추가 요청: Fish·Oh My Posh·Herdr(사용자 확인 https://herdr.dev/)·Aside 브라우저/CLI·Paseo(https://paseo.sh/) 상세 가이드를 12 문서에 작성했다. 공식 웹·배포 스크립트를 읽었으며 설치자·앱·서버·테스트는 실행하지 않았다.
- 실제 장치 설치·변경·테스트·OMO QA는 하지 않는다.
- 문서 생성은 사용자에게 이미 요청받은 작업이므로 재승인 대기를 만들지 않았다.
- 한국어 문서 지침과 테스트 금지 지시를 스킬의 영문 헤더·QA 기본값보다 우선했다.

## 조사 영역

| 영역 | 산출물 | 상태 |
| --- | --- | --- |
| 패키지와 전역 설치 | 01·02 | 작성 완료 |
| 셸·개발·보안 | 03·04 | 작성 완료 |
| AI 설정과 플러그인 | 05 | 작성 완료 |
| 앱 CLI와 개인 도구 | 06 | 작성 완료 |
| 전달 순서와 목록 | 07·08·10 | 작성 완료 |
| 공식 배포 자료 | 09 | 작성 완료 |

## 산출물

전체 계획은 [Mac mini 이전 계획](../plans/mac-mini-migration.md), 상세 문서는 같은 이름의 하위 디렉터리에 있다. 현재 디렉터리 README.md에 문서 안내를 제공한다.

## 근거와 미확인 영역

Formula 203종, Caskroom 13개, 전역 명령 경로 942개와 별도 사용자 Python 명령 10개를 기록했다. 공식 API·공홈 조회는 09 문서에 성공과 실패를 구분했다. 개인 도구 출처, 프로젝트 전체 의존성, 새 Mac 사양·인증·실행 상태는 미확인으로 남겼다.

## 완료 범위

후속 사용 흐름: Orca + Herdr 또는 Paseo + Herdr에 Yazi·Neovim·lazygit을 결합하는 13 문서를 추가했다. lazygit은 기존 계획에 포함되어 있었고 현재 Neovim 플러그인·단축키 선언을 직접 읽었다. 전용 앱 간 integration 또는 중첩 TUI 실행 성공을 주장하지 않았다.

후속 결정: tmux를 새 Mac의 설치·복원에서 제외하고 Herdr로 대체한다. Ghostty는 필수 설치 대상이며 공식 설치·설정 문서를 다시 열람해 03 문서를 보강했다. 기존 Mac의 tmux를 제거하거나 설정을 삭제하지 않았다.

조사 및 계획 문서 작성 완료. 실제 Mac mini 이전 미실행. 테스트·QA·OMO 검토 작업 없음. 원본 설정과 비밀값·키·대화 파일을 새 산출물로 복사하지 않았다.
