from sqlalchemy.orm import Session

from .models import ProhibitedAction


def log_prohibited_action(db: Session, description: str, performed_by: str | None = None) -> ProhibitedAction:
    action = ProhibitedAction(description=description, performed_by=performed_by)
    db.add(action)
    db.commit()
    db.refresh(action)
    return action


def list_prohibited_actions(db: Session, limit: int = 100):
    return db.query(ProhibitedAction).order_by(ProhibitedAction.timestamp.desc()).limit(limit).all()
