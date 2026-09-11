# poppler

- 설치 버전: 26.09.0
- 역할: PDF rendering library (based on the xpdf-3.0 code base)
- 분류: 명시적 설치 도구

## 사용 방법

```sh
pdftotext input.pdf output.txt
pdfinfo input.pdf
```

제공 명령: `pdfattach`, `pdfdetach`, `pdffonts`, `pdfimages`, `pdfinfo`, `pdfseparate`, `pdfsig`, `pdftocairo`, `pdftohtml`, `pdftoppm`, `pdftops`, `pdftotext`, `pdfunite`.

## 관리와 참고

설치 확인은 `brew info poppler`. 업데이트는 필요할 때 `brew upgrade poppler`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://poppler.freedesktop.org/)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/poppler)
