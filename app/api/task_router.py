from fastapi import APIRouter
from app.models import Task

task_router = APIRouter()

@task_router.post("/tasks/")
async def create_task(task: Task):
    # 태스크 생성 로직 (예: LangGraph Agent 호출)
    return {"msg": "Task created successfully!", "task": task}