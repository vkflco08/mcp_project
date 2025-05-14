from fastapi import FastAPI
from mcp_project.app.api import task_router

app = FastAPI()

# 태스크 관련 라우터 등록
app.include_router(task_router)
