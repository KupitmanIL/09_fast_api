from fastapi import FastAPI, HTTPException

from models.task_models import TaskDTO, Task

app = FastAPI()

tasks_db = []

@app.post("/tasks")
def create_task(task_dto: TaskDTO):
    task = Task(title=task_dto.title, description=task_dto.description, id=len(tasks_db))
    tasks_db.append(task)
    return task

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return tasks_db[skip:skip+limit]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            tasks_db.remove(task)
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task_dto: TaskDTO):
    for task in tasks_db:
        if task.id == task_id:
            task.title = task_dto.title
            task.description = task_dto.description
            return task
    raise HTTPException(status_code=404, detail="Task not found")

