from fastapi import FastAPI
from app.routers import survey
from app.database import init_db

app = FastAPI(title="Survey API")

app.include_router(survey.router)

@app.on_event("startup")
def on_startup():
    init_db() 