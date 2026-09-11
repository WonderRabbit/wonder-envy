# nss

- 설치 버전: 3.129
- 역할: Libraries for security-enabled client and server applications
- 분류: 의존성으로 설치

## 사용 방법

```sh
man addbuiltin
man atob
man baddbdir
# 제공 명령의 상세 옵션은 아래 공식 문서를 참조
```

제공 명령: `addbuiltin`, `atob`, `baddbdir`, `bltest`, `btoa`, `certutil`, `chktest`, `cmsutil`, `crlutil`, `dbtest`, `dbtool`, `derdump`, `dertimetest`, `digest`, `ecperf`, `encodeinttest`, `fbectest`, `fipstest`, `httpserv`, `listsuites`, `makepqg`, `mangle`, `modutil`, `multinit`, `nonspr10`, `nss-config`, `nss-policy-check`, `nssdefaults`, `ocspclnt`, `ocspresp`, `oidcalc`, `p7content`, `p7env`, `p7sign`, `p7verify`, `pk11ectest`, `pk11gcmtest`, `pk11importtest`, `pk11mode`, `pk12util`, `pk1sign`, `pkix-errcodes`, `pp`, `pwdecrypt`, `remtest`, `rsaperf`, `rsapoptst`, `sdbthreadtst`, `sdrtest`, `secmodtest`, `selfserv`, `shlibsign`, `signtool`, `signver`, `ssltap`, `strsclnt`, `symkeyutil`, `tstclnt`, `validation`, `vfychain`, `vfyserv`.

## 관리와 참고

설치 확인은 `brew info nss`. 업데이트는 필요할 때 `brew upgrade nss`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://firefox-source-docs.mozilla.org/security/nss/index.html)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/nss)
