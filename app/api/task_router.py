from fastapi import APIRouter
from mcp_project.app.models.models import Task

task_router = APIRouter()

@task_router.post("/tasks/")
async def create_task(task: Task):
    result = run_task_agent(task)
    return {"msg": "Task created!", "agent_result": result}

@task_router.get("/tasks/")
async def list_tasks():
    # 추후 DB로 대체할 수 있는 메모리 저장소
    return [{"title": "Test Task", "status": "Pending"}]

@task_router.put("/tasks/{task_id}")
async def update_task_status(task_id: int, status: str):
    # 실제 DB 연동 전 stub 처리
    return {"msg": f"Task {task_id} updated to {status}"}
