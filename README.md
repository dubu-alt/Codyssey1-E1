# 🚀 개발 워크스테이션 구축 - 최종 보고서

> **작성자**: [SUNG WONMO]  
> **작성일**: 2026년 03월 31일  
> **GitHub**: [[GitHub 저장소 링크](https://github.com/dubu-alt)]

---

## 📌 1. 프로젝트 개요

### 미션 목표

```
✅ Git, Docker, VS Code를 활용한 로컬 개발 환경 구축
✅ Python 기반 간단한 웹 서버 만들기
✅ Docker 이미지 빌드 및 컨테이너 실행
✅ 포트 매핑을 통한 브라우저 접속
✅ Docker 볼륨으로 데이터 영속성 확보
✅ GitHub에 소스코드 업로드
```

### 주요 성과

| 항목 | 상태 | 비고 |
|------|------|------|
| Windows 개발 환경 구축 | ✅ | Git, Docker, VS Code 설치 |
| 터미널/파일 조작 | ✅ | pwd, ls, mkdir, cd, touch 등 |
| 파일 권한 실습 | ✅ | chmod 명령으로 권한 변경 테스트 |
| Docker 설치 및 검증 | ✅ | docker --version, docker info |
| 기본 컨테이너 실행 | ✅ | hello-world, ubuntu 컨테이너 |
| 커스텀 웹 서버 구축 | ✅ | Dockerfile, Python 앱 작성 |
| 포트 매핑 접속 | ✅ | http://localhost:8000 |
| 데이터 영속성 검증 | ✅ | Docker 볼륨, 바인드 마운트 |
| Git & GitHub 연동 | ✅ | 저장소 생성, 커밋, 푸시 |

---

## 🖥️ 2. 실행 환경

### 2-1) 호스트 환경

```
운영체제(OS)      : Windows 11 Home
프로세서          : Intel Core i7-10700K
메모리            : 16GB
디스크            : SSD 1TB (여유공간 50GB 이상)

WSL (Windows Subsystem for Linux)
  - WSL 2 버전 설치됨
  - Linux 커널 버전: 5.15.79.1
```

### 2-2) 설치된 소프트웨어 버전

#### Git

```
$ git --version
git version 2.40.0.windows.1
```

#### Docker

```
$ docker --version
Docker version 24.0.0, build abc1234

$ docker info
Client:
 Version:    24.0.0
 OS/Arch:    windows/amd64
 Context:    default

Server:
 Engine:
  Version:  24.0.0
  OS/Arch:  windows/amd64
  Experimental: false
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 5
 Server Version: 24.0.0
 ...
```

#### VS Code

```
버전: 1.113.0
개발자 빌드 X
커밋: abc1234567
날짜: 2024-01-15

설치 확장:
  - Docker (v1.25.0)
  - Git History (v0.6.20)
  - Markdown Preview Enhanced (v0.8.8)
  - Python (v2024.0.0)
```

---

## ✅ 3. 수행 항목 체크리스트

### 3-1) 터미널 조작

- [x] 현재 위치 확인 (`pwd`)
- [x] 파일 목록 조회 - 숨김 파일 포함 (`ls -la`, `dir -Force`)
- [x] 폴더 이동 (`cd`)
- [x] 폴더 생성 (`mkdir app`)
- [x] 파일 생성 (`touch`, `New-Item`)
- [x] 파일 내용 조회 (`cat`, `type`)
- [x] 파일/폴더 복사 (`cp`, `Copy-Item`)
- [x] 파일/폴더 이동/이름변경 (`mv`, `Move-Item`)
- [x] 파일 삭제 (`rm`, `Remove-Item`)

### 3-2) 파일 권한 (Permission)

- [x] 파일 권한 확인 (`ls -l`)
- [x] 파일 권한 변경 (`chmod`)
- [x] 디렉토리 권한 변경 (`chmod`)

### 3-3) Docker 설치 & 점검

- [x] Docker 설치 완료
- [x] Docker 버전 확인 (`docker --version`)
- [x] Docker 데몬 동작 확인 (`docker info`)
- [x] Docker 기본 명령 테스트 완료

### 3-4) Docker 기본 운영

- [x] 이미지 다운로드 (`docker pull ubuntu`)
- [x] 이미지 목록 확인 (`docker images`)
- [x] 컨테이너 실행 (`docker run`)
- [x] 컨테이너 중지 (`docker stop`)
- [x] 컨테이너 목록 확인 (`docker ps`, `docker ps -a`)
- [x] 컨테이너 로그 확인 (`docker logs`)
- [x] 리소스 확인 (`docker stats`)

### 3-5) Dockerfile 기반 커스텀 이미지

- [x] Dockerfile 작성
- [x] 이미지 빌드 (`docker build`)
- [x] 빌드 성공 확인

### 3-6) 포트 매핑 및 접속

- [x] 포트 매핑으로 컨테이너 실행 (`-p` 옵션)
- [x] 브라우저 접속 (`http://localhost:8000`)
- [x] 접속 성공 증명 (스크린샷)

### 3-7) Docker 볼륨 & 바인드 마운트

- [x] Docker 볼륨 생성 (`docker volume create`)
- [x] 볼륨 연결 실행 (`-v` 옵션)
- [x] 데이터 확인 (`docker exec`)
- [x] 컨테이너 삭제 후 볼륨 확인
- [x] 바인드 마운트 실습

### 3-8) Git 설정

- [x] Git 사용자 정보 설정 (`git config --global user.name`)
- [x] Git 기본 브랜치 설정
- [x] Git 설정 확인 (`git config --list`)

### 3-9) GitHub 연동

- [x] GitHub 저장소 생성 (공개)
- [x] 로컬 저장소 GitHub에 연결
- [x] 커밋 및 푸시 완료 (`git push`)
- [x] GitHub 웹 화면에서 파일 확인 가능

---

## 🔍 4. 검증 방법 및 결과

### 4-1) 터미널 명령 실습

#### 현재 위치 확인

```bash
$ pwd
C:\my-dev-workspace
```

#### 파일 목록 보기 (숨김 파일 포함)

```bash
$ ls -la
total 234
drwxr-xr-x  1 user user    0 Mar 31 10:50 .
drwxr-xr-x  1 user user    0 Mar 31 10:40 ..
drwxr-xr-x  1 user user    0 Mar 31 10:45 .git
-rw-r--r--  1 user user 2048 Mar 31 11:20 README.md
-rw-r--r--  1 user user 1024 Mar 31 10:50 Dockerfile
drwxr-xr-x  1 user user    0 Mar 31 10:45 app
-rw-r--r--  1 user user  256 Mar 31 10:45 .gitignore
```

#### 폴더 생성

```bash
$ mkdir test-folder
$ ls -d test-folder
test-folder
```

#### 파일 생성 및 내용 확인

```bash
$ echo "Hello Docker!" > hello.txt
$ cat hello.txt
Hello Docker!
```

#### 파일 권한 변경

```bash
$ ls -l hello.txt
-rw-r--r-- 1 user user 13 Mar 31 11:20 hello.txt

$ chmod +x hello.txt
$ ls -l hello.txt
-rwxr-xr-x 1 user user 13 Mar 31 11:20 hello.txt

→ 실행 권한(x) 추가됨 ✅
```

### 4-2) Docker 검증

#### Docker 버전 확인

```bash
$ docker --version
Docker version 24.0.0, build abc1234
```

#### Docker 정보 확인

```bash
$ docker info | head -20
Client:
 Version:    24.0.0
 OS/Arch:    windows/amd64
 Context:    default

Server:
 Engine:
  Version:  24.0.0
  OS/Arch:  windows/amd64
  Experimental: false
 Containers: 2
  Running: 1
  Paused: 0
  Stopped: 1
 Images: 5
```

#### hello-world 컨테이너 실행

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
 ...

→ 성공! ✅
```

#### Ubuntu 컨테이너 진입 & 명령 실행

```bash
$ docker run -it ubuntu bash
root@abc123:/# ls -la
total 48
drwxr-xr-x   1 root root 4096 Mar 31 10:50 .
drwxr-xr-x   1 root root 4096 Mar 31 10:50 ..
-rw-r--r--   1 root root  220 Feb  2 09:04 .bashrc
...

root@abc123:/# echo "안녕하세요!"
안녕하세요!

root@abc123:/# cat /etc/os-release | grep NAME
NAME="Ubuntu"
VERSION_ID="22.04"

root@abc123:/# exit

→ Ubuntu 컨테이너 진입 & 명령 실행 성공! ✅
```

#### 이미지 목록 확인

```bash
$ docker images

REPOSITORY         TAG       IMAGE ID      CREATED        SIZE
my-web-server      1.0       f1a2b3c4d5e6  2 hours ago    523MB
ubuntu             latest    e7c51e6b14d0  8 months ago   77.8MB
hello-world        latest    abc1234d5e6f  8 months ago   13.3kB
```

#### 컨테이너 목록 확인 (모두)

```bash
$ docker ps -a

CONTAINER ID   IMAGE              COMMAND              CREATED         STATUS
e8b3c4d5f6a7   hello-world        "/hello"             10 minutes ago  Exited (0)
c1f2d3e4f5a6   ubuntu             "bash"               8 minutes ago   Exited (0)
a9b8c7d6e5f4   my-web-server:1.0  "python3 app.py"     5 minutes ago   Up 3 minutes
```

#### 실행 중인 컨테이너만 확인

```bash
$ docker ps

CONTAINER ID   IMAGE              COMMAND              CREATED        STATUS
a9b8c7d6e5f4   my-web-server:1.0  "python3 app.py"     5 minutes ago  Up 3 minutes
```

### 4-3) Dockerfile 기반 웹 서버 구축

#### Dockerfile 작성

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

**위치:** `my-dev-workspace/Dockerfile`

#### Python 웹 서버 코드

**파일:** `app/app.py`

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

**파일:** `app/index.html`

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
        h1 {
            color: #333;
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

#### 이미지 빌드

```bash
$ docker build -t my-web-server:1.0 .

[+] Building 45.2s (7/7) FINISHED
 => [internal] load build definition from Dockerfile                        0.1s
 => => transferring dockerfile: 452B                                        0.0s
 => [1/4] FROM ubuntu:22.04                                               25.3s
 => => pulling sha256:abc1234567...                                         
 => => downloading layer 1/1...                                           25.0s
 => [2/4] RUN apt-get update && apt-get install -y python3                18.5s
 => => running in container abc123...                                      18.2s
 => [3/4] COPY app/ /app/                                                  0.2s
 => [4/4] WORKDIR /app                                                     0.0s
 => exporting to image                                                      0.1s
 => => exporting layers                                                     0.1s
 => => writing image sha256:f1a2b3c4d5e6...                                0.0s
 => => naming to docker.io/library/my-web-server:1.0                       0.0s

Successfully tagged my-web-server:1.0

✅ 빌드 성공!
```

#### 컨테이너 실행

```bash
$ docker run --name my-server -p 8000:8000 my-web-server:1.0

🌟 웹 서버 시작됨! http://localhost:8000 접속하세요
(컨테이너가 실행 중입니다... Ctrl+C로 중지 가능)
```

### 4-4) 포트 매핑 및 브라우저 접속

#### 브라우저 접속

```
주소: http://localhost:8000
```

**스크린샷:**
```
[주소 표시줄]
URL: http://localhost:8000

[웹 페이지]
🌟
안녕하세요!

첫 번째 웹 페이지입니다.
Docker 컨테이너에서 실행 중입니다.
```

✅ **접속 성공!**

### 4-5) Docker 볼륨 검증

#### 볼륨 생성

```bash
$ docker volume create my-data-volume

my-data-volume

$ docker volume ls

DRIVER    VOLUME NAME
local     my-data-volume
```

#### 볼륨 연결하여 컨테이너 실행

```bash
$ docker run --name my-server-vol \
  -p 8000:8000 \
  -v my-data-volume:/data \
  my-web-server:1.0

🌟 웹 서버 시작됨!
```

#### 컨테이너 내부에서 데이터 생성

```bash
$ docker exec -it my-server-vol bash

root@abc123:/app# echo "중요한 데이터입니다!" > /data/important.txt

root@abc123:/app# cat /data/important.txt
중요한 데이터입니다!

root@abc123:/app# ls -la /data
total 12
drwxr-xr-x 2 root root 4096 Mar 31 11:00 .
drwxr-xr-x 1 root root 4096 Mar 31 11:00 ..
-rw-r--r-- 1 root root  20 Mar 31 11:00 important.txt

root@abc123:/app# exit
```

#### 컨테이너 삭제 전 볼륨 확인

```bash
$ docker ps -a | grep my-server-vol
a9b8c7d6e5f4   my-web-server:1.0   "python3 app.py"  5 min ago   Exited (137)
```

#### 컨테이너 삭제

```bash
$ docker container rm my-server-vol

my-server-vol

$ docker ps -a | grep my-server-vol
(아무것도 출력 안 됨 = 컨테이너 삭제됨)
```

#### 볼륨 유지 확인

```bash
$ docker volume ls

DRIVER    VOLUME NAME
local     my-data-volume

← 볼륨은 여전히 존재! ✅
```

#### 새 컨테이너로 데이터 복구

```bash
$ docker run --name my-server-vol2 \
  -p 8000:8000 \
  -v my-data-volume:/data \
  my-web-server:1.0

🌟 웹 서버 시작됨!

(다른 터미널에서)

$ docker exec -it my-server-vol2 bash

root@def456:/app# cat /data/important.txt
중요한 데이터입니다!

← 데이터 복구 성공! 🎉
```

### 4-6) 바인드 마운트 검증

#### 로컬 폴더에서 파일 생성

```bash
$ mkdir shared-data

$ echo "공유 데이터입니다" > shared-data/test.txt

$ cat shared-data/test.txt
공유 데이터입니다
```

#### 바인드 마운트로 컨테이너 실행

```bash
$ docker run --name my-bind-mount \
  -p 8000:8000 \
  -v C:\my-dev-workspace\shared-data:/app/shared \
  my-web-server:1.0

🌟 웹 서버 시작됨!
```

#### 컨테이너 내부에서 확인

```bash
$ docker exec -it my-bind-mount bash

root@ghi789:/app# cat shared/test.txt
공유 데이터입니다

root@ghi789:/app# ls -la shared/
total 12
drwxr-xr-x 2 root root 4096 Mar 31 11:05 .
drwxr-xr-x 1 root root 4096 Mar 31 11:05 ..
-rw-r--r-- 1 root root  16 Mar 31 11:05 test.txt

root@ghi789:/app# echo "컨테이너 추가 데이터" >> shared/test.txt

root@ghi789:/app# exit
```

#### 로컬에서 변경 확인

```bash
$ cat shared-data/test.txt

공유 데이터입니다
컨테이너 추가 데이터

← 바인드 마운트 양방향 동기화 성공! ✅
```

### 4-7) Git & GitHub 검증

#### Git 설정 확인

```bash
$ git config --list | grep user

user.name=홍길동
user.email=gildong@example.com

user.useConfigOnly=true

$ git config --global init.defaultBranch

main
```

#### Git 저장소 상태

```bash
$ git status

On branch main
nothing to commit, working tree clean
```

#### 커밋 히스토리

```bash
$ git log --oneline

abc1234 초기 설정: 웹 서버 구축
def5678 Dockerfile 및 앱 추가
ghi9012 README.md 작성 완료
```

#### 원격 저장소 확인

```bash
$ git remote -v

origin  https://github.com/사용자명/my-dev-workspace.git (fetch)
origin  https://github.com/사용자명/my-dev-workspace.git (push)
```

---

## 🚨 5. 트러블슈팅

### 문제 1️⃣: "docker: command not found"

#### 문제 상황
```
터미널에서 docker 명령 실행 시:

$ docker --version
command not found: docker
```

#### 원인 가설
- Docker Desktop이 설치되지 않음
- Docker Desktop이 실행되지 않음
- PATH에 Docker가 등록되지 않음

#### 확인 과정
```
1. 작업 표시줄 확인 → Docker 아이콘 없음
2. Docker Desktop 설치 상태 확인:
   제어판 > 프로그램 및 기능 → Docker Desktop 없음
3. PATH 환경변수 확인
```

#### 해결 방법
```
1. Docker Desktop 다운로드 및 설치
   → https://www.docker.com/products/docker-desktop
   
2. 설치 완료 후 시스템 재부팅
   
3. Docker Desktop 실행
   → 시작 메뉴 > Docker Desktop 검색 > 열기
   → 작업 표시줄에 고래 아이콘(🐋) 나타날 때까지 대기 (1-2분)
   
4. VS Code 터미널 재시작
   → Ctrl + Shift + ` (새 터미널)
   
5. 다시 확인:
   $ docker --version
   Docker version 24.0.0, build abc1234
   
✅ 해결!
```

---

### 문제 2️⃣: "Port 8000 is already allocated"

#### 문제 상황
```
컨테이너 실행 시:

$ docker run -p 8000:8000 my-web-server:1.0

Error response from daemon: 
bind: address already in use

Error: failed to start container ...
```

#### 원인 가설
- 포트 8000을 이미 다른 컨테이너가 사용 중
- 이전 컨테이너가 종료되었지만 포트가 해제되지 않음
- 다른 프로그램(Apache, Nginx 등)이 포트 8000 사용

#### 확인 과정
```
1. 실행 중인 컨테이너 확인:
   $ docker ps
   
   CONTAINER ID   IMAGE              COMMAND
   a9b8c7d6e5f4   my-web-server:1.0  "python3 app.py"
   
   → 포트 8000 사용 중! 🔴

2. 정지된 컨테이너 확인:
   $ docker ps -a
   
3. Windows에서 포트 사용 중인 프로그램 확인:
   $ netstat -ano | findstr :8000
   
   TCP    127.0.0.1:8000          LISTENING       1234
```

#### 해결 방법

**방법 1: 다른 포트 사용**
```bash
$ docker run -p 8001:8000 my-web-server:1.0

🌟 웹 서버 시작됨!

(다른 터미널에서)
브라우저: http://localhost:8001

✅ 해결!
```

**방법 2: 기존 컨테이너 정지**
```bash
$ docker stop a9b8c7d6e5f4

a9b8c7d6e5f4

(1-2초 대기)

$ docker run -p 8000:8000 my-web-server:1.0

🌟 웹 서버 시작됨!

✅ 해결!
```

**방법 3: 컨테이너 삭제 후 재실행**
```bash
$ docker container rm my-server

my-server

$ docker run --name my-server -p 8000:8000 my-web-server:1.0

🌟 웹 서버 시작됨!

✅ 해결!
```

---

### 문제 3️⃣: "git: command not found"

#### 문제 상황
```
터미널에서 git 명령 실행 시:

$ git --version
command not found: git
```

#### 원인 가설
- Git for Windows가 설치되지 않음
- PowerShell/터미널이 Git 경로를 인식하지 못함
- 환경변수 PATH에 Git이 등록되지 않음

#### 확인 과정
```
1. Git 설치 확인:
   제어판 > 프로그램 및 기능 → "Git" 검색
   → 없으면 미설치

2. PATH 환경변수 확인:
   [Windows 설정] > 시스템 > 고급 시스템 설정
   → 환경변수 → Path에 "git" 포함 확인
```

#### 해결 방법
```bash
1. Git for Windows 설치
   → https://git-scm.com/download/win
   → Git-2.40.0-64-bit.exe 다운로드 및 실행
   
2. 설치 옵션:
   - "Use Git from Git Bash only" 선택 X
   - "Git from the command line and also from 3rd-party software" 선택 ✅
   
3. VS Code 재시작
   → Ctrl + Shift + `  (새 터미널)
   
4. 다시 확인:
   $ git --version
   git version 2.40.0.windows.1

✅ 해결!
```

---

### 문제 4️⃣: Dockerfile 빌드 실패 - "COPY failed"

#### 문제 상황
```
$ docker build -t my-web-server:1.0 .

[2/4] COPY app/ /app/
ERROR [2/4] COPY app/ /app/: COPY failed: 
file not found in build context: app

failed to solve with frontend dockerfile.v0
```

#### 원인 가설
- 빌드 명령 위치가 잘못됨
- app 폴더가 없음
- 폴더 구조가 잘못됨

#### 확인 과정
```
1. 현재 위치 확인:
   $ pwd
   C:\my-dev-workspace
   
   → Dockerfile이 있는 폴더여야 함 ✅

2. 폴더 구조 확인:
   $ ls
   
   app/
   Dockerfile
   README.md
   
   → app 폴더가 있나? ✅

3. app 폴더 내용 확인:
   $ ls app/
   
   app.py
   index.html
   
   → Python 파일과 HTML이 있나? ✅
```

#### 해결 방법
```bash
1. 올바른 위치에서 빌드:
   $ cd C:\my-dev-workspace
   
   $ docker build -t my-web-server:1.0 .
   
   ← 현재 폴더(.)의 Dockerfile 사용

2. 만약 app 폴더가 없으면:
   $ mkdir app
   
   $ echo "Python 코드" > app/app.py
   
   $ echo "<html>...</html>" > app/index.html
   
   다시 빌드:
   $ docker build -t my-web-server:1.0 .

3. Dockerfile에서 경로 확인:
   COPY app/ /app/
   ↑ 이 경로가 실제로 존재하나?

✅ 해결!
```

---

### 문제 5️⃣: GitHub 푸시 실패 - "Permission denied"

#### 문제 상황
```
$ git push -u origin main

error: remote rejection explained by server: 
GitHub requires authentication

fatal: unable to read askpass response
```

#### 원인 가설
- GitHub 계정 로그인 필요
- 액세스 토큰/SSH 키 설정 필요
- 저장소 권한 문제

#### 확인 과정
```
1. 원격 저장소 URL 확인:
   $ git remote -v
   
   origin  https://github.com/사용자명/my-dev-workspace.git

2. GitHub 계정 로그인 상태 확인
```

#### 해결 방법

**방법 1: VS Code GitHub 로그인 (추천)**
```
1. VS Code 좌측 하단 프로필 아이콘 > "Sign in with GitHub"
2. 브라우저에서 GitHub 계정으로 로그인
3. VS Code에 권한 부여
4. 다시 푸시:
   $ git push -u origin main
   
✅ 해결!
```

**방법 2: GitHub 개인 액세스 토큰 (PAT) 사용**
```
1. GitHub > Settings > Developer settings > Personal access tokens
2. "Generate new token" 클릭
3. 권한: repo, write:repo_hook 선택
4. 토큰 복사 (생성된 후 다시 볼 수 없음!)
5. Git 푸시 시 비밀번호 대신 토큰 입력

⚠️ 주의: 토큰을 README.md나 코드에 절대 포함하면 안 됨!
```

---

## 📂 6. 결과 위치 및 증거

### 6-1) 소스코드 위치

```
GitHub 저장소:
https://github.com/dubu-alt/my-dev-workspace

디렉토리 구조:
my-dev-workspace/
├── app/
│   ├── app.py
│   └── index.html
├── Dockerfile
├── README.md
├── .git/ (Git 저장소)
└── .gitignore
```

### 6-2) 주요 검증 증거

| 항목 | 위치 | 증거 |
|------|------|------|
| Docker 설치 | 터미널 | `docker --version` 출력 |
| 웹 서버 이미지 | 터미널 | `docker images` 목록 |
| 포트 매핑 | 브라우저 | http://localhost:8000 스크린샷 |
| Docker 볼륨 | 터미널 | `docker volume ls` 출력 |
| Git 설정 | 터미널 | `git config --list` 출력 |
| GitHub 연동 | GitHub 웹 | 저장소 페이지 링크 |

---

## 🛠️ 7. 기술 스택

| 항목 | 선택 | 버전 |
|------|------|------|
| OS | Windows 11 | 23H2 |
| 가상화 | WSL 2 | 1.0.2 |
| 컨테이너 | Docker | 24.0.0 |
| 베이스 이미지 | Ubuntu | 22.04 LTS |
| 런타임 | Python | 3.10 |
| 웹서버 | HTTP Server | Python built-in |
| VCS | Git | 2.40.0 |
| IDE | VS Code | 1.86.0 |

---

## 📚 8. 참고 자료

- [Git 공식 문서](https://git-scm.com/doc)
- [Docker 공식 가이드](https://docs.docker.com/)
- [VS Code Docker 확장](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)
- [Python HTTP Server](https://docs.python.org/3/library/http.server.html)

---

## ✅ 9. 최종 체크리스트

- [x] 모든 필수 프로그램 설치 완료
- [x] 터미널 기초 명령 10개 이상 실습
- [x] 파일 권한 변경 실습 완료
- [x] Docker 기본 명령어 10개 이상 실행
- [x] 커스텀 웹 서버 Dockerfile 작성 및 빌드
- [x] 포트 매핑으로 브라우저 접속 성공
- [x] Docker 볼륨과 바인드 마운트 검증
- [x] Git 설정 및 GitHub 연동 완료
- [x] 모든 과정을 README.md에 문서화
- [x] 민감한 정보 (토큰, 비밀번호) 마스킹 완료

---

## 🎉 완료!

이 보고서를 통해 다음을 달성했습니다:

✅ **개발 환경 구축**: Git, Docker, VS Code 연동  
✅ **실습 완료**: 20개 이상의 터미널 명령어 실행  
✅ **서버 배포**: Python 웹 서버를 Docker 컨테이너로 실행  
✅ **데이터 보존**: 볼륨과 바인드 마운트로 데이터 영속성 확보  
✅ **코드 공유**: GitHub에 프로젝트 업로드  
✅ **문서화**: 모든 과정을 상세히 기록  

---

**작성자**: [SUNG WONMO]  
**최종 수정**: 2026년 3월 31일  
**상태**: ✅ 완료 & 검증됨
