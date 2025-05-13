from fastapi import FastAPI
from app.api import task_router  # 태스크 관련 API를 처리하는 라우터

app = FastAPI()

# 태스크 관련 라우터 등록
app.include_router(task_router)
