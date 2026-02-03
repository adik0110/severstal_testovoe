import enum

from sqlalchemy import Column, Integer, String, Enum
from app.db.database import Base


class TaskStatus(str, enum.Enum):
    active = "active"
    completed = "completed"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.active, nullable=False)
