import pytest
from fastapi.testclient import TestClient

from main import app
from routes.routes import tasks_db


@pytest.fixture(autouse=True)
def clear_tasks():
    """Keep tests independent of each other's in-memory task data."""
    tasks_db.clear()
    yield
    tasks_db.clear()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def create_task(client, title="Test task", description="Test description"):
    return client.post("/tasks/", json={"title": title, "description": description})


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task(client):
    response = create_task(client)
    assert response.status_code == 200
    task = response.json()
    assert isinstance(task["id"], int)
    assert task["id"] >= 1
    assert task["title"] == "Test task"
    assert task["description"] == "Test description"
    assert task["is_completed"] is False


def test_create_task_invalid_title(client):
    response = create_task(client, title="ab")
    assert response.status_code == 422
    assert "detail" in response.json()
    assert tasks_db == []


def test_get_task(client):
    task_id = create_task(client).json()["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id


def test_get_missing_task(client):
    response = client.get("/tasks/999999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}


def test_get_tasks_pagination(client):
    for i in range(3):
        create_task(client, title=f"Task {i}")
    response = client.get("/tasks/?skip=1&limit=1")
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Task 1"


def test_update_task(client):
    task_id = create_task(client).json()["id"]
    response = client.put(
        f"/tasks/{task_id}",
        json={"title": "Updated task", "description": "Updated description"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": task_id,
        "title": "Updated task",
        "description": "Updated description",
        "is_completed": False,
    }


def test_update_preserves_completion_status(client):
    task_id = create_task(client).json()["id"]
    tasks_db[0].is_completed = True
    response = client.put(f"/tasks/{task_id}", json={"title": "Updated task"})
    assert response.status_code == 200
    assert response.json()["is_completed"] is True


def test_update_missing_task(client):
    response = client.put("/tasks/999999999", json={"title": "Updated task"})
    assert response.status_code == 404


def test_delete_task(client):
    task_id = create_task(client).json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted"}
    assert client.get(f"/tasks/{task_id}").status_code == 404


def test_delete_missing_task(client):
    response = client.delete("/tasks/999999999")
    assert response.status_code == 404