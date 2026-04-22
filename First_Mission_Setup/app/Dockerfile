# 1. 가벼운 웹 서버 이미지인 nginx:alpine을 베이스로 사용
FROM nginx:alpine

# 2. "hello world" 내용이 담긴 index.html 파일을 nginx 기본 경로에 생성
RUN echo "hello world" > /usr/share/nginx/html/index.html

# 3. 컨테이너 내부에서 80번 포트를 사용함을 명시 (생략 가능)
EXPOSE 80
