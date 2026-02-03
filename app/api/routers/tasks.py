from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_task_service(db: Session = Depends(database.get_db)):
    return TaskService(db)

@router.post("/", response_model=schemas.Task)
def create_task(task: schemas.TaskCreate, service: TaskService = Depends(get_task_service)):
    return service.create_task(task)

@router.get("/", response_model=list[schemas.Task])
def list_tasks(service: TaskService = Depends(get_task_service)):
    return service.get_tasks()

@router.get("/{task_id}", response_model=schemas.Task)
def get_task(task_id: int, service: TaskService = Depends(get_task_service)):
    db_task = service.get_task(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.put("/{task_id}", response_model=schemas.Task)
def update_task(task_id: int, task: schemas.TaskUpdate, service: TaskService = Depends(get_task_service)):
    db_task = service.update_task(task_id, task)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task

@router.delete("/{task_id}", response_model=schemas.Task)
def delete_task(task_id: int, service: TaskService = Depends(get_task_service)):
    db_task = service.delete_task(task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
