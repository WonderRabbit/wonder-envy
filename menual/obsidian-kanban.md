# Obsidian Kanban·CLI 운영

2026-09-11 설치. 보관함은 `~/Volt`, 기본 보드는 `10-Projects/OBS-Obsidian/OBS Kanban.md`다.

## 설치 구성

| 플러그인 | 버전 | 용도 |
| --- | --- | --- |
| [Kanban](https://github.com/community-archive/obsidian-kanban/releases/tag/2.0.51) | 2.0.51 | Markdown 파일의 열과 카드를 직접 관리 |
| [Tasks Kanban](https://github.com/Djiit/obsidian-tasks-kanban/releases/tag/0.10.3) | 0.10.3 | Tasks 체크박스를 상태별 보드로 조회·이동 |
| [Excalidraw](https://github.com/zsviczian/obsidian-excalidraw-plugin/releases/tag/2.27.3) | 2.27.3 | 설계 그림·시각 노트 |

“kanban task”는 기존 Tasks 8.4.0과 연동하는 Tasks Kanban으로 구성했다. 기존 QuickAdd도 유지한다. Kanban은 현재 community-archive 저장소에서 배포하므로 업데이트 전 백업하고 샘플 보드로 확인한다. 설치 자산과 SHA-256은 [설치 기록](../local/checks/obsidian-kanban-results.json)에 남긴다. Kanban 자산은 배포자 digest가 없어 내려받은 파일의 hash만 기록했고, 다른 두 플러그인은 GitHub release digest와 대조했다.

## 상태·카테고리 규칙

프로젝트·카테고리는 [기존 운영 매뉴얼](obsidian.md)의 규칙을 따른다. 보드는 프로젝트마다 하나로 시작한다. 제목에는 필요하면 `[[상세 노트]]` 링크를 넣는다. 카드는 한 줄로 유지하고 상세 설명은 연결된 노트에 적는다.

| 열 | Tasks 체크박스 | 뜻 |
| --- | --- | --- |
| backlog | `[B]` | 후보 |
| todo | `[ ]` | 실행 준비 |
| doing | `[/]` | 진행 |
| review | `[R]` | 검토 |
| done | `[x]` | 완료 |
| cancelled | `[-]` | 취소 |

각 카드에는 `#task`와 고유 block ID가 붙는다. 자동 ID는 `kb-`와 UUID이며 프로젝트 번호가 필요하면 `--id OBS-003`처럼 지정하고 프로젝트 홈의 다음 번호도 갱신한다. ID는 변경하거나 재사용하지 않는다. **카드 상태와 연결 노트 YAML `status`는 별개**다. 노트 단위 이슈의 원본은 기존대로 YAML이며, 이 CLI는 그것을 자동 변경하지 않는다.

일반 Kanban 드래그는 열, Tasks Kanban 드래그는 체크박스를 바꾼다. 두 화면의 자동 양방향 동기화는 제공하지 않는다. GUI 작업 후 사용한 화면에 맞게 명시적으로 조정한다.

```sh
volt-kanban sync --from columns  # 일반 Kanban 열을 기준으로 체크박스 조정
volt-kanban sync --from tasks    # Tasks 체크박스를 기준으로 열 조정
```

혼합 편집 후에는 `list`로 상태를 확인하고 어느 쪽을 기준으로 할지 결정한다. CLI `move`·`done`은 열과 체크박스를 한 번에 변경한다. ID 없는 GUI 카드는 조회만 가능하며 sync에서 제외된다. 관리하려면 카드 끝에 고유 `^ID`를 추가한다.

## CLI 사용

Obsidian이 실행 중이고 Settings → General → Command line interface가 켜져 있어야 한다. `uv`가 PATH에 있어야 하며, 처음 실행할 때 잠긴 의존성을 내려받는다.

```sh
volt-kanban list
volt-kanban create '검색 설계 [[검색 상세]]' --id OBS-003
volt-kanban show OBS-003
volt-kanban move OBS-003 doing
volt-kanban edit OBS-003 '검색 설계 검토 [[검색 상세]]'
volt-kanban done OBS-003
```

다른 프로젝트는 전역 옵션을 명령 앞에 놓는다.

```sh
volt-kanban --vault Volt --board '10-Projects/APP-App/APP Kanban.md' init
volt-kanban --board '10-Projects/APP-App/APP Kanban.md' create '첫 작업'
```

`init`은 기존 파일을 덮어쓰지 않는다. `--help`로 옵션을 확인한다. `OBSIDIAN_VAULT`, `VOLT_KANBAN_BOARD`, `OBSIDIAN_CLI` 환경변수로 기본값을 바꿀 수 있다. 출력은 JSON이다. 동시 수정은 앱 내부 원자적 비교 후 쓰기로 검사하고 `CONFLICT`를 반환한다. 다시 읽고 의도를 확인한 뒤 재시도한다. 잘못된 ID·중복 ID·지원하지 않는 레이아웃·여러 줄 카드는 거절한다. 삭제·반복 작업 생성·완료일 기록은 이 도구의 기능에 포함되지 않는다.

## OpenCode·Claude Code

두 도구의 새 세션에서 다음처럼 요청한다.

```text
/kanban 티켓 목록을 보여줘
/kanban OBS-003을 doing으로 이동해
/kanban "검색 설계" 티켓을 만들어줘
```

공유 skill은 `~/.claude/skills/volt-kanban/SKILL.md`에 설치했다. OpenCode도 이 위치를 검색한다. slash command는 `~/.claude/commands/kanban.md`, `~/.config/opencode/commands/kanban.md`에 각각 설치했다. Claude Code에서는 `/volt-kanban`으로 skill을 직접 호출할 수도 있다. 실행 중이던 세션은 다시 열어 새 파일을 검색하게 한다.

[OpenCode skills](https://opencode.ai/docs/skills/), [OpenCode commands](https://opencode.ai/docs/commands/), [Claude Code skills](https://code.claude.com/docs/en/skills)에 따른 경로다. OpenCode의 실제 skill 검색 결과를 확인했다. Claude Code 파일 배치와 skill 형식은 검증했으며 모델을 호출하는 전체 대화 테스트는 수행하지 않았다.

## 재설치·검증

저장소 루트에서 실행한다. 플러그인 설치와 별도로 CLI·skill·command를 배치하는 스크립트다. 변경되는 기존 파일은 로컬 백업 폴더에 보존한다.

```sh
sh local/obsidian/install.sh
uv run --with pytest --with pydantic pytest -q local/obsidian/tests
VOLT_KANBAN_LIVE=1 uv run --with pytest --with pydantic pytest -q local/obsidian/tests/test_live.py
```

실제 보관함 테스트는 임시 보드를 생성해 동시 수정 거부·한글/셸 구문 보존·상태 이동을 검사한 뒤 자기 파일만 삭제한다. 런타임은 `~/.local/share/wonder-envy/obsidian`, 실행 파일은 `~/.local/bin/volt-kanban`이다. 잠금 파일로 의존성 버전을 고정한다. uninstall 시 이 도구의 위 경로와 두 command 파일만 제거하고 보관함·다른 skill은 유지한다.
