from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, init_db
from .db_utils import log_prohibited_action, list_prohibited_actions

app = FastAPI()


@app.on_event("startup")
def on_startup() -> None:
    """Initialize database tables."""
    init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/prohibited-actions")
def create_prohibited_action(description: str, performed_by: str | None = None, db: Session = Depends(get_db)):
    action = log_prohibited_action(db, description, performed_by)
    return {
        "id": action.id,
        "description": action.description,
        "timestamp": action.timestamp,
        "performed_by": action.performed_by,
    }


@app.get("/prohibited-actions")
def get_prohibited_actions(limit: int = 100, db: Session = Depends(get_db)):
    actions = list_prohibited_actions(db, limit)
    return actions
