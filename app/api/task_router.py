from fastapi import APIRouter
from app.models.models import Task

task_router = APIRouter()

# 간단한 in-memory 저장소 (임시)
TASK_DB = []
TASK_ID_SEQ = 1

@task_router.post("/tasks/")
async def create_task(task: Task):
    global TASK_ID_SEQ
    task.id = TASK_ID_SEQ
    TASK_ID_SEQ += 1
    TASK_DB.append(task)
    result = run_task_agent(task)
    return {"msg": "Task created!", "task": task, "agent_result": result}

@task_router.get("/tasks/")
async def list_tasks():
    return TASK_DB

@task_router.put("/tasks/{task_id}")
async def update_task_status(task_id: int, status: str):
    for task in TASK_DB:
        if task.id == task_id:
            task.status = status
            return {"msg": f"Task {task_id} updated to {status}", "task": task}
    return {"error": f"Task {task_id} not found"}