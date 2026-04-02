# ⚡ Windows + Mac + Linux 명령어 치트시트

> **모든 OS에서 사용할 수 있는 명령어 정리!** 🖥️🍎🐧

---

## 🎯 OS별 특징

| OS | 터미널 | 파일시스템 | 권한 시스템 | chmod |
|----|--------|----------|-----------|-------|
| **Windows** | PowerShell / Git Bash | NTFS | ACL | ❌ (무시됨) |
| **Mac** | Terminal / Zsh | APFS / HFS+ | Unix 권한 | ✅ (작동) |
| **Linux** | Bash / Zsh | ext4 / ext3 | Unix 권한 | ✅ (작동) |

---

## 📂 파일 & 폴더 명령어

### 기본 조회

#### Windows
```powershell
pwd                    # 현재 위치 확인
ls                     # 파일 목록 (짧은 형식)
ls -la                 # 파일 목록 (상세, 숨김 포함)
dir                    # 파일 목록 (Windows 방식)
dir /a                 # 숨김 파일 포함
```

#### Mac / Linux
```bash
pwd                    # 현재 위치 확인
ls                     # 파일 목록 (짧은 형식)
ls -la                 # 파일 목록 (상세, 숨김 포함)
ls -lh                 # 파일 크기 보기 좋게
ll                     # ls -l의 별칭 (Mac/Linux)
tree                   # 폴더 구조 트리 형식 (설치 필요)
```

---

### 이동 & 생성

#### Windows & Mac & Linux (공통)
```bash
cd folder-name         # 폴더 이동
cd ..                  # 상위 폴더로
cd ~                   # 홈 폴더로
cd /                   # 루트로
mkdir my-folder        # 폴더 생성
```

#### Mac & Linux만
```bash
touch file.txt         # 파일 생성 (빈 파일)
mktemp                 # 임시 파일 생성
```

#### Windows PowerShell
```powershell
New-Item -ItemType File -Name "file.txt"    # 파일 생성
New-Item -ItemType Directory -Name "folder" # 폴더 생성
```

---

### 파일 내용

#### Windows & Mac & Linux (공통)
```bash
cat file.txt           # 파일 내용 보기
```

#### Windows만
```powershell
type file.txt          # 파일 내용 보기
cat file.txt           # (Git Bash에서도 가능)
```

#### Mac & Linux만
```bash
less file.txt          # 페이지 단위로 보기 (q로 나가기)
more file.txt          # 페이지 단위로 보기 (Space로 다음)
head -n 10 file.txt    # 처음 10줄만 보기
tail -n 10 file.txt    # 마지막 10줄만 보기
wc -l file.txt         # 줄 수 세기
```

#### 파일 생성 및 내용 입력

##### Windows
```powershell
echo "content" > file.txt   # 파일 생성 및 내용 입력
echo "content" >> file.txt  # 파일에 내용 추가
```

##### Mac & Linux
```bash
echo "content" > file.txt   # 파일 생성 및 내용 입력
echo "content" >> file.txt  # 파일에 내용 추가
cat > file.txt << EOF       # 여러 줄 입력 (Ctrl+D로 저장)
line 1
line 2
EOF
```

---

### 복사 & 이동 & 삭제

#### Windows PowerShell
```powershell
cp source.txt dest.txt              # 파일 복사
cp -r folder/ new-folder/           # 폴더 복사
move file.txt newname.txt           # 파일 이름 변경
mv file.txt newname.txt             # 파일 이동/이름 변경
rm file.txt                         # 파일 삭제
rm -r folder/                       # 폴더 삭제
del file.txt                        # 파일 삭제 (Windows 방식)
rmdir folder                        # 빈 폴더 삭제
```

#### Mac & Linux (Linux 표준)
```bash
cp source.txt dest.txt              # 파일 복사
cp -r folder/ new-folder/           # 폴더 복사
cp -i source.txt dest.txt           # 덮어쓰기 전 확인
mv file.txt newname.txt             # 파일 이동/이름 변경
mv -i file.txt newname.txt          # 덮어쓰기 전 확인
rm file.txt                         # 파일 삭제
rm -r folder/                       # 폴더 삭제
rm -i file.txt                      # 삭제 전 확인
rmdir folder                        # 빈 폴더 삭제
```

---

## 🔐 권한 (Permission) 명령어

### 확인 (모두 같음)

```bash
ls -l file.txt         # 파일 권한 확인
ls -ld folder          # 폴더 권한 확인
stat file.txt          # 상세 정보 (Mac/Linux)
```

### 변경

#### Mac & Linux ✅
```bash
chmod +x file.txt      # 실행 권한 추가
chmod -w file.txt      # 쓰기 권한 제거
chmod 755 file.txt     # 권한 설정 (rwx r-x r-x)
chmod 644 file.txt     # 권한 설정 (rw- r-- r--)
chmod u+x file.txt     # 소유자에게 실행 권한
chmod g+r file.txt     # 그룹에게 읽기 권한
chmod o-x file.txt     # 기타에서 실행 권한 제거
```

#### Windows PowerShell ⚠️
```powershell
# chmod는 안 됩니다! (NTFS이므로)
# 대신 이렇게 사용:

Set-ItemProperty -Path "file.txt" -Name IsReadOnly -Value $true
Get-Item -Path "file.txt" | Select-Object IsReadOnly

# 또는 icacls 명령어:
icacls "file.txt" /grant Users:F
```

---

## 🐳 Docker 명령어 (모두 동일)

### 버전 & 정보

```bash
docker --version       # Docker 버전
docker info            # Docker 상세 정보
docker stats           # 리소스 사용량
```

### 이미지 관리

```bash
docker images          # 설치된 이미지 목록
docker pull ubuntu     # 이미지 다운로드
docker build -t my-app:1.0 .   # Dockerfile로 이미지 빌드
docker rmi image-id    # 이미지 삭제
docker inspect image-id  # 이미지 상세 정보
docker tag old-name new-name   # 이미지 태그 변경
```

### 컨테이너 실행

```bash
docker run ubuntu                    # 컨테이너 실행 후 종료
docker run -it ubuntu bash          # 상호작용 모드 (터미널 진입)
docker run -d nginx                 # 백그라운드에서 실행
docker run --name my-server -p 8000:8000 my-app:1.0
                                    # 이름 지정 + 포트 매핑
docker run --name my-server \
  -p 8000:8000 \
  -v my-volume:/data \
  -e ENV_VAR=value \
  my-app:1.0                       # 복합 옵션
```

### 컨테이너 조회

```bash
docker ps              # 실행 중인 컨테이너
docker ps -a           # 모든 컨테이너 (중지된 것도)
docker ps -q           # 컨테이너 ID만 출력
docker ps -a | grep my-app   # 특정 컨테이너 찾기
```

### 컨테이너 제어

```bash
docker stop container-id       # 컨테이너 중지
docker start container-id      # 중지된 컨테이너 시작
docker restart container-id    # 컨테이너 재시작
docker rm container-id         # 컨테이너 삭제
docker pause container-id      # 컨테이너 일시 정지
docker unpause container-id    # 일시 정지 해제
docker kill container-id       # 강제 종료
```

### 컨테이너 접근

```bash
docker exec -it container-id bash       # 컨테이너 셸 진입
docker exec -it container-id sh         # Alpine 등 경량 이미지용
docker logs container-id                # 로그 확인
docker logs -f container-id             # 실시간 로그
docker logs --tail 50 container-id      # 마지막 50줄
docker top container-id                 # 실행 중인 프로세스
docker stats container-id               # 리소스 사용량
docker cp file.txt container-id:/app/   # 파일 복사 (호스트 → 컨테이너)
docker cp container-id:/app/file.txt .  # 파일 복사 (컨테이너 → 호스트)
```

### 볼륨 (Volume)

```bash
docker volume create my-volume          # 볼륨 생성
docker volume ls                        # 볼륨 목록
docker volume inspect my-volume         # 볼륨 상세 정보
docker volume rm my-volume              # 볼륨 삭제

# 실행 시 볼륨 연결
docker run -v my-volume:/app my-image

# 바인드 마운트 (로컬 폴더 연결)
docker run -v /local/path:/container/path my-image
```

### 정리

```bash
docker container prune          # 중지된 모든 컨테이너 삭제
docker image prune              # 사용 안 하는 이미지 삭제
docker system prune             # 사용 안 하는 모든 것 삭제
docker system df                # Docker 디스크 사용량
```

---

## 📝 Git 명령어 (모두 동일)

### 설정

```bash
git config --global user.name "이름"
git config --global user.email "이메일"
git config --list              # 설정 확인
git config user.name           # 특정 설정만 보기
```

### 저장소

```bash
git init                        # 새 저장소 생성
git clone url                   # 저장소 복제
git status                      # 상태 확인
git log                         # 커밋 히스토리
git log --oneline               # 간단한 히스토리
git log --graph --oneline --all # 브랜치 시각화
```

### 커밋

```bash
git add file.txt                # 파일 추가
git add .                       # 모든 변경사항 추가
git commit -m "메시지"          # 커밋
git commit -am "메시지"         # 추적 중인 파일 자동 추가 + 커밋
git push origin main            # GitHub에 푸시
git pull origin main            # GitHub에서 가져오기
```

### 브랜치

```bash
git branch                      # 브랜치 목록
git branch new-branch           # 브랜치 생성
git checkout new-branch         # 브랜치 전환
git switch new-branch           # 브랜치 전환 (최신)
git merge other-branch          # 브랜치 병합
git branch -d new-branch        # 브랜치 삭제
```

### 원격 저장소

```bash
git remote -v                   # 원격 저장소 목록
git remote add origin url       # 원격 저장소 추가
git remote remove origin        # 원격 저장소 제거
git push -u origin main         # 첫 푸시 (-u: upstream 설정)
git pull                        # 최신 코드 가져오기
```

### 복구

```bash
git diff                        # 변경사항 비교
git checkout file.txt           # 파일 변경사항 취소
git reset HEAD file.txt         # 스테이징 취소
git revert commit-id            # 커밋 되돌리기
git stash                       # 임시 저장
git stash pop                   # 임시 저장한 것 복구
```

---

## 🎯 실용적인 조합 명령어

### Mac & Linux에서 새 프로젝트 시작

```bash
# 프로젝트 폴더 생성
mkdir my-project
cd my-project

# Git 초기화
git init
git config user.name "이름"
git config user.email "이메일"

# 폴더 구조 생성
mkdir app src tests
touch README.md .gitignore

# Git 커밋
git add .
git commit -m "초기 설정"
```

### Windows PowerShell에서 새 프로젝트 시작

```powershell
# 프로젝트 폴더 생성
mkdir my-project
cd my-project

# Git 초기화
git init
git config user.name "이름"
git config user.email "이메일"

# 폴더 구조 생성
mkdir app, src, tests
New-Item -ItemType File -Name "README.md"
New-Item -ItemType File -Name ".gitignore"

# Git 커밋
git add .
git commit -m "초기 설정"
```

### Docker 이미지 빌드 및 실행

```bash
# 1. Dockerfile 위치 확인
pwd

# 2. 이미지 빌드
docker build -t my-app:1.0 .

# 3. 빌드 확인
docker images | grep my-app

# 4. 컨테이너 실행
docker run --name my-server -p 8000:8000 -v my-volume:/data my-app:1.0

# 5. 실행 확인 (다른 터미널)
docker ps

# 6. 로그 확인
docker logs my-server
```

### 컨테이너에 파일 복사

```bash
# 호스트 → 컨테이너
docker cp file.txt my-server:/app/

# 컨테이너 → 호스트
docker cp my-server:/app/file.txt ./local-file.txt
```

---

## 💻 Mac 특화 명령어

### 시스템 정보

```bash
system_profiler SPSoftwareDataType    # 시스템 정보
uname -a                             # OS 정보
sw_vers                              # macOS 버전
```

### 프로세스 관리

```bash
ps aux                               # 실행 중인 프로세스
top                                  # 실시간 프로세스 모니터링
kill -9 pid                          # 강제 종료
lsof -i :8000                        # 포트 8000 사용 확인
```

### 패키지 관리 (Homebrew)

```bash
brew install nodejs                  # 패키지 설치
brew list                            # 설치된 패키지
brew uninstall nodejs                # 패키지 제거
brew update                          # Homebrew 업데이트
brew upgrade                         # 패키지 업그레이드
```

### 파일 권한 (GUI)

```bash
# 터미널에서 파일 속성 열기
open -a Finder file.txt

# 그 후 [Command+I] 또는 우클릭 > 정보 > 공유 및 권한
```

---

## 🪟 Windows PowerShell 특화 명령어

### 프로세스 관리

```powershell
Get-Process                          # 실행 중인 프로세스
Stop-Process -Name process_name      # 프로세스 종료
Get-NetTCPConnection -LocalPort 8000 # 포트 사용 확인
```

### 파일 권한

```powershell
Get-Item file.txt | Select-Object IsReadOnly
Set-ItemProperty -Path "file.txt" -Name IsReadOnly -Value $true
icacls "file.txt" /grant Users:F     # ACL 설정
```

### 패키지 관리 (Chocolatey)

```powershell
choco install nodejs                 # 패키지 설치
choco list                           # 설치된 패키지
choco uninstall nodejs               # 패키지 제거
choco upgrade all                    # 모든 패키지 업그레이드
```

---

## 📖 도움말 명령어 (모두 동일)

```bash
docker --help                   # Docker 도움말
docker run --help               # 특정 명령어 도움말
git --help                      # Git 도움말
man ls                          # 상세 매뉴얼 (Mac/Linux)
help ls                         # 도움말 (PowerShell)
```

---

## 🎓 OS별 권장 터미널

| OS | 권장 | 대안 |
|----|------|------|
| **Windows** | PowerShell | Git Bash, WSL |
| **Mac** | Terminal (기본) | iTerm2, Hyper |
| **Linux** | Bash (기본) | Zsh, Fish |

---

## 📊 명령어 호환성 표

| 명령어 | Windows | Mac | Linux | 비고 |
|--------|---------|-----|-------|------|
| `pwd` | ✅ Git Bash | ✅ | ✅ | 위치 확인 |
| `ls` | ✅ Git Bash | ✅ | ✅ | 파일 목록 |
| `mkdir` | ✅ | ✅ | ✅ | 폴더 생성 |
| `chmod` | ❌ | ✅ | ✅ | 권한 변경 |
| `docker` | ✅ | ✅ | ✅ | 컨테이너 |
| `git` | ✅ | ✅ | ✅ | 버전 관리 |

---

## 💡 마지막 팁

### 1️⃣ 명령어 자동완성
- **Mac/Linux**: Tab 키
- **PowerShell**: Tab 키 (좌우 화살표로 선택)

### 2️⃣ 명령어 히스토리
- **모두**: ↑↓ 화살표 키
- **Mac/Linux**: Ctrl+R로 검색

### 3️⃣ 긴 명령어 작성
```bash
# Mac/Linux: \ 로 줄 바꿈
docker run \
  --name my-app \
  -p 8000:8000 \
  my-image:1.0

# PowerShell: ` (백틱) 로 줄 바꿈
docker run `
  --name my-app `
  -p 8000:8000 `
  my-image:1.0
```

---

**북마크하고 필요할 때마다 참고하세요!** 📌

