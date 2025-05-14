# utils/agent_runner.py
from mcp_project.app.models.models import Task

def run_task_agent(task: Task):
    # LangGraph 연동 전에 stub 반환
    return {"result": "Stub result from LangGraph"}