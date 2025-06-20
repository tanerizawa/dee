from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime

from .database import Base

class ProhibitedAction(Base):
    __tablename__ = "prohibited_actions"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    performed_by = Column(String, nullable=True)
