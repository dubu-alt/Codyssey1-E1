# ✅ Windows + VS Code 최종 체크리스트

> **이 체크리스트를 하나씩 따라가면 과제 완성!** 🚀

---

## 📋 PHASE 1: 준비 (30분)

### Step 1-1: 프로그램 설치
- [x] Git for Windows 설치 (`git --version` 확인)
- [x] Docker Desktop 설치 (`docker --version` 확인)
- [x] VS Code 설치 (Docker, Git History 확장 설치)
- [x] 작업 폴더 생성: `C:\my-dev-workspace`
- [x] VS Code에서 폴더 열기

### Step 1-2: VS Code 터미널 세팅
- [x] 터미널 열기: Ctrl + `
- [x] PowerShell 또는 Git Bash 선택
- [x] `pwd` 명령으로 현재 위치 확인

---

## 📋 PHASE 2: 기초 (30분)

### Step 2-1: 터미널 명령 실습 (이 명령들을 모두 실행하고 출력 결과 캡처)

```
[x] pwd                        → 현재 위치 출력
[x] ls -la                     → 파일 목록 (숨김 포함)
[x] mkdir app                  → app 폴더 생성
[x] cd app                     → 폴더 이동
[x] cd ..                      → 상위 폴더로 이동
[x] touch test.txt             → 파일 생성
[x] echo "hello" > test.txt    → 파일 내용 작성
[x] cat test.txt               → 파일 내용 보기
[x] rm test.txt                → 파일 삭제
[x] cp file1.txt file2.txt     → 파일 복사
[x] mv file.txt newfile.txt    → 파일 이름 변경
```

### Step 2-2: 파일 권한 실습

```
[x] ls -l hello.txt                    → 권한 확인
[ ] chmod +x hello.txt                 → 실행 권한 추가
[ ] ls -l hello.txt                    → 변경 확인
[ ] chmod 755 app                      → 폴더 권한 변경
```

**📸 스크린샷**: 권한 변경 전/후 비교

---

## 📋 PHASE 3: Docker 기초 (40분)

### Step 3-1: Docker 점검

```
[ ] docker --version                   → 버전 확인
[ ] docker info                        → 정보 확인
```

**📸 스크린샷**: `docker info` 출력
![docker version](image.png)
![도커 정보 플러그인 생략](image-1.png)
### Step 3-2: 기본 컨테이너 실행

```
[ ] docker run hello-world             → hello-world 실행
[ ] docker ps                          → 실행 중인 컨테이너
[ ] docker ps -a                       → 모든 컨테이너
[ ] docker images                      → 이미지 목록
```

### Step 3-3: Ubuntu 컨테이너 진입

```
[ ] docker run -it ubuntu bash         → Ubuntu 진입
  (내부)
[ ] ls -la                             → 파일 목록
[ ] echo "test"                        → 텍스트 출력
[ ] cat /etc/os-release                → OS 정보
[ ] exit                               → 종료
```

**📸 스크린샷**: Ubuntu 진입 화면

---

## 📋 PHASE 4: 웹 서버 구축 (60분)

### Step 4-1: 파일 생성

#### `app/index.html` 만들기

VS Code 탐색기에서:
```
1. app 폴더 우클릭
2. 새 파일: index.html
3. 다음 내용 입력:
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello World</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 40px;
            text-align: center;
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <h1>🌟 안녕하세요!</h1>
    <p>첫 번째 웹 페이지입니다.</p>
    <p>Docker 컨테이너에서 실행 중입니다.</p>
</body>
</html>
```

- [ ] HTML 파일 저장 (Ctrl+S)

#### `app/app.py` 만들기

```
1. app 폴더에서 새 파일: app.py
2. 다음 코드 입력:
```

```python
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return SimpleHTTPRequestHandler.do_GET(self)

os.chdir('/app')
server = HTTPServer(('0.0.0.0', 8000), MyHandler)
print("🌟 웹 서버 시작됨! http://localhost:8000 접속하세요")
server.serve_forever()
```

- [ ] Python 파일 저장 (Ctrl+S)

### Step 4-2: Dockerfile 생성

```
1. 루트 폴더(my-dev-workspace)에서 새 파일: Dockerfile
2. 대소문자 정확하게! (Dockerfile, dockerfile X)
3. 다음 내용 입력:
```

```dockerfile
FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

COPY app/ /app/

WORKDIR /app

EXPOSE 8000

CMD ["python3", "app.py"]
```

- [ ] Dockerfile 저장 (Ctrl+S)

### Step 4-3: Docker 이미지 빌드

터미널에서 (C:\my-dev-workspace 위치):

```
[ ] docker build -t my-web-server:1.0 .
```

예상 출력:
```
[+] Building 45.2s (7/7) FINISHED
...
Successfully tagged my-web-server:1.0
```

**📸 스크린샷**: 빌드 완료 메시지

- [ ] 이미지 확인: `docker images`

---

## 📋 PHASE 5: 포트 매핑 & 브라우저 (20분)

### Step 5-1: 컨테이너 실행

```
[ ] docker run --name my-server -p 8000:8000 my-web-server:1.0
```

예상 출력:
```
🌟 웹 서버 시작됨! http://localhost:8000 접속하세요
```

💡 **주의**: Ctrl+C로 멈출 수 있지만, 이 상태로 두세요 (다음 단계에서 사용)

### Step 5-2: 브라우저 접속

다른 터미널 열기:
```
[ ] Chrome/Edge/Firefox 실행
[ ] 주소 표시줄에 입력: http://localhost:8000
[ ] Enter 누르기
```

예상 화면:
```
🌟
안녕하세요!

첫 번째 웹 페이지입니다.
Docker 컨테이너에서 실행 중입니다.
```

**📸 스크린샷** (매우 중요!):
- 주소창에 "localhost:8000" 보이는 화면
- 웹 페이지 렌더링된 화면
- 이 두 사진을 README.md에 붙여넣기!

---

## 📋 PHASE 6: Docker 볼륨 (30분)

### Step 6-1: 볼륨 생성

```
[ ] docker volume create my-data-volume
[ ] docker volume ls
```

### Step 6-2: 볼륨으로 컨테이너 실행

기존 컨테이너 종료 (Ctrl+C)

```
[ ] docker run --name my-server-vol \
      -p 8000:8000 \
      -v my-data-volume:/data \
      my-web-server:1.0
```

### Step 6-3: 데이터 생성 (새 터미널)

```
[ ] docker exec -it my-server-vol bash
```

컨테이너 내부:
```
[ ] echo "중요한 데이터입니다!" > /data/important.txt
[ ] cat /data/important.txt
[ ] exit
```

**📸 스크린샷**: 데이터 생성 확인

### Step 6-4: 컨테이너 삭제 후 데이터 확인

```
[ ] docker container rm my-server-vol
[ ] docker volume ls              (← 볼륨 남아있는지 확인)
```

**📸 스크린샷**: 볼륨은 남아있는 화면

### Step 6-5: 새 컨테이너로 복구

```
[ ] docker run --name my-server-vol2 \
      -p 8000:8000 \
      -v my-data-volume:/data \
      my-web-server:1.0
```

```
[ ] docker exec -it my-server-vol2 bash
```

컨테이너 내부:
```
[ ] cat /data/important.txt        (← 이전 데이터가 보여야 함!)
[ ] exit
```

**📸 스크린샷**: 데이터 복구 확인

### Step 6-6: 바인드 마운트 실습 (선택)

```
[ ] mkdir shared-data
[ ] echo "공유 파일" > shared-data/test.txt
[ ] docker run --name my-bind-mount \
      -p 8000:8000 \
      -v C:\my-dev-workspace\shared-data:/app/shared \
      my-web-server:1.0
```

```
[ ] docker exec -it my-bind-mount bash
  (컨테이너 내부)
[ ] cat /app/shared/test.txt
[ ] exit
```

**📸 스크린샷**: 바인드 마운트 작동 확인

---

## 📋 PHASE 7: Git & GitHub (30분)

### Step 7-1: Git 설정

```
[ ] git config --global user.name "홍길동"
[ ] git config --global user.email "gildong@example.com"
[ ] git config --list
```

**📸 스크린샷**: `git config --list` 출력

### Step 7-2: 저장소 초기화 (이미 했으면 skip)

```
[ ] git init
[ ] git add .
[ ] git commit -m "초기 설정: 웹 서버 구축"
```

### Step 7-3: GitHub 저장소 생성

```
1. https://github.com > 우측 상단 +
2. New repository 클릭
3. Repository name: my-dev-workspace
4. Description: "Windows 환경에서 Docker 웹 서버 구축"
5. Public (공개) 선택
6. Create repository 클릭

[ ] GitHub 저장소 URL 복사
    https://github.com/사용자명/my-dev-workspace
```

**📸 스크린샷**: GitHub 저장소 페이지

### Step 7-4: 로컬과 GitHub 연결

```
[ ] git remote add origin https://github.com/사용자명/my-dev-workspace.git
[ ] git push -u origin main
```

**📸 스크린샷**: 푸시 완료 메시지

### Step 7-5: GitHub 웹에서 확인

```
[ ] https://github.com/사용자명/my-dev-workspace
[ ] Dockerfile, app/, README.md 파일 보이는지 확인
```

**📸 스크린샷**: GitHub 저장소 페이지 (파일 목록 보이는 화면)

---

## 📋 PHASE 8: README.md 작성 (60분)

### Step 8-1: README.md 템플릿 사용

```
1. 루트 폴더에 README.md 파일 생성
2. 다음 템플릿 복사 (위에서 제공한 README_template.md)
3. 자신의 정보로 수정:
   - [당신의 이름]
   - [당신의 GitHub 사용자명]
   - [작성 날짜]
   - 스크린샷 경로 추가
```

### Step 8-2: 필수 포함 내용

**섹션 1: 프로젝트 개요**
- [ ] 미션 목표 정리
- [ ] 주요 성과 표로 정리

**섹션 2: 실행 환경**
- [ ] OS, Docker, Git, VS Code 버전
- [ ] `docker --version` 출력 결과

**섹션 3: 수행 항목 체크리스트**
- [ ] 터미널 명령 10개 이상
- [ ] Docker 명령 10개 이상
- [ ] 권한, 포트, 볼륨 등 모두 체크 표시

**섹션 4: 검증 방법 & 결과**
- [ ] 각 명령어와 출력 결과를 코드블록으로 정리
- [ ] 스크린샷 삽입 (주소창 보이는 사진)

**섹션 5: 트러블슈팅 (2건 이상)**
- [ ] 문제 상황
- [ ] 원인 가설
- [ ] 확인 과정
- [ ] 해결 방법

### Step 8-3: README.md 저장 및 GitHub 푸시

```
[ ] Ctrl + S로 저장
[ ] git add README.md
[ ] git commit -m "최종 보고서: README.md 작성 완료"
[ ] git push origin main
```

---

## 📋 PHASE 9: 최종 점검 (10분)

### Step 9-1: GitHub 저장소 확인

```
[ ] https://github.com/사용자명/my-dev-workspace 접속
[ ] 파일 목록:
    ✅ Dockerfile
    ✅ app/ 폴더
    ✅ README.md
    ✅ .git/ 폴더 (숨김)
```

### Step 9-2: README.md 최종 검수

GitHub에서 README.md 열어서 확인:
- [ ] 제목과 개요 명확함
- [ ] 환경 정보 명시되어 있음
- [ ] 체크리스트 항목이 모두 ✅ 표시됨
- [ ] 명령어와 출력 결과가 코드블록으로 정리됨
- [ ] 스크린샷이 포함되어 있음 (주소창, 웹 페이지, 터미널)
- [ ] 트러블슈팅이 2건 이상 포함됨
- [ ] 민감한 정보(토큰, 비밀번호) 없음

### Step 9-3: 로컬 폴더 최종 확인

```
[ ] C:\my-dev-workspace 폴더 열기
[ ] 파일 구조:
    ✅ README.md
    ✅ Dockerfile
    ✅ app/index.html
    ✅ app/app.py
    ✅ .git/ 폴더
    ✅ .gitignore (선택)
```

---

## 🎯 최종 제출 체크리스트

### 필수 제출물

```
☑️  GitHub Repository 링크
    https://github.com/사용자명/my-dev-workspace

☑️  README.md 포함 내용:
    ✅ 프로젝트 개요
    ✅ 실행 환경 (Docker, Git, OS 버전)
    ✅ 수행 항목 체크리스트
    ✅ 검증 방법 + 결과
    ✅ 명령어 실행 로그 (코드블록)
    ✅ 스크린샷 (포트 매핑, 웹 페이지)
    ✅ 트러블슈팅 2건 이상

☑️  소스 코드:
    ✅ Dockerfile
    ✅ app/app.py
    ✅ app/index.html

☑️  Git & GitHub:
    ✅ 공개 저장소
    ✅ 최소 1개 커밋
    ✅ GitHub 웹에서 확인 가능
```

---

## 🚀 제출 방법

### 제출할 것:

**GitHub Repository URL**을 과제 제출 폼에 입력:
```
https://github.com/[당신의username]/my-dev-workspace
```

### 확인 사항:

```
1. 링크에 들어가면 README.md 바로 보여야 함 ✅
2. README.md 내에 모든 증거(스크린샷, 명령어, 출력)가 있어야 함 ✅
3. 파일들이 모두 Public하게 공개되어야 함 ✅
4. 민감한 정보(토큰 등)가 없어야 함 ✅
```

---

## 💡 마지막 팁

### 문제가 생기면:

```
1. 에러 메시지를 전부 복사
2. ChatGPT 또는 Claude에 붙여넣기
3. "Windows Docker에서 이 에러가 나는데 어떻게 해?"라고 물어보기
4. 해결 방법을 README.md의 "트러블슈팅" 섹션에 추가!
```

### 스크린샷 찍을 때:

```
✅ 주소 표시줄이 보여야 함 (localhost:8000)
✅ 웹 페이지 내용이 렌더링되어야 함
✅ 터미널의 명령어와 출력이 명확해야 함
✅ 파일 탐색기의 폴더 구조가 명확해야 함
```

### 시간 관리:

```
Phase 1-2: 1시간 (기초)
Phase 3-4: 1.5시간 (Docker + 웹서버)
Phase 5-6: 1시간 (포트매핑 + 볼륨)
Phase 7-8: 1시간 (Git + README)
Phase 9: 30분 (최종 점검)

총 5시간 정도면 충분합니다!
```

---

## ✅ 완료 신호

이것들이 모두 ✅ 되면 **과제 완성**입니다! 🎉

- [ ] GitHub 저장소 공개
- [ ] README.md 완성 (모든 섹션 포함)
- [ ] 모든 스크린샷 포함
- [ ] 트러블슈팅 2건 이상 기록
- [ ] 로컬과 GitHub 동기화 완료
- [ ] 민감 정보 제거 확인

---

**화이팅! 당신은 할 수 있습니다!** 💪

다른 질문이 생기면 언제든지 물어보세요! 😊
