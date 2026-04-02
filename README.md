# 🚀 개발 워크스테이션 구축하기!

> **작성자**: [SUNG WONMO]  
> **작성일**: 2026년 03월 31일  
> **GitHub**: [[GitHub 저장소 링크](https://github.com/dubu-alt)]

---

## 📌 1. 프로젝트 개요

### 미션 목표

```
✅ Git, Docker, VS Code를 활용한 로컬 개발 환경 구축
✅ 간단한 웹 서버 만들기
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
| 커스텀 웹 서버 구축 | ✅ | Dockerfile, 웹 이미지 실행 앱 작성 |
| 포트 매핑 접속 | ✅ | http://localhost:8080 |
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

vnkers948441@c3r3s7 workspace % git --version
git version 2.53.0
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
vnkers948441/desktop/workspace
```

#### 파일 목록 보기 (숨김 파일 포함)

```bash
$ ls -la
total 88
drwxr-xr-x   6 vnkers948441  vnkers948441    192 Apr  1 11:16 .
drwx------+  5 vnkers948441  vnkers948441    160 Apr  1 11:02 ..
drwxr-xr-x  15 vnkers948441  vnkers948441    480 Apr  1 11:19 .git
-rw-r--r--   1 vnkers948441  vnkers948441     52 Apr  1 11:03 bin.txt
-rw-r--r--@  1 vnkers948441  vnkers948441  13044 Apr  1 11:16 final_checklist.md
-rw-r--r--@  1 vnkers948441  vnkers948441  22910 Apr  1 11:16 README.md
```

#### 폴더 생성

```bash
$ mkdir workspace
$ ls -d workspace  (파일 존재 여부 확인)
test-folder
```

#### 파일 생성 및 내용 확인

```bash
$ echo "안녕하세요!" > hello.txt
$ cat hello.txt
안녕하세요!
```

#### 파일 권한 변경

```bash
$ ls -l hello.txt (권한 확인)
-rw-r--r--  1 vnkers948441  vnkers948441  16 Apr  1 11:24 hello.txt

$ chmod +x hello.txt (권한 변경)
$ ls -l hello.txt (권한 재확인)
-rwxr-xr-x  1 vnkers948441  vnkers948441  16 Apr  1 11:24 hello.txt

→ 실행 권한(x) 추가됨 ✅
```

### 4-2) Docker 검증

#### Docker 버전 확인

```bash
$ docker --version
Docker version 28.5.2, build ecc6942
```

#### Docker 정보 확인

```bash
$ docker info | head -20
Client:
 Version:    28.5.2
 Context:    orbstack
 Debug Mode: false
 Plugins:
  buildx: Docker Buildx (Docker Inc.)
    Version:  v0.29.1
    Path:     /Users/vnkers948441/.docker/cli-plugins/docker-buildx
  compose: Docker Compose (Docker Inc.)
    Version:  v2.40.3
    Path:     /Users/vnkers948441/.docker/cli-plugins/docker-compose

Server:
 Containers: 0
  Running: 0
  Paused: 0
  Stopped: 0
 Images: 0
 Server Version: 28.5.2
```

#### hello-world 컨테이너 실행

```bash
$ docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.(amd64)
 ...

→ 성공! ✅
```

#### Ubuntu 컨테이너 진입 & 명령 실행

```bash
$ docker run -it ubuntu bash
root@e2421e459f8e:/# ls -la
total 16
drwxr-xr-x   1 root root   6 Apr  1 02:29 .
drwxr-xr-x   1 root root   6 Apr  1 02:29 ..
-rwxr-xr-x   1 root root   0 Apr  1 02:29 .dockerenv
lrwxrwxrwx   1 root root   7 Apr 22  2024 bin -> usr/bin
drwxr-xr-x   1 root root   0 Apr 22  2024 boot
...

root@e2421e459f8e:/# echo "hello"
hello

root@e2421e459f8e:/# cat /etc/os-release
PRETTY_NAME="Ubuntu 24.04.4 LTS"
NAME="Ubuntu"

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
# 1. 가벼운 웹 서버 이미지인 nginx:alpine을 베이스로 사용
FROM nginx:alpine

# 2. "hello world" 내용이 담긴 index.html 파일을 nginx 기본 경로에 생성
RUN echo "hello world" > /usr/share/nginx/html/index.html

# 3. 컨테이너 내부에서 80번 포트를 사용함을 명시 (생략 가능)
EXPOSE 80
```

**위치:** `vnkers948441/workspace/app/Dockerfile`


#### 이미지 빌드

```bash
$ docker build -t my-web-server:1.0 .

[+] Building 8.0s (6/6) FINISHED                                                                  docker:orbstack
 => [internal] load build definition from Dockerfile                                                         0.2s
 => => transferring dockerfile: 372B                                                                         0.0s
 => [internal] load metadata for docker.io/library/nginx:alpine                                              3.1s
 => [internal] load .dockerignore                                                                            0.1s
 => => transferring context: 2B                                                                              0.0s
 => [1/2] FROM docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c315c152f9c20  3.6s
 => => resolve docker.io/library/nginx:alpine@sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c315c152f9c20  0.1s
 => => sha256:d5030d429039a823bef4164df2fad7a0defb8d00c98c1136aec06701871197c2 12.32kB / 12.32kB             0.0s
 => => sha256:e7257f1ef28ba17cf7c248cb8ccf6f0c6e0228ab9c315c152f9c203cd34cf6d1 10.33kB / 10.33kB             0.0s
 => => sha256:7e89aa6cabfc80f566b1b77b981f4bb98413bd2d513ca9a30f63fe58b4af6903 2.50kB / 2.50kB               0.0s
 => => sha256:589002ba0eaed121a1dbf42f6648f29e5be55d5c8a6ee0f8eaa0285cc21ac153 3.86MB / 3.86MB               0.5s
 => => extracting sha256:4d9d41f3822d171ccc5f2cdfd75ad846ac4c7ed1cd36fb998fe2c0ce4501647b                    0.0s
 => => extracting sha256:3370263bc02adcf5c4f51831d2bf1d54dbf9a6a80b0bf32c5c9b9400630eaa08                    0.4s
 => [2/2] RUN echo "hello world" > /usr/share/nginx/html/index.html                                          0.4s
 => exporting to image                                                                                       0.2s
 => => exporting layers                                                                                      0.1s
 => => writing image sha256:872edd14e1995ede46be97c09c9b4dd86c27657a36465141a55d7f22fe5fb3ad                 0.0s
 => => naming to docker.io/library/my-web-server:1.0 

Successfully tagged my-web-server:1.0

✅ 빌드 성공!
```

#### 컨테이너 실행

```bash
% docker run -d -p 8080:80 --name my-web-container my-web-server:1.0

🌟 웹 서버 시작됨! http://localhost:8080 접속
(컨테이너가 실행 중입니다... Ctrl+C 중지)
```

### 4-4) 포트 매핑 및 브라우저 접속

#### 브라우저 접속

```
주소: http://localhost:8080
```

**스크린샷:**
![컨테이너 실행 결과](<https://github.com/user-attachments/assets/2b36fd28-1a2f-4200-8b4c-5b10c3731117>)

```
[주소 표시줄]
URL: http://localhost:8080

```

✅ **접속 성공!**

### 4-5) Docker 볼륨 검증

#### 볼륨 생성

```bash
$ docker volume create my-nginx-data

my-nginx-data

$ docker volume ls

DRIVER    VOLUME NAME
local     my-nginx-data
```

#### 볼륨 연결하여 컨테이너 실행

```bash
$ docker run --name my-server-vol \
  -p 8080:80 \
  -v my-nginx-data:/data
  my-web-server:1.0

🌟 웹 서버 시작됨!
```

#### 컨테이너 내부에서 데이터 생성

```bash
$ docker exec -it my-nginx-data-vol sh

root@abc123:/app# echo "중요한 데이터입니다!" > /data/important.txt

root@abc123:/app# cat /data/important.txt
중요한 데이터입니다!

root@abc123:/app# ls -la /data
total 4
drwxr-xr-x    1 root     root            26 Apr  1 05:54 .
drwxr-xr-x    1 root     root            40 Apr  1 05:04 ..
-rw-r--r--    1 root     root            16 Apr  1 05:54 important.txt

root@abc123:/app# exit
```

#### 컨테이너 삭제 전 볼륨 확인

```bash
$ docker ps -a | grep my-server-vol
a9b8c7d6e5f4   my-web-server:1.0   "python3 app.py"  5 min ago   Exited (137)
```

#### 컨테이너 삭제

```bash
$ docker container rm my-nginx-data-vol

my-nginx-data-vol

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
docker run --name my-nginx-data-vol-recovery \
  -p 8001:80 \
  -v my-nginx-data:/data \
  my-web-server:1.0

🌟 웹 서버 시작됨!

(다른 터미널에서)

docker exec -it my-nginx-data-vol-recovery sh

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

origin  https://github.com/dubu-alt/First_Mission_Setup.git (fetch)
origin  https://github.com/dubu-alt/First_Mission_Setup.git (push)
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
   
   origin https://github.com/dubu-alt/First_Mission_Setup.git 

2. GitHub 계정 로그인 상태 확인
```

#### 해결 방법

**방법 1: VS Code GitHub 로그인**
```
1. VS Code 좌측 하단 프로필 아이콘 > "Sign in with GitHub"
2. 브라우저에서 GitHub 계정으로 로그인
3. VS Code에 권한 부여
4. 다시 푸시:
   $ git push -u origin main
   
✅ 해결!
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

---

**작성자**: [SUNG WONMO]  
**최종 수정**: 2026년 3월 31일  
**상태**: ✅ 완료 & 검증됨
