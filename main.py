from fastapi import FastAPI

from src.routes.employee_router import employee_router

app = FastAPI()
app.include_router(employee_router, prefix="/employees", tags=["employees"])