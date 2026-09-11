# pyenv

- 설치 버전: 2.8.5
- 역할: Python version management
- 분류: 명시적 설치 도구

## 사용 방법

```sh
pyenv versions
pyenv which python
# 프로젝트 버전 전환: pyenv local <설치한 정확한 버전>
```

제공 명령: `pyenv`, `pyenv-install`, `pyenv-uninstall`, `python-build`.

## 관리와 참고

설치 확인은 `brew info pyenv`. 업데이트는 필요할 때 `brew upgrade pyenv`로 진행한다. 의존성 패키지는 상위 도구의 요구를 확인하고 관리한다.

- [공식 홈페이지](https://github.com/pyenv/pyenv)
- [Homebrew 배포 정보](https://formulae.brew.sh/formula/pyenv)
