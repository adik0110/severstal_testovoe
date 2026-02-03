from sqlalchemy.orm import Session
from app.db import models, schemas

class TaskRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, task: schemas.TaskCreate) -> models.Task:
        db_task = models.Task(title=task.title, status=task.status)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def get_all(self):
        return self.db.query(models.Task).all()

    def get_by_id(self, task_id: int):
        return self.db.query(models.Task).filter(models.Task.id == task_id).first()

    def update(self, task_id: int, task: schemas.TaskUpdate):
        db_task = self.get_by_id(task_id)
        if db_task:
            db_task.title = task.title
            db_task.status = task.status
            self.db.commit()
            self.db.refresh(db_task)
        return db_task

    def delete(self, task_id: int):
        db_task = self.get_by_id(task_id)
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
        return db_task
