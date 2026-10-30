from fastapi import FastAPI, HTTPException

from models.task_model import TaskDTO, Task

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
    return HTTPException(status_code=404, detail="Task not found")

@app.get("/tasks")
def get_tasks(skip: int = 0, limit: int = 10):
    return tasks_db[skip:skip+limit]

#TODO Homework: add delete and update tasks by id functionalities

@app.get("/health")
async def health():
    return {"status": "ok"}