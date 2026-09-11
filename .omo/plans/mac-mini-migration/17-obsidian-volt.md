# 17. Obsidian 설치와 Volt 운영 계획

작성일: 2026-09-11. 요청 범위: Obsidian 설치, `~/Volt` 사용 준비, 파워유저 community plugin 추천, Jira식 프로젝트·카테고리 운영 매뉴얼, 옵시디언 도구 관리 체크리스트 추가.

## 설계 결정

- `~/Volt` 자체를 단일 vault로 사용한다. 하위에 다시 Volt 보관함을 만들지 않는다.
- PARA를 응용한 물리 폴더와 `category/project/type/status/components` 속성을 결합한다.
- 상세 규칙은 [운영 매뉴얼](../../../menual/obsidian.md)을 기준으로 한다.
- 초기에는 코어 Bases·Templates·Daily notes·Properties·Backlinks·Canvas·File recovery를 사용한다.
- 커뮤니티 플러그인은 추천·후속 도입 계획으로 구분한다. 추천했다는 이유만으로 일괄 활성화하지 않는다.

## 단계별 실행과 완료 조건

| 단계 | 실행 내용 | 완료 조건 |
| --- | --- | --- |
| 1. 설치 | Homebrew의 `brew install --cask obsidian`; 실패하면 공식 Mac 배포 검토 | `/Applications/Obsidian.app` 버전과 cask 영수증 확인 |
| 2. 보관함 준비 | 기존 파일 유무 확인, 폴더·홈·분류 사전·템플릿·샘플·Bases 파일 생성 | 기존 자료 손실 없이 생성되고 JSON/YAML·링크 정합성 확인 |
| 3. 앱 설정 | Open folder as vault → `~/Volt`; 아래 기본 설정 적용·확인 | 템플릿으로 노트 생성, 첨부 위치와 링크 갱신 확인 |
| 4. 실제 운영 검증 | OBS-001 샘플의 상태·차단 값을 바꾸고 Bases 목록 확인 | doing/blocked 필터 변화와 재시작 후 상태 유지 |
| 5. 백업 | 보관함과 숨김 설정 폴더를 포함하는 백업 수단 설정 | 별도 폴더로 노트·첨부 복원 성공 |
| 6. 확장 | Tasks→QuickAdd부터 필요에 따라 한 개씩 도입 | 플러그인별 버전·목적·설정·확인 결과 기록 |
| 7. 정착 | 일주일 후 카테고리·상태·WIP·플러그인 검토 | 실제 프로젝트를 입력하고 미분류·중복 속성 정리 |

일정 제안: 첫날 1~4단계, 첫 주 5~6단계, 1주 후 7단계. 백업 수단·모바일 동기화·유료 서비스 선택은 실제 사용 요구에 따라 결정한다. 이 문서는 일정 제안이며 자동 실행 예약은 아니다.

## 앱에서 확인할 기본 설정

| 설정 | 값 |
| --- | --- |
| Files and links → Default location for new notes | `00-Inbox` |
| Default location for new attachments | `99-Attachments` |
| Automatically update internal links | 켜기 |
| Deleted files | 시스템 휴지통 |
| Templates folder | `91-Templates` |
| Daily notes folder / format | `50-Daily` / `YYYY-MM-DD` |
| Daily notes template | `91-Templates/Daily.md` |
| Properties in document | Visible |
| 시작 화면 | `90-System/Home.md`를 북마크 |
| 테마 | 기본 테마로 시작; 사용성이 안정되면 변경 |
| Community plugins | 초기에는 Restricted mode 유지, 선택한 플러그인 도입 시 해제 |

JSON 파일을 준비한 상태와 앱에서 작동을 확인한 상태를 구분한다. 최초 실행에서 보관함 등록이 필요할 수 있다. 기본 Templates의 `{{date}}`, `{{title}}`를 사용하며 프로젝트 링크·카테고리·고유 ID는 생성 후 직접 확정한다.

## 복구·운영

플러그인 도입 전 vault 백업을 만들고 문제 발생 시 해당 플러그인을 끈 뒤 재시작한다. 복구 시 `.obsidian`을 통째로 덮어쓰기 전에 현재 설정을 별도 보관한다. 운영 노트는 `~/Volt`, 환경 관리 문서의 원본은 이 저장소에 둔다. Volt에 복사된 매뉴얼은 참고용 스냅샷이며 업데이트 시 원본에서 다시 복사한다.

## 출처

- [Obsidian 공식 다운로드](https://obsidian.md/download)
- [Properties](https://obsidian.md/help/properties), [Bases](https://obsidian.md/help/bases), [Bases 파일 문법](https://obsidian.md/help/bases/syntax)
- [Community plugins 설치](https://obsidian.md/help/community-plugins)
- 플러그인별 공식 문서와 선정 이유는 [운영 매뉴얼](../../../menual/obsidian.md)에 정리했다.

실제 완료/미완료는 [설치 체크리스트](../../../local/INSTALL-CHECKLIST.md)의 “17. 옵시디언 도구 관리”를 기준으로 한다.

## TODOs — 2026-09-11 실행

이번 실행은 현재 가능한 설치·설정·검증과 문서 커밋·푸시를 완료한다. 1주 운영 회고와 필요 시 다기기 동기화는 후속 운영 항목으로 유지한다.

- [x] A. 현재 보관함을 백업하고 별도 경로 복원·내용 일치를 확인한다.
- [x] B. Volt를 앱에 등록하고 기본 설정·Tasks·QuickAdd 설치 및 동작을 확인한다.
- [x] C. 템플릿·Bases 필터·첨부·링크·재시작 시나리오를 검증한다.
- [x] D. 실제 설치 버전·사용법·백업 절차·남은 운영 항목을 문서와 체크리스트에 반영한다.

E. 전달: Obsidian 변경만 커밋하고 독립 검토 후 origin/main에 푸시한다. 전달 완료 여부는 Git 이력과 원격 SHA를 기준으로 확인한다.

## Final Verification Wave

F. 최종 검증: 커밋 SHA에 대한 독립 검토·실행 증거와 원격 반영을 확인한다. SHA별 검토 결과는 로컬 실행 ledger에 기록한다. 문서가 자기 자신의 커밋·푸시 상태를 고정 기록하지 않는다.

## 실행 결과 요약

2026-09-11에 Obsidian 1.13.7과 초기 확장 Tasks 8.4.0·QuickAdd 2.25.0을 설치했다. 공식 릴리스 자산 해시를 확인하고 앱에서 활성 버전·설정을 조회했다. 초기 Restricted mode는 이 두 플러그인을 사용하도록 해제했다. 나머지 추천 플러그인은 필요 시 도입한다.

Volt 등록, Home 북마크, 속성 자료형, 템플릿 생성, Bases의 Doing/Blocked 필터, 첨부 위치, 링크 이름 갱신, QuickAdd 수집·템플릿 실행, 재시작 유지와 테스트 자료 정리를 앱의 공식 CLI로 검증했다. 접근성 화면 제어 서비스는 응답하지 않아 중단했으며, 앱 자체 CLI와 실제 Home 스크린샷을 사용했다.

설치 전 `.obsidian`을 포함한 `ditto` 스냅샷을 만들고 별도 임시 경로에 복원·비교했다. 독립 검토에서 아카이브 해시와 복원을 재확인했다. 같은 디스크에 보관한 복구 사본으로, 외부 저장소 백업은 아직 구성하지 않았다.

1주 운영 후 분류·WIP 검토와 필요 시 다기기 동기화는 후속 운영이다. 현재 설치·검증 요약은 [결과 기록](../../../local/checks/obsidian-results.json), 사용 흐름은 [매뉴얼](../../../menual/obsidian.md)에서 확인한다.
