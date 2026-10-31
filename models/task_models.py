from pydantic import BaseModel

class Task(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_completed: bool = False

class TaskDTO(BaseModel):
    title: str
    description: str | None = None