from fastapi import APIRouter, HTTPException
from itertools import count
from models.task_models import TaskDTO, Task

router = APIRouter(prefix="/tasks")

counter = count(start = 1000, step = 1000)
tasks_db = []

@router.post("/")
def create_task(task_dto: TaskDTO):
    task = Task(title=task_dto.title, description=task_dto.description, id=next(counter))
    tasks_db.append(task)
    return task

@router.get("/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    return HTTPException(status_code=404, detail="Task not found")

@router.get("/")
def get_tasks(skip: int = 0, limit: int = 10):
    return tasks_db[skip:skip+limit]

@router.delete("/{task_id}")
def delete_task(task_id: int):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            del tasks_db[idx]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")


@router.put("/{task_id}")
def update_task(task_id: int, task_dto: TaskDTO):
    for idx, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[idx] = Task(title=task_dto.title, description=task_dto.description, id=task_id)
            return tasks_db[idx]
    raise HTTPException(status_code=404, detail="Task not found")