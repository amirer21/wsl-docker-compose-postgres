# WSL Ubuntu에서 Docker 및 PostgreSQL 설치 및 연결 방법

## 목차
1. WSL 설정 및 Docker 설치
2. Docker 네트워크 생성 및 Docker 시작
3. Docker Compose 설정 및 컨테이너 빌드
4. PostgreSQL 컨테이너 관리
5. PostgreSQL에 연결하기
6. PostgreSQL 데이터베이스 덤프 및 복구
7. DBeaver에서 PostgreSQL 연결
8. 문제 해결

---

### 1. WSL 설정 및 Docker 설치

WSL 2를 설치하고 기본 버전으로 설정합니다.

```powershell
# PowerShell 관리자 권한으로 실행
wsl --set-default-version 2
```

리눅스 커널 업데이트 패키지를 설치합니다. WSL 2 Linux 커널 업데이트 패키지를 다운로드하여 설치합니다.

기존 배포판을 WSL 2로 변환합니다.

# PowerShell 관리자 권한으로 실행
```
wsl --list --verbose
wsl --set-version <Distro> 2
```

2. Docker 네트워크 생성 및 Docker 시작
WSL 터미널에서 Docker를 설치하고 네트워크를 생성합니다.

# Docker 그룹 추가
```
sudo groupadd docker
sudo usermod -aG docker $USER
```

# Docker 네트워크 생성
```
sudo docker network create docker_images_default
```

# Docker 시작
```
sudo service docker start
```

# Docker 데몬 디버깅 모드로 시작
```
sudo dockerd --debug
```

3. Docker Compose 설정 및 컨테이너 빌드

# 이미지 YML 파일 경로로 이동
```
cd /mnt/c/Users/amirer/docker_images
```

# Docker Compose 빌드 및 시작
```
docker-compose up -d
```

# 상태 확인
```
sudo docker ps
```

# 로그 출력
```
sudo docker logs -f <container_id_or_name>
```

4. PostgreSQL 컨테이너 관리

# PostgreSQL 컨테이너 중지
```
sudo docker stop postgres_container
```

# PostgreSQL 컨테이너 이름 변경
```
sudo docker rename postgres_container my_postgres
```

# 컨테이너 재시작
```
sudo docker start my_postgres
```

5. PostgreSQL에 연결하기
PostgreSQL 클라이언트를 설치하고 데이터베이스 서버에 연결합니다.

# PostgreSQL 클라이언트 설치
```
sudo apt-get install postgresql-client
```

# 데이터베이스 서버에 연결
```
psql -h <docker_host_ip> -p <port> -U <username> -d <database>

psql -h localhost -p 5432 -U hong -d testdb
```

# Docker 컨테이너 내부에서 연결
```
sudo docker exec -it my_postgres /bin/bash

psql -U hong -d testdb
```

6. PostgreSQL 데이터베이스 덤프 및 복구

# 덤프 파일 복사
```
sudo docker cp /mnt/c/Users/amirer/docker_images/testdb.sql my_postgres:/testdb.sql
```

# 데이터베이스 덤프 생성

# sudo docker exec -t my_postgres pg_dump -U hong -d testdb > /mnt/c/Users/amirer/docker_images/testdb.sql

# 덤프 파일을 데이터베이스에 적용
```
sudo docker exec -it my_postgres /bin/bash
psql -U hong -d testdb -f /mnt/c/Users/amirer/docker_images/testdb.sql
```

7. DBeaver에서 PostgreSQL 연결

# Docker IP 매핑 확인
```
sudo docker ps
```

# 호스트 IP 확인
```
hostname -I
```

DBeaver에 다음 정보를 입력합니다.

Host: 172.0.0.4 (호스트 머신의 실제 네트워크 인터페이스 IP 주소)
Port: 5432
Database: testdb
Username: hong
Password: 1111

8. 문제 해결
브리지 네트워킹 오류가 발생할 경우, WSL 2로 업그레이드해야 합니다.

# 모듈 로드 시도
```
sudo modprobe bridge
```

# 오류 발생 시 WSL 2로 업그레이드 필요
업그레이드 후 Docker 및 PostgreSQL을 다시 설정하여 문제를 해결합니다.

