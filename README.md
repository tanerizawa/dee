# Dear Diary

This repository contains experimental code and documentation for the **Dear Diary** AI counseling concept. The PRD outlines a journaling companion that analyzes daily entries and responds with supportive guidance.

## Tech Stack

### Backend
- **Python + FastAPI** for a lightweight API layer.

### Mobile Client
- **Kotlin + Jetpack Compose** for a modern Android interface.

## High-Level Architecture
1. The Android app sends journal entries to the FastAPI server.
2. The server processes text with AI models and returns advice.
3. Data storage and user authentication are handled on the backend.

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
pip install -r requirements.txt  # To be added
```

### Android environment
1. Install Android Studio with SDK tools and a recent Kotlin setup.
2. Open the project in Android Studio or run Gradle from the command line.

### Running the application
- **Backend**
  ```bash
  uvicorn app.main:app --reload  # Placeholder path
  ```
- **Android app**
  ```bash
  ./gradlew installDebug
  adb shell am start -n com.example.diary/.MainActivity
  ```

These commands are placeholders until the app code is added.

## License
MIT
