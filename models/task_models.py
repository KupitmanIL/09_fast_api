from pydantic import BaseModel, Field

class Task(BaseModel):
    id: int = Field(..., ge=1)
    title: str
    description: str | None = None
    is_completed: bool = False

class TaskDTO(BaseModel):
    title: str = Field(..., min_length=3, max_length=20)
    description: str | None = None