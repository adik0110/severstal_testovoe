from fastapi import FastAPI
from app.db.database import Base, engine
from app.api.routers import tasks

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tasks API")

app.include_router(tasks.router)
