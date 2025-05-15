# utils/agent_runner.py
from app.models.models import Task

def run_task_agent(task: Task):
    # LangGraph 연동 전에 stub 반환
    task_analysis = {
        "title": task.title,
        "summary": f"Summary of: {task.description}",
        "steps": [
            "Step 1: 이해",
            "Step 2: 처리",
            "Step 3: 완료 저장"
        ]
    }
    return {"agent_result": task_analysis}
