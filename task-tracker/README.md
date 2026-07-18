# Task Tracker API

A simple task management REST API built with FastAPI.

## Quick Start

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
venv\Scripts\activate.bat
```

**On macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Server
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### 5. View API Documentation
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

### 6. Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "ok",
  "timestamp": "2024-01-10T15:30:45.123456"
}
```

## API Endpoints (Module 1 - Foundation Only)

- `GET /health` - Health check
- `GET /` - Root/welcome endpoint
- `GET /docs` - Swagger documentation

## Project Structure

```
task-tracker/
├── app/
│   ├── main.py           # FastAPI application entry point
│   ├── models/           # Pydantic data models
│   ├── api/routes/       # API endpoints (organized by resource)
│   ├── core/             # Configuration and utilities
│   └── storage/          # Data persistence layer
├── tests/                # Test files
├── requirements.txt      # Python dependencies
├── REQUIREMENTS.md       # Project requirements and user stories
├── ARCHITECTURE.md       # Architecture decision record
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore patterns
└── README.md             # This file
```

## Architecture

This module uses **FastAPI + in-memory storage with JSON file persistence** for learning purposes. 

**Key decisions:**
- No database in Module 1 (adds unnecessary complexity)
- In-memory dict backed by JSON file (simple, testable, file-backed)
- Pydantic models for automatic validation
- RESTful API design

See [ARCHITECTURE.md](ARCHITECTURE.md) for full architecture decision rationale.

## Next Steps

Module 2 and beyond will add:
- Full CRUD endpoints for tasks
- SQL database integration
- Authentication
- Real-time updates
- Frontend UI

## Testing

```bash
pytest tests/
```

## Development

Run with live reload:
```bash
uvicorn app.main:app --reload
```

Run with specific host/port:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```
