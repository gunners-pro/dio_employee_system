from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.schemas.employee_schema import Employee
from src.repositories.employee_repository import EmployeeRepository
from src.database.db import get_db

employee_router = APIRouter()
employee_repository = EmployeeRepository()

@employee_router.post("/", response_model=Employee)
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    employee_repository.add(employee, db)
    return employee

@employee_router.get("/{id}", response_model=Employee)
def read_employee(id: str, db: Session = Depends(get_db)):
    employee = employee_repository.get_by_id(id, db)
    return employee

@employee_router.put("/{id}", response_model=Employee)
def update_employee(id: str, employee: Employee, db: Session = Depends(get_db)):
    return employee_repository.update(employee, id, db)

@employee_router.delete("/{id}", response_model=Employee)
def delete_employee(id: str, db: Session = Depends(get_db)):    
    return employee_repository.remove(id, db)

@employee_router.get("/", response_model=List[Employee])
def list_employees(db: Session = Depends(get_db)):
    return employee_repository.list_all(db)