# Obsidian 프로젝트·카테고리 운영 매뉴얼

작성일: 2026-09-11. 보관함은 `~/Volt` 하나를 사용한다. 아래 분류 체계는 개인 작업용 권장 운영 규칙이며, Obsidian이나 Jira가 강제하는 표준은 아니다. 설치 순서와 완료 판정은 [설치·설정 계획](../.omo/plans/mac-mini-migration/17-obsidian-volt.md), 실제 상태는 [체크리스트](../local/INSTALL-CHECKLIST.md)에 기록한다.

## 1. 기본 모델

**폴더는 보관 위치, 속성은 분류·상태, 링크는 관계, 태그는 보조 주제**를 담당한다. 프로젝트 하나에 문서와 작업을 모으고, 전체 프로젝트를 속성으로 가로질러 조회한다. 같은 노트를 여러 카테고리 폴더에 복제하지 않는다.

| Jira에서 익숙한 개념 | Volt에서 사용할 표현 | 예시·규칙 |
| --- | --- | --- |
| 프로젝트 카테고리 | `category` | `engineering`, `knowledge` 등 프로젝트의 주된 영역 한 개 |
| 프로젝트 | `project` 및 프로젝트 홈 노트 | `"[[OBS]]"`; 목표·종료 조건이 있는 일 |
| 이슈 키 | `id` | `OBS-001`; 발급 후 재사용하지 않음 |
| 이슈 유형 | `type` | `epic`, `story`, `task`, `bug` |
| 에픽·상위 작업 | `parent` 링크 | 에픽→스토리/작업→하위 작업, 최대 3단계 |
| 컴포넌트 | `components` 목록 | `vault`, `templates`, `plugins`, `backup` |
| 워크플로 | `status` | `backlog`, `todo`, `doing`, `review`, `done`, `cancelled` |
| 우선순위 | `priority` | `P0`~`P3`; 기본 `P2` |
| 레이블 | `tags` | `topic/obsidian`, `context/mac` |
| 필터·보드 | Bases 뷰 | 프로젝트별·상태별·마감일별 목록 |

Jira와 자동 동기화되는 구성은 아니다. 실제 Jira를 함께 사용하면 팀 이슈 상태는 Jira를 원본으로 하고, Obsidian에는 `jira_url`과 설계·회의·결정 기록을 연결한다. 개인 작업만 Volt의 `status`를 원본으로 관리한다.

## 2. 폴더 구조

```text
~/Volt/
├── 00-Inbox/              # 아직 분류하지 않은 수집함
├── 10-Projects/
│   └── OBS-Obsidian/      # 프로젝트 코드-이름
│       ├── OBS.md        # 프로젝트 홈
│       └── OBS-001 보관함 검증.md
├── 20-Areas/              # 끝나는 날짜가 없는 책임 영역·운영 기준
├── 30-Resources/          # 프로젝트를 넘어 재사용할 지식·자료
├── 40-Archive/            # 완료 프로젝트와 비활성 자료
├── 50-Daily/              # YYYY-MM-DD 일일 기록
├── 90-System/             # Home, 분류 사전, 운영 매뉴얼, Bases
├── 91-Templates/          # 프로젝트·작업·지식·일일 템플릿
└── 99-Attachments/        # 이미지·PDF 등 첨부
```

PARA의 프로젝트·영역·자료·보관 구분을 응용한다. 상위 폴더 번호는 정렬용이며 Johnny.Decimal의 전체 번호 체계를 도입한 것은 아니다. MOC(Map of Content)는 링크를 모은 길잡이 노트로 사용한다. Zettelkasten의 한 노트 한 주제 원칙은 재사용 지식에 적용하되, 모든 회의록을 잘게 쪼개지는 않는다.

프로젝트의 하위 폴더는 실제로 파일이 많아질 때만 추가한다. `doing/`, `done/` 폴더를 만들지 않는다. 상태 변경은 `status` 수정으로 끝낸다. 아카이브 이동은 Obsidian 내부에서 수행하고 링크 자동 갱신을 확인한다.

## 3. 카테고리 결정 규칙

초기 사전은 다음 다섯 개다. 업무 목록을 확인한 뒤 확장할 수 있다.

| 값 | 포함 기준 | 경계 사례 |
| --- | --- | --- |
| `engineering` | 제품·코드·개발 환경 구축 | 개발 터미널 구성, 배포 자동화 |
| `knowledge` | 지식 관리·학습 체계·문서 운영 | Obsidian 구축은 여기에 배정 |
| `operations` | 반복 운영·장비·계정·유지보수 | 장치 정기 점검, 갱신 관리 |
| `business` | 고객·사업·콘텐츠 성과 | 제안서, 출시 캠페인 |
| `personal` | 개인 생활·취미 계획 | 여행 준비, 생활 프로젝트 |

분류할 때는 다음 순서를 따른다.

1. **끝나는 결과가 있는가?** 있으면 Projects. 계속 지켜야 하는 책임이면 Areas. 참고용이면 Resources. 불명확하면 Inbox.
2. **이 결과의 주된 목적은 무엇인가?** 그 목적에 맞는 `category` 하나를 선택한다. 사용한 도구로 목적을 분류하지 않는다.
3. **어느 프로젝트의 결과물인가?** 소유 프로젝트는 하나만 지정한다. 다른 프로젝트와의 관계는 `related` 링크 목록으로 표현한다.
4. **프로젝트 안의 어느 부분인가?** `components`에 복수 지정한다. `status`나 기술 이름을 최상위 카테고리로 올리지 않는다.
5. **다시 찾는 데 필요한 주제인가?** `topic/obsidian` 같은 태그를 0~3개 붙인다. 프로젝트·상태·우선순위는 태그로 중복하지 않는다.

예: “Obsidian 백업 구성”은 `category: knowledge`, `project: "[[OBS]]"`, `components: [backup]`, `tags: [topic/obsidian]`이다. “Mac 전체 백업 운영”은 `operations`의 영역 노트로 두고 서로 링크한다. “React 상태 관리 원리”는 Resources의 재사용 지식이며, 적용한 프로젝트에서 링크한다.

분류 원칙은 **한 축에 한 질문**이다. 카테고리 축은 목적, 컴포넌트 축은 구성 요소, 유형 축은 문서·작업 종류를 표현한다. 동일 축의 의미가 최대한 겹치지 않도록 하되, 분류를 완벽하게 만들려고 수집을 멈추지 않는다.

새 카테고리는 기존 정의로 설명할 수 없는 프로젝트가 3개 이상이고 별도 조회 목적이 있을 때 주간 검토에서 추가한다. 이 숫자는 초기 운영 기준이다. 단발 주제는 태그로 시작한다. 영문 소문자·하이픈 표기를 사용하고, `catagory`처럼 다른 철자나 `dev`/`development` 동의어를 섞지 않는다. 변경 시 분류 사전에 이전 값→새 값과 변경일을 남기고 전체 속성과 뷰 필터를 함께 수정한다.

## 4. 속성 스키마와 이름

Properties는 YAML frontmatter에 저장된다. 같은 속성명에는 보관함 전체에서 동일한 자료형을 사용한다. 링크 값은 따옴표로 감싼다. [공식 Properties 문서](https://obsidian.md/help/properties)

| 속성 | 자료형 | 규칙 |
| --- | --- | --- |
| `id` | Text | 프로젝트 홈 `OBS`, 이슈 `OBS-001` |
| `type` | Text | 작업: epic/story/task/bug, 문서: project/area/note/meeting/decision/daily/system |
| `category` | Text | 분류 사전의 값 하나; 프로젝트 작업은 홈과 일치 |
| `project` | Text | 소유 프로젝트 링크 하나; 독립 지식에는 생략 |
| `parent` | Text | 상위 이슈 링크; 없으면 생략, 순환 금지 |
| `components` | List | 프로젝트 홈에서 정의한 값; 없어도 빈 목록 유지 |
| `status` | Text | 작업 6상태; 프로젝트 planned/active/paused/completed/cancelled; 지식 draft/evergreen/archived |
| `priority` | Text | 작업 전용; P0 긴급 중단, P1 다음 우선, P2 일반, P3 나중 |
| `created`, `due` | Date | YYYY-MM-DD; 마감이 없으면 due 생략 |
| `blocked` | Checkbox | true/false; 차단 이유와 해소 조건은 본문 |
| `tags` | Tags | 보조 주제·맥락 |
| `related` | List | 관련 노트 링크 목록, 소유 관계와 구분 |

프로젝트명은 `OBS-Obsidian`, 홈 파일은 `OBS.md`, 이슈 파일은 `OBS-001 보관함 검증.md`처럼 코드와 읽을 수 있는 제목을 쓴다. 코드 목록과 다음 번호는 프로젝트 홈에서 관리한다. 여러 기기에서 동시에 번호를 발급하지 않는다. 자동 발급은 충돌 처리까지 설계한 뒤 도입한다.

```yaml
---
id: OBS-001
type: task
category: knowledge
project: "[[OBS]]"
components:
  - vault
status: todo
priority: P2
created: 2026-09-11
blocked: false
tags:
  - topic/obsidian
---
```

본문에는 목적, 완료 조건, 실행 체크리스트, 증거·결정 링크를 둔다. 실행 단계 체크박스를 전부 체크해도 `status`는 자동 변경되지 않는다. 독립 마감·의사결정·상태가 필요한 일은 새 이슈 노트로 분리하고 `parent`로 연결한다.

## 5. 상태와 검토 루틴

`backlog → todo → doing → review → done`을 기본 흐름으로 사용한다. 취소는 `cancelled`와 사유를 남긴다. 검토 실패 시 `review → doing`, 완료 후 재작업 시 `done → todo`로 돌아가고 이유를 기록한다.

- `todo` 진입: 목적·다음 행동·완료 조건이 명확하다.
- `doing` 진입: 실제 작업을 시작했다. 개인 동시 진행은 기본 3개 이하로 제한한다.
- 차단: 현재 상태를 유지하고 `blocked: true`, 원인·해소 담당·재확인 날짜를 본문에 적는다.
- `review` 진입: 결과와 확인 근거가 준비됐다.
- `done` 진입: 완료 조건을 검증했다. 체크박스 개수만으로 판정하지 않는다.

매일 Inbox를 분류하고 오늘 할 작업 1~3개를 고른다. Daily에는 작업 원문을 복사하지 않고 링크와 진행 기록을 남긴다. 주 1회 미분류·장기 차단·기한 초과·부모 없는 이슈·카테고리 오타를 점검한다. 월 1회 미사용 태그와 플러그인을 정리하고 백업 복원 1건을 확인한다.

프로젝트 완료 시 결과 요약과 재사용 지식을 Resources로 정리한 후 프로젝트 폴더를 Archive로 이동한다. 고유 ID는 유지한다. 진행 중 대시보드는 Archive를 제외한다.

## 6. 대시보드와 검색

기본 Bases는 Markdown 노트의 속성으로 목록을 구성한다. `90-System/Work.base`에서 모든 작업을 조회하고, 앱에서 프로젝트·상태·우선순위 필터를 추가한다. Bases는 관계형 DB의 제약 조건이나 Jira의 워크플로 검증을 자동 제공하는 것으로 간주하지 않는다. [Bases 개요](https://obsidian.md/help/bases)

초기 뷰는 `All work`, `Doing`, `Blocked`다. 초기 목록은 작업 파일만 포함한다. 마감일 관리가 필요해지면 `due` 열과 오름차순 정렬을 추가한다. 프로젝트 홈에는 목표·완료 조건·컴포넌트 사전·결정 링크를 유지한다. 분류와 상태의 원본은 각 노트의 속성이다.

Kanban의 카드 이동과 이슈 노트 `status`가 자동으로 동기화된다고 가정하지 않는다. 현재 설치된 보드와 CLI의 상태 조정 방법은 [Kanban 운영 매뉴얼](obsidian-kanban.md)을 따른다.

## 7. 설치·추천 플러그인

2026-09-11에 Tasks 8.4.0과 QuickAdd 2.25.0을 초기 플러그인으로 설치·활성화했다. 추가 요청으로 Kanban 2.0.51·Tasks Kanban 0.10.3·Excalidraw 2.27.3도 설치했다. 나머지는 추천 목록이다. 플러그인별 실제 상태·버전·검증 결과는 [체크리스트](../local/INSTALL-CHECKLIST.md)를 기준으로 한다.

| 상태·순서 | 플러그인 | 도입 이유·설정 기준 | 공식 출처 |
| --- | --- | --- | --- |
| 설치됨 | Tasks 8.4.0 | 여러 노트의 세부 체크리스트·반복 작업·기한 조회. global filter는 `#task`이며 업무 체크박스에만 사용 | [저장소](https://github.com/obsidian-tasks-group/obsidian-tasks) |
| 설치됨 | QuickAdd 2.25.0 | Inbox 수집과 프로젝트·이슈 템플릿 생성 단축. Inbox task capture와 New task note만 구성 | [문서](https://quickadd.obsidian.guide/) |
| 선택 2 | Templater | 프로젝트 선택·날짜 등 동적 템플릿. 기본 Templates로 부족할 때 도입; 동일 생성 경로에 두 엔진을 중복 적용하지 않음 | [문서](https://silentvoid13.github.io/Templater/) |
| 선택 2 | Omnisearch | 노트가 많아지면 본문 검색 개선. PDF·이미지 검색은 별도 인덱싱 요구사항 확인 | [저장소](https://github.com/scambier/obsidian-omnisearch) |
| 선택 3 | Dataview | Bases로 표현하기 어려운 읽기용 집계. 우선 DQL만 사용하고 JavaScript 쿼리는 필요할 때 검토 | [저장소](https://github.com/blacksmithgu/obsidian-dataview) |
| 설치됨 | Excalidraw 2.27.3 | 설계 스케치·시각적 지식 연결. 일반 관계도는 기본 Canvas부터 사용 | [저장소](https://github.com/zsviczian/obsidian-excalidraw-plugin) |
| 조건부 | Git | Markdown 변경 이력과 복구 보조. 저장소·인증·충돌 처리 확인 후 도입 | [저장소](https://github.com/Vinzent03/obsidian-git) |
| 설치됨 | Kanban 2.0.51 | 시각적 보드에는 유용하나 현재 저장소에 새 유지관리자 모집 안내가 있음. 업데이트 전 유지보수 상태 재확인 | [현재 저장소](https://github.com/community-archive/obsidian-kanban) |

Tasks는 체크박스 단위 도구이고, 이 매뉴얼의 이슈는 노트 단위다. 이슈 상태는 YAML, 세부 단계 완료는 체크박스가 각각 담당한다. Tasks를 설치한 후 사용할 조회 예:

````markdown
```tasks
not done
path includes 10-Projects/
sort by due
```
````

현재 QuickAdd 사용 절차는 Command palette에서 `QuickAdd: Run QuickAdd`를 실행해 `Inbox task capture` 또는 `New task note`를 고르는 것이다. 전자는 `Enter value` 한 항목만 입력받아 `00-Inbox/Inbox.md`에 `#task` 체크박스를 추가한다. 마감일이 있으면 작업을 만든 뒤 명시적으로 추가한다. 후자는 `91-Templates/Task.md`를 바탕으로 `00-Inbox`에 작업 노트를 만든다. 생성한 노트의 `id`·`category`·`project`는 확인 뒤 직접 확정한다.

추가 설치는 Settings → Community plugins에서 Restricted mode를 해제하고 Browse에서 이름과 제작자를 확인한 뒤 Install → Enable 순서로 진행한다. 한 개 설치할 때마다 샘플 생성·편집·재시작을 확인하고 버전과 설정을 도구 체크리스트에 기록한다. 커뮤니티 플러그인은 로컬 파일 등에 접근할 수 있으므로 공식 프로젝트와 설정을 확인한다. [공식 설치 안내](https://obsidian.md/help/community-plugins)

## 8. 백업·확장 원칙

보관함 전체와 `.obsidian` 설정을 별도 저장장치 또는 버전 있는 백업 대상으로 포함한다. 동기화는 백업을 대체하지 않는다. 다음은 로컬 스냅샷을 만들고 별도 폴더에 복원하는 재현 가능한 절차다. 실행 전에 Obsidian을 종료해 열린 파일이 없는 상태를 만든다.

```zsh
backup_root="$HOME/.local/state/wonder-envy/backups/obsidian"
stamp="$(date +%Y%m%dT%H%M%S%z)"
mkdir -p "$backup_root/$stamp"
ditto -c -z --keepParent "$HOME/Volt" "$backup_root/$stamp/Volt.cpgz"

restore_root="$(mktemp -d)"
ditto -x "$backup_root/$stamp/Volt.cpgz" "$restore_root"
diff -qr "$HOME/Volt" "$restore_root/Volt"
```

`diff`가 출력 없이 끝나면 노트·첨부·`.obsidian`을 포함한 파일 내용이 일치한다. 복원본은 원본 보관함으로 쓰지 말고 Obsidian에서 별도 vault로 열어 설정과 노트가 실제로 열리는지도 확인한다. 이 경로의 스냅샷은 같은 디스크에 있으므로 실수 복구에는 쓸 수 있어도 디스크 고장·분실에 대비한 독립 백업은 아니다. 확인 후 암호화된 외장 저장장치나 신뢰하는 버전 있는 원격 백업에 archive를 복사하고, 그 사본도 같은 절차로 정기 복원한다.

멀티디바이스가 필요해지면 Obsidian Sync 또는 다른 동기화 방식 하나를 선택한다. 같은 보관함에 여러 동기화 엔진을 겹쳐 적용하지 않는다. Git을 도입하면 원격 공개 여부와 첨부 용량을 검토하고, 초기에는 수동 commit으로 충돌 처리를 익힌다. API 키는 노트에 기록하지 않는다.

팀 권한·감사 이력·자동 워크플로가 필요하면 Jira를 유지하고 Obsidian을 개인 지식·설계 기록 공간으로 연결한다. 파일 수가 커지면 플러그인 수·첨부·조회 범위를 먼저 점검하고, 접근 권한이나 동기화 경계가 달라질 때 보관함 분리를 검토한다.

추가 도구: Tasks Kanban 0.10.3의 6상태 보드와 OpenCode·Claude Code `/kanban` 설정은 [Kanban·CLI 운영](obsidian-kanban.md)을 참조한다.
