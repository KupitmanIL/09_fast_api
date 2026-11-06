# Task Management REST API

A lightweight REST API for task management built with **Python, FastAPI, and Pydantic**.

The project demonstrates CRUD operations, request validation, HTTP exception handling, middleware-based logging, and API documentation.

## Features

* Create new tasks
* Retrieve a task by ID
* Retrieve a paginated list of tasks
* Update existing tasks
* Delete tasks
* Validate incoming requests using Pydantic
* Handle HTTP errors
* Log HTTP requests and responses
* Interactive API documentation with Swagger UI

## Tech Stack

* Python 3.10+
* FastAPI
* Pydantic
* Uvicorn
* Pytest
* HTTPX

## Project Structure

```text
09_fast_api/
├── loggers/
│   └── logger_req.py
├── models/
│   └── task_models.py
├── routes/
│   └── routes.py
├── tests/
│   └── test_tasks.py
├── main.py
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/KupitmanIL/09_fast_api.git
cd 09_fast_api
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

On Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

## API Endpoints

| Method | Endpoint           | Description                    |
| ------ | ------------------ | ------------------------------ |
| GET    | `/health`          | Check application health       |
| POST   | `/tasks/`          | Create a task                  |
| GET    | `/tasks/`          | Retrieve tasks with pagination |
| GET    | `/tasks/{task_id}` | Retrieve a task by ID          |
| PUT    | `/tasks/{task_id}` | Update a task                  |
| DELETE | `/tasks/{task_id}` | Delete a task                  |

### Create a Task

**POST** `/tasks/`

Example request:

```json
{
  "title": "Learn FastAPI",
  "description": "Build a REST API"
}
```

Example response:

```json
{
  "id": 1000,
  "title": "Learn FastAPI",
  "description": "Build a REST API",
  "is_completed": false
}
```

### Get Tasks

**GET** `/tasks/?skip=0&limit=10`

Returns a list of tasks with pagination.

### Update a Task

**PUT** `/tasks/1000`

Example request:

```json
{
  "title": "Study FastAPI",
  "description": "Improve API development skills"
}
```

The existing task ID and completion status are preserved.

### Delete a Task

**DELETE** `/tasks/1000`

Example response:

```json
{
  "message": "Task deleted"
}
```

## Validation and Error Handling

The API uses Pydantic models for request validation.

Task titles must contain between **3 and 20 characters**.

The application returns:

* `404 Not Found` when a requested task does not exist.
* `422 Unprocessable Entity` when request validation fails.

## API Documentation

FastAPI automatically generates interactive API documentation.

After starting the application, open:

* **Swagger UI:** `http://127.0.0.1:8000/docs`
* **ReDoc:** `http://127.0.0.1:8000/redoc`

## Data Storage

Tasks are stored in an in-memory Python list.

**Important:** Data is not persisted between application restarts.

This project focuses on REST API fundamentals rather than database integration.

## Testing

The project includes **11 automated tests** using Pytest and FastAPI TestClient.

Tests cover:

* Task creation and validation
* Retrieving tasks by ID
* Task pagination
* Task updates
* Preservation of task completion status
* Task deletion
* HTTP 404 error handling
* Health endpoint

### Install Development Dependencies

```bash
pip install -r requirements-dev.txt
```

### Run Tests

From the project root directory, execute:

```bash
python -m pytest tests/ -v
```

The test suite contains 11 tests covering the application's core functionality.

## Project Status

Educational project demonstrating backend development fundamentals with FastAPI.

The application includes CRUD operations, request validation, HTTP error handling, logging middleware, interactive API documentation, and automated tests.
