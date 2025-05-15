from fastapi import APIRouter
from pydantic import BaseModel
from app.utils.llm import call_gpt_review  # 추후 구현
import os

code_router = APIRouter()

class CodeReviewRequest(BaseModel):
    file_path: str

@code_router.post("/code-review/")
def review_code(request: CodeReviewRequest):
    file_path = request.file_path

    if not os.path.exists(file_path):
        return {"error": "File not found."}

    with open(file_path, "r") as f:
        content = f.read()

    suggestion = call_gpt_review(content)
    return {"suggestion": suggestion}