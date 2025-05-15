from app.models.models import Task
from app.utils.task_agent_graph import get_task_agent_graph
from app.utils.chroma_client import collection
from uuid import uuid4
from sentence_transformers import SentenceTransformer

graph = get_task_agent_graph()
embedder = SentenceTransformer("all-MiniLM-L6-v2")

def run_task_agent(task: Task):
    input_state = {
        "task": {
            "title": task.title,
            "description": task.description
        }
    }
    
    result = graph.invoke(input_state)

    summary = result.get("analysis")
    steps = result.get("steps", [])

    # ▶ 임베딩 생성 및 저장
    content = f"{task.title}\n{task.description}\n{summary}\n{str(steps)}"
    embedding = embedder.encode(content).tolist()
    doc_id = str(uuid4())

    collection.add(
        ids=[doc_id],
        documents=[content],
        embeddings=[embedding],
        metadatas=[{
            "title": task.title,
            "status": "completed"
        }]
    )

    return {
        "summary": summary,
        "steps": steps,
        "chroma_id": doc_id
    }