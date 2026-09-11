# difftastic

- 설치 버전: 0.70.0
- 역할: Diff that understands syntax
- 분류: 명시적 설치 도구

## 사용 방법

```sh
git -c diff.external=difft diff
difft before.ts after.ts
```

제공 명령: `difft`.

## 관리와 참고

설치 확인은 `brew info difftastic`. 업데이트는 필요할 때 `brew upgrade difftastic`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://difftastic.wilfred.me.uk/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/difftastic)
