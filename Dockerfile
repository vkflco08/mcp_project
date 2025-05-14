# Dockerfile
FROM python:3.12-slim

# 필수 패키지 설치
RUN apt-get update && apt-get install -y build-essential

# 작업 디렉토리 설정
WORKDIR /app

# 종속성 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 코드 복사
COPY . .

# FastAPI 서버 실행
CMD ["uvicorn", "mcp_project.app.main:app", "--host", "0.0.0.0", "--port", "8000"]