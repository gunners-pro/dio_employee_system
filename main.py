from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()

from src.routes.employee_router import employee_router
from src.database.db import engine
from src.models.employee_model import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(employee_router, prefix="/employees", tags=["employees"])