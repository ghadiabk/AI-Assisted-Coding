# Task Tracker — Mid-Course Project

A full-stack task management application featuring a **FastAPI** backend and a **Vanilla JavaScript** Kanban board frontend. Extended as part of the AI-Assisted Coding Mid-Course Project to include task tagging/categorization and dynamic multi-parameter search and filtering.

---

## Technical Stack & Features
* **Backend:** Python 3.12+, FastAPI, Pydantic v2 validation, in-memory JSON file persistence.
* **Frontend:** Vanilla HTML5/CSS3/JavaScript (ES6+), Native HTML5 Drag-and-Drop, debounced live filter bar, modal form workflows.
* **Testing:** `pytest` and `httpx.TestClient` test suite.

---

## Getting Started

### 1. Prerequisites & Virtual Environment Setup

Clone the repository and navigate to the project directory:
```bash
git checkout mid-course-project
```

### Create and activate a Python virtual environment:

## On Windows (PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

## On macOS / Linux:

python3 -m venv venv
source venv/bin/activate

### Install project dependencies:

pip install -r requirements.txt

### Running the Backend Server

## Start the FastAPI backend with hot-reloading enabled on port 8000:

uvicorn app.main:app --reload --port 8000

### Verify that the server is running by opening:
Health Check: http://localhost:8000/health (Should return HTTP 200 {"status": "ok", ...})
Interactive API Docs (Swagger UI): http://localhost:8000/docs

### Opening the Frontend Interface

## With the backend server running in your terminal:
## Locate frontend/index.html in your workspace.
## Open the file in your web browser:
## Recommended: Use the Live Server extension in VS Code (served at http://127.0.0.1:5500 or http://localhost:5500).
## Alternative: Double-click frontend/index.html to open it directly in Google Chrome, Microsoft Edge, or Firefox.
## Note: Ensure the backend remains active on http://localhost:8000 while interacting with the frontend board.


### Running the Test Suite

## Execute the complete automated test suite (includes base CRUD, validation, status transition rules, tags, and search query tests):

pytest tests/ -v

## Running Specific Test Groups
# Run only the tag validation tests:

pytest tests/ -k "tags" -v

# Run only the status transition tests:

pytest tests/ -k "transition" -v


## Technical Decisions
* [Architecture Decision: In-Memory Storage Layer](docs/decisions/in-memory-storage.md)