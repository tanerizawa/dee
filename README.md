# Dear Diary

This repository contains experimental code and documentation for the **Dear Diary** AI counseling concept. The PRD outlines a journaling companion that analyzes daily entries and responds with supportive guidance.

## Tech Stack

### Backend
- **Python + FastAPI** for a lightweight API layer.
- **SQLite with SQLAlchemy** for simple local persistence.

### Mobile Client
- **Kotlin + Jetpack Compose** for a modern Android interface.

## High-Level Architecture
1. The Android app sends journal entries to the FastAPI server.
2. The server processes text with AI models and returns advice.
3. Data storage and user authentication are handled on the backend.

## Development Phases
The project roadmap includes several stages. See [docs/fase1-system-design.md](docs/fase1-system-design.md)
for details about the first phase covering system design and architecture.

## Getting Started

### Clone the repository
```bash
git clone <REPO_URL>
cd dee
```

### Python environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The API uses a local SQLite database located at `data.db`. Tables are created
automatically on startup.

### Android environment
1. Install Android Studio with SDK tools and a recent Kotlin setup.
2. Open the project in Android Studio or run Gradle from the command line.

### Running the application
- **Backend**
  ```bash
  uvicorn app.main:app --reload
  ```
- **Android app**
  ```bash
  cd android-app
  ./gradlew installDebug
  adb shell am start -n com.example.diary/.MainActivity
  ```

These commands assume the backend lives in `app/` and the Android project in `android-app/`.

### Working with the database

`app.db_utils` exposes helper functions to log and query prohibited actions.
Example:

```python
from app.database import SessionLocal
from app.db_utils import log_prohibited_action

db = SessionLocal()
log_prohibited_action(db, "Attempted restricted feature", performed_by="user42")
db.close()
```

Use the `/prohibited-actions` endpoints to create and fetch entries via the API.

## License
MIT
