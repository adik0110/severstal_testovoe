from pydantic import BaseModel

from app.db.models import TaskStatus


class TaskBase(BaseModel):
    title: str
    status: TaskStatus = TaskStatus.active

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
