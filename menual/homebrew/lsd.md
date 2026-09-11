# lsd

설치 버전: 1.2.0. 파일 목록을 색상·아이콘·트리로 표시한다. Homebrew 직접 설치 도구다.

```fish
lsd
lsd -lah
lsd --tree --depth 2
lsd --color always --icon always
```

Fish 별칭은 `ls`, `ll`, `la`, `lt`다. 시스템 ls는 `command ls`로 실행한다. 설정은 `~/.config/lsd/config.yaml`, Catppuccin Mocha 색상은 같은 폴더의 `colors.yaml`이다. 아이콘은 JetBrainsMono Nerd Font를 사용한다. 기존 eza와 함께 설치되어 있다.

확인: `lsd --version`, `brew info lsd`. 업데이트: `brew upgrade lsd`.

- [lsd 공식 사용법](https://github.com/lsd-rs/lsd)
- [Homebrew 배포](https://formulae.brew.sh/formula/lsd)
- [Catppuccin 포트](https://github.com/catppuccin/lsd)
- [Fish·테마 운영](../fish-and-themes.md)
