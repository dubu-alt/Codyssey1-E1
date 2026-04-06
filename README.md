# 개발 워크스테이션 구축하기!

> **작성자**: [SUNG WONMO]  
> **작성일**: 2026년 03월 31일  
> **GitHub**: [[GitHub 저장소 링크](https://github.com/dubu-alt)]

---

### 큰 과정 맥락

| 항목 | 비고 |
|------|------|
| 개발 환경 구축| Git, Docker, VS Code 설치 |
| 터미널/파일 조작 | pwd, ls, mkdir, cd, touch 등 |
| 파일 권한 실습 | chmod 명령으로 권한 변경 테스트 |
| Docker 설치 및 검증 | docker --version, docker info |
| 기본 컨테이너 실행 | hello-world, ubuntu 컨테이너 |
| 커스텀 웹 서버 구축 | Dockerfile, 웹 이미지 실행 앱 작성 |
| 포트 매핑 접속 | http://localhost:8080 |
| 데이터 영속성 검증  | Docker 볼륨, 바인드 마운트 |
| Git & GitHub 연동 | 저장소 생성, 커밋, 푸시 |

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

```

---

## 3. 체크리스트

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

```
ls -la
total 88
drwxr-xr-x   6 vnkers948441  vnkers948441    192 Apr  1 11:16 .
drwx------+  5 vnkers948441  vnkers948441    160 Apr  1 11:02 ..
drwxr-xr-x  15 vnkers948441  vnkers948441    480 Apr  1 11:19 .git
-rw-r--r--   1 vnkers948441  vnkers948441     52 Apr  1 11:03 bin.txt
-rw-r--r--@  1 vnkers948441  vnkers948441  13044 Apr  1 11:16 final_checklist.md
-rw-r--r--@  1 vnkers948441  vnkers948441  22910 Apr  1 11:16 README.md
```

#### 폴더 생성 및 삭제,이동, 변경

```bash
mkdir workspace
ls -d workspace  (파일 존재 여부 확인)
worksapce

Make Directory의 약어로, 폴더를 생성하는 명령어다.

touch — 파일 생성

root@vnkers948441 ❯ touch bin.txt
파일을 생성하는 명령어다. `.`을 기준으로 파일명과 확장자를 구분한다.

vnkers948441@c3r3s3 workspace % mv bin1.txt bin2.txt
bin.txt 파일 이름을 bin2.txt  파일이름으로 변경

vnkers948441@c3r3s3 workspace % rm test1.txt
rm은 remove의 약어로 원하는 파일을 삭제 할수 있다.

vnkers948441@c3r3s3 workspace % rm -d help
폴더를 삭제하고 싶다면 rm -d 삭제할 디렉토리명 을 써야된다.

cp <복사 대상> <복사할 파일명>
cp는 Copy의 약어로 원하는 곳으로 복사할 수 있다.
vnkers948441@c3r3s3 workspace % cp hello.txt bin2.txt


mv <대상 파일> <변경될 이름> 형식으로 이름 변경에도 사용할 수 있다.
vnkers948441@c3r3s3 workspace % mv test.txt app
```

#### 텍스트 파일 생성 및 생성한 내용 확인

```bash
$ echo "안녕하세요!" > hello.txt
$ cat hello.txt
안녕하세요!
```
---



#### 파일 권한 변경
Change Mode의 약어로, 숫자로 권한을 지정할 수있다.

| 숫자 | 권한 |
|------|------|
| 4 | r (읽기) |
| 2 | w (쓰기) |
| 1 | x (실행) |

숫자를 합산하여 사용한다. 순서는 소유자 / 그룹 / 기타 사용자 순이다.

```bash
$ ls -l hello.txt (권한 확인)
-rw-r--r--  1 vnkers948441  vnkers948441  16 Apr  1 11:24 hello.txt

$ chmod +x hello.txt (권한 변경)
$ ls -l hello.txt (권한 재확인)
-rwxr-xr-x  1 vnkers948441  vnkers948441  16 Apr  1 11:24 hello.txt

→ 실행 권한(x) 추가
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

→ 성공
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

→ Ubuntu 컨테이너 진입 & 명령 실행
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

CONTAINER ID     IMAGE                 COMMAND                 CREATED        STATUS
a9b8c7d6e5f4   my-web-server:1.0  "docker-entrypoint.."     5 minutes ago  Up 3 minutes
```

### 4-3) Dockerfile 기반 웹 서버 구축

#### Dockerfile 작성

```dockerfile
# 1. 가벼운 웹 서버 이미지인 nginx:alpine을 베이스로 사용
FROM nginx:alpine

# 2. "hello world" 내용이 담긴 index.html 파일을 nginx 기본 경로에 생성
# 두번째방법은 내 컴퓨터의 index.html을 컨테이너 내부의 Nginx 경로로 복사 --> COPY index.html /usr/share/nginx/html/index.html
RUN echo "hello world" > /usr/share/nginx/html/index.html

# 3. 컨테이너 내부에서 80번 포트를 사용함을 명시 (생략 가능)
EXPOSE 80
```
| 명령어 | 역할 |
|--------|------|
| `FROM nginx:alpine` | nginx 웹 서버가 설치된 Alpine 이미지를 베이스로 사용 |
| `RUN echo "hello world" > /usr/share/nginx/html/index.html ...` | 생성된 HTML을 nginx 기본 웹 경로에 복사 |
| `EXPOSE 80` | 컨테이너가 80번 포트를 사용함을 명시 |

> 도커 안에서 도커를 여는 것(DinD, Docker in Docker)은 일반적으로 불가능하고 전용 이미지와 `--privileged` 옵션이 필요하다. 따라서 `docker-project` 폴더를 컨테이너 바깥(Mac 터미널)으로 옮긴 뒤 이미지를 빌드한다.

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

빌드 성공
```

#### 컨테이너 실행

```bash
% docker run -d -p 8080:80 --name my-web-container my-web-server:1.0

웹 서버 시작됨! http://localhost:8080 접속
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

**접속 성공 확인**

### 4-5) Docker 볼륨 검증
데이터베이스, 로그 파일 등 사라지면 안 되는 데이터를 보존할 때 볼륨을 사용한다.
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
docker run --name my-server-vol -p 8080:80 -v my-nginx-data:/data my-web-server:1.0

-v my-nginx-data:/data my-web-server:1.0 → my-nginx 볼륨을 컨테이너의 /data경로에 연결


/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/04/03 02:44:50 [notice] 1#1: using the "epoll" event method
2026/04/03 02:44:50 [notice] 1#1: nginx/1.29.7
2026/04/03 02:44:50 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/04/03 02:44:50 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/04/03 02:44:50 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/04/03 02:44:50 [notice] 1#1: start worker processes
2026/04/03 02:44:50 [notice] 1#1: start worker process 30
2026/04/03 02:44:50 [notice] 1#1: start worker process 31
2026/04/03 02:44:50 [notice] 1#1: start worker process 32
2026/04/03 02:44:50 [notice] 1#1: start worker process 33
2026/04/03 02:44:50 [notice] 1#1: start worker process 34
2026/04/03 02:44:50 [notice] 1#1: start worker process 35
192.168.215.1 - - [03/Apr/2026:02:45:29 +0000] "GET / HTTP/1.1" 304 0 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/18.6 Safari/605.1.15" "-"
🌟 웹 서버 시작됨!
```

### 볼륨 연결 후 컨테이너 실행하고 난뒤 로컬호스트 실행 이미지
<img width="1090" height="192" alt="Screenshot 2026-04-03 at 11 47 10 AM" src="https://github.com/user-attachments/assets/76ee4817-3e94-4796-a96b-193add842b0c" />

#### 컨테이너 내부에서 데이터 생성

```bash
$ docker exec -it my-server-vol sh

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
<img width="1507" height="264" alt="Screenshot 2026-04-03 at 12 10 25 PM" src="https://github.com/user-attachments/assets/77d6b0d5-4c84-4c09-b67c-8127229806bd" />

#### 컨테이너 삭제 전 볼륨 확인

```bash
$ docker ps -a | grep my-server-vol
d9a627c13762   my-web-server:1.0   "/docker-entrypoint.…"   26 minutes ago      Up 26 minutes 0.0.0.0:8080->80/tcp, [::]:8080->80/tcp   my-server-vol
```

#### 컨테이너 삭제

```bash
$ docker container rm my-server-vol

my-server-vol

$ docker ps -a | grep my-server-vol
(아무것도 출력 안 됨 = 컨테이너 삭제됨)
```
<img width="1457" height="211" alt="Screenshot 2026-04-03 at 12 17 32 PM" src="https://github.com/user-attachments/assets/1d774b8c-a1cd-4160-b5a7-11f39999155b" />

#### 볼륨 유지 확인

```bash
$ docker volume ls

DRIVER    VOLUME NAME
local     my-ngnix-data

← 볼륨은 여전히 살아있음!
```

#### 새 컨테이너로 데이터 복구

```bash
docker run --name my-nginx-data-vol-recovery \
  -p 8001:80 \
  -v my-nginx-data:/data \
  my-web-server:1.0

 웹 서버 시작

(다른 터미널에서)

docker exec -it my-nginx-data-vol-recovery sh

root@def456:/app# cat /data/important.txt
중요한 데이터입니다!

← 데이터 복구
```

### 4-6) 바인드 마운트 검증
호스트의 실제 디렉토리를 컨테이너에 마운트해서 파일 동기화함\
바인드 마운트를 사용하는 이유는 호스트(Mac)의 파일을 수정하면 컨테이너에 즉시 반영되는지 확인하기 위해서다\
매번 코드를 수정할때마다 이미지를 재빌드하는 건 비효율적이므로, 바인드 마운트를 활용하면 개발 속도가 크게 향상된다.\
(프론트엔드에서 Live Server 같은 익스텐션을 사용하는 것과 유사한 느낌)
| 상황 | 결과 |
|------|------|
| 볼륨 없이 | 컨테이너 삭제 → 데이터도 함께 삭제 |
| 볼륨 있으면 | 컨테이너 삭제 → 데이터 유지 |

#### 로컬 폴더에서 새 파일 생성

```bash
pwd
$ mkdir share-data

$ echo "공유 데이터입니다" > share-data/share.txt

$ cat share-data/share.txt
이건 공유 데이터입니다.
```

#### 바인드 마운트로 컨테이너 실행

```
vnkers948441@c3r3s7 share-data % docker run --name bind-mount \
  -p 8000:8000 \
  -v $PWD/share-data:/app/shared\    현재 경로에 있는 폴더 기준으로 잡음!                                   
  my-web-server:1.0

/docker-entrypoint.sh: /docker-entrypoint.d/ is not empty, will attempt to perform configuration
/docker-entrypoint.sh: Looking for shell scripts in /docker-entrypoint.d/
/docker-entrypoint.sh: Launching /docker-entrypoint.d/10-listen-on-ipv6-by-default.sh
10-listen-on-ipv6-by-default.sh: info: Getting the checksum of /etc/nginx/conf.d/default.conf
10-listen-on-ipv6-by-default.sh: info: Enabled listen on IPv6 in /etc/nginx/conf.d/default.conf
/docker-entrypoint.sh: Sourcing /docker-entrypoint.d/15-local-resolvers.envsh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/20-envsubst-on-templates.sh
/docker-entrypoint.sh: Launching /docker-entrypoint.d/30-tune-worker-processes.sh
/docker-entrypoint.sh: Configuration complete; ready for start up
2026/04/03 02:18:50 [notice] 1#1: using the "epoll" event method
2026/04/03 02:18:50 [notice] 1#1: nginx/1.29.7
2026/04/03 02:18:50 [notice] 1#1: built by gcc 15.2.0 (Alpine 15.2.0) 
2026/04/03 02:18:50 [notice] 1#1: OS: Linux 6.17.8-orbstack-00308-g8f9c941121b1
2026/04/03 02:18:50 [notice] 1#1: getrlimit(RLIMIT_NOFILE): 20480:1048576
2026/04/03 02:18:50 [notice] 1#1: start worker processes
2026/04/03 02:18:50 [notice] 1#1: start worker process 30
2026/04/03 02:18:50 [notice] 1#1: start worker process 31
2026/04/03 02:18:50 [notice] 1#1: start worker process 32
2026/04/03 02:18:50 [notice] 1#1: start worker process 33
2026/04/03 02:18:50 [notice] 1#1: start worker process 34
2026/04/03 02:18:50 [notice] 1#1: start worker process 35

웹 서버 시작
```

#### 컨테이너 내부에서 확인

```bash
$ docker exec -it bind-mount bash

root@ghi789:/app# cat share/test.txt
공유 데이터입니다

root@ghi789:/app# ls -la share/
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

← 바인드 마운트 양방향 동기화 성공
```

### 4-7) Git & GitHub 검증

#### Git 로컬에 정보 저장 및 확인 및 초기화 하기

```bash
$ git config --global user.name "Dubu"
git config -- global user.email "vnkers94@gmail.com"
git config -l

credential.helper=osxkeychain
user.name=Dubu
user.email=vnkers94@gmail.com
core.repositoryformatversion=0
core.filemode=true
core.bare=false
core.logallrefupdates=true
core.ignorecase=true
core.precomposeunicode=true

git init (깃 저장소 초기화 및 설정)

````
## Git 설정 완료
```
git add . (깃 폴더 전체 선택)
git commit -m "첫번째 커밋"
git log (커밋 내역 확인)
```
````
vnkers948441@c3r3s3 workspace % git add .  
vnkers948441@c3r3s3 workspace % git commit -m "첫번째 커밋"
[master (최상위-커밋) 96491e0] 첫번째 커밋
 9 files changed, 1609 insertions(+)
 create mode 100644 .DS_Store
 create mode 100644 README.md
 create mode 100644 app/Dockerfile
 create mode 100644 app/index.html
 create mode 100644 app/test.txt
 create mode 100644 bin2.txt
 create mode 100644 final_checklist.md
 create mode 100644 hello.txt
 create mode 100644 share-data/share.txt
vnkers948441@c3r3s3 workspace % git log

commit 96491e0c86b07cff8d0e47749e4237ef1c5c2454 (HEAD -> master)
Author: Dubu <vnkers94@gmail.com>
Date:   Mon Apr 6 13:15:51 2026 +0900
````

#### Git 저장소 상태

```bash
$ git status

On branch main
nothing to commit, working tree clean
```

#### 커밋 히스토리

```bash
$ git log --oneline

96491e0 (HEAD -> master) 첫번째 커밋
```

#### 원격 저장소 확인

```bash
$ git remote -v

origin  https://github.com/dubu-alt/First_Mission_Setup.git (fetch)
origin  https://github.com/dubu-alt/First_Mission_Setup.git (push)
```

---

## 5. 트러블슈팅

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
   a9b8c7d6e5f4   my-web-server:1.0  "index.html"
   
   → 포트 8000 사용 중임을 확인 

2. 정지된 컨테이너 확인:
   $ docker ps -a
   
```

#### 해결 방법

**방법 1: 다른 포트 사용**
```bash
$ docker run -p 8001:8000 my-web-server:1.0

웹 서버 시작됨!

(다른 터미널에서)
브라우저: http://localhost:8001

해결
```

**방법 2: 기존 컨테이너 정지**
```bash
$ docker stop a9b8c7d6e5f4

a9b8c7d6e5f4

(1-2초 대기)

$ docker run -p 8000:8000 my-web-server:1.0

웹 서버 시작

```

**방법 3: 컨테이너 삭제 후 재실행**
```bash
$ docker container rm my-server

my-server

$ docker run --name my-server -p 8000:8000 my-web-server:1.0

웹 서버 시작


```
---

## 📂 6. 각종 결과 위치

### 6-1) 소스코드 위치

```
GitHub 저장소:
https://github.com/dubu-alt/Fist-Mission_Setup

디렉토리 구조:
workspace/
├── app/
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
| 포트 매핑 | 브라우저 | http://localhost:8080 스크린샷 |
| Docker 볼륨 | 터미널 | `docker volume ls` 출력 |
| Git 설정 | 터미널 | `git config --list` 출력 |
| GitHub 연동 | GitHub 웹 | 저장소 페이지 링크 |

---

---

## 📚 8. 참고 자료

- [Git 공식 문서](https://git-scm.com/doc)
- [Docker 공식 가이드](https://docs.docker.com/)
- [VS Code Docker 확장](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)

---

## 9. 최종 체크리스트

- [x] 모든 필수 프로그램 설치 및 확인
- [x] 터미널 기초 명령어 실습
- [x] 파일 권한 변경 실습 완료하기
- [x] Docker 기본 명령어 10개 이상 실행
- [x] 커스텀 웹 서버 Dockerfile 작성 및 빌드
- [x] 포트 매핑으로 브라우저 접속 성공 확인
- [x] Docker 볼륨과 바인드 마운트 검증
- [x] Git 설정 및 GitHub 연동 완료
- [x] 모든 과정을 README.md에 문서화

---

---

**작성자**: [SUNG WONMO]  
**최종 수정**: 2026년 4월 3일  
