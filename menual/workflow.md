# 일상 개발 흐름과 추가 도구

터미널의 기본 셸은 Fish다. Node·Java도 Fish에서 사용하며, 프로젝트의 실제 폴더에서 `herdr`를 시작한다. `y`로 파일을 고르고 `nvim`으로 편집하며 `lg`로 변경을 살펴본다. `exit`는 자식 개발 셸을 종료한다.

## 파일·내용·구조·문서 찾기

| 대상 | 도구 | 예시 |
| --- | --- | --- |
| 파일 이름 | fd | `fd --type f '\.md$'` |
| 후보 선택 | fzf | `fd --type f \| fzf` |
| 파일 본문 | ripgrep | `rg -n 'TODO' .` |
| 코드 구조 | ast-grep | `ast-grep run --lang ts --pattern 'console.log($$$ARGS)' src/` |
| JSON | jq | `jq 'keys' data.json` |
| YAML | Mike Farah yq | `yq -o=json '.' config.yaml` |
| Markdown | mdq | `mdq '#' README.md` |

`fd`·`rg`의 기본 무시 규칙은 유지한다. 숨김 파일이 필요할 때 해당 호출에만 `--hidden`을 붙인다. fzf 예시는 후보 표시용이며 임의 파일명을 shell code로 실행하는 wrapper가 아니다. 각 도구의 옵션은 [개별 매뉴얼](README.md)을 참고한다.

## Worktrunk

```sh
wt list
wt switch existing-branch
wt switch --create feature/example
```

기존 프로젝트에 최초 커밋이 있어야 한다. 새 worktree의 실제 경로에서 `herdr`를 열거나 원하는 pane에서 그 경로로 이동한다. 하나의 셸에서 `wt switch`를 실행해도 다른 pane은 이동하지 않는다. Orca/Paseo가 관리하는 worktree의 생성·정리는 해당 앱이 담당한다.

정리 전 변경·프로세스를 확인한다. branch를 보존하려면 `wt remove --no-delete-branch --foreground feature/example`을 사용한다. 이 명령은 worktree를 실제로 제거하므로 작업 완료 후에만 실행한다.

설정은 `~/.config/worktrunk/config.toml`, 프로젝트 hook은 선택적인 `.config/wt.toml`이다. 초기 구성에는 자동 agent·merge·서버 시작 hook을 추가하지 않았다. [공식 사용법](https://worktrunk.dev/), [설정](https://worktrunk.dev/config/), [제거](https://worktrunk.dev/remove/)

## Atuin + fzf

- Ctrl-R: Atuin 이력 검색. 선택한 명령은 편집 후 실행한다.
- Ctrl-T: fzf 파일 선택.
- Alt-C: fzf 디렉터리 선택. macOS Option 키 전달은 터미널 설정에 따른다.
- 방향키는 기존 셸 동작을 유지한다. Atuin AI 키는 등록하지 않았다.

```sh
atuin search --limit 10 'git'
```

`~/.config/atuin/config.toml`은 `auto_sync=false`, `enter_accept=false`다. 클라우드 동기화·옛 이력 import를 하지 않았다. 이력은 개인 자료이므로 저장소에 추가하지 않는다. [공식 설치](https://docs.atuin.sh/latest/guide/installation/), [키 설정](https://docs.atuin.sh/latest/configuration/key-binding/)

## mise

런타임은 기존 nvm·pyenv·SDKMAN이 관리한다. `mise`는 이름 붙인 작업을 실행하는 용도로 사용한다.

```toml
# 프로젝트 mise.toml 예시
[tasks.env-paths]
description = "개발 도구 경로"
run = "command -v node; command -v python; command -v java"
```

```sh
mise tasks ls
mise run env-paths
```

설정에 신뢰가 필요하면 내용을 읽고 해당 파일만 `mise trust`로 등록한다. 현재 저장소에는 명세만으로 프로젝트 런타임을 추가하는 `[tools]` 구성을 두지 않았다. Fish의 Homebrew 자동 activation은 같은 이름의 사용자 `conf.d/mise-activate.fish`로 비활성화했다. [공식 Tasks](https://mise.jdx.dev/tasks/)

## Hurl

```hurl
GET {{base_url}}/health
HTTP 200
```

위 내용을 프로젝트의 `tests/http/health.hurl`에 저장한 뒤 준비된 로컬 서버를 대상으로 실행한다.

```sh
hurl --test --variable base_url=http://127.0.0.1:8080 tests/http/health.hurl
```

URL·경로·응답 조건은 실제 API에 맞춘다. 서버 시작은 별도이며 토큰은 공유하는 명세에 넣지 않는다. 설치 확인에는 임시 loopback 서버만 사용했고 종료했다. [공식 튜토리얼](https://hurl.dev/docs/tutorial/your-first-hurl-file.html)

## lnav

```sh
lnav application.log
lnav access.log error.log
```

`?`는 도움말, `q`는 종료다. `;`로 SQL 조회를 시작하며 인식된 로그 테이블에 맞춰 조회한다. 사용자 설정·포맷은 이 Mac에서 `~/.config/lnav`에 저장된다. 원본 로그는 자동 이동·삭제하지 않는다. [공식 매뉴얼](https://docs.lnav.org/en/latest/)

## difftastic

```sh
git -c diff.external=difft diff
difft before.ts after.ts
```

구문을 고려한 비교가 필요할 때 명시적으로 사용한다. 일반 `git diff`와 lazygit의 기본 diff는 유지했다. patch 생성·적용은 기존 Git을 쓴다. [공식 Git 연동](https://difftastic.wilfred.me.uk/git.html)
