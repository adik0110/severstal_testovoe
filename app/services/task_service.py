from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRepository
from app.db import schemas

class TaskService:
    def __init__(self, db: Session):
        self.repo = TaskRepository(db)

    def create_task(self, task: schemas.TaskCreate):
        return self.repo.create(task)

    def get_tasks(self):
        return self.repo.get_all()

    def get_task(self, task_id: int):
        return self.repo.get_by_id(task_id)

    def update_task(self, task_id: int, task: schemas.TaskUpdate):
        return self.repo.update(task_id, task)

    def delete_task(self, task_id: int):
        return self.repo.delete(task_id)
