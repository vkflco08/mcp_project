from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    status: str  # e.g., "Pending", "In Progress", "Completed"