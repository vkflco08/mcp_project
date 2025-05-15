from fastapi import FastAPI
from app.api.task_router import task_router

app = FastAPI()

# 태스크 관련 라우터 등록
app.include_router(task_router)

@app.get("/")
def read_root():
    return {"message": "Hello from MCP!"}
