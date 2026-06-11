from typing import List
from uuid import uuid4
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.employee_log_schema import TipoAcao
from src.schemas.employee_schema import Employee
from src.models.employee_model import EmployeeModel
from src.repositories.employee_repository import EmployeeRepository
from src.repositories.log_repository import LogRepository
from src.database.db import get_db

employee_router = APIRouter()
employee_repository = EmployeeRepository()
log_repository = LogRepository("employee")

@employee_router.post("/", response_model=Employee)
def create_employee(employee: Employee, db: Session = Depends(get_db)):
    db_employee = EmployeeModel(
        id=str(uuid4()),
        nome=employee.nome,
        endereco=employee.endereco,
        ramal=employee.ramal,
        emailProfissional=employee.emailProfissional,
        departamento=employee.departamento,
        salario=employee.salario,
        dataAdmissao=employee.dataAdmissao
    )
    return employee_repository.add(db_employee, db)

@employee_router.get("/{id}", response_model=Employee)
def read_employee(id: str, db: Session = Depends(get_db)):
    emp = employee_repository.get_by_id(id, db)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return emp

@employee_router.put("/{id}", response_model=Employee)
def update_employee(id: str, employee: Employee, db: Session = Depends(get_db)):
    emp = employee_repository.get_by_id(id, db)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee_repository.update(id, employee, db)

@employee_router.delete("/{id}", response_model=Employee)
def delete_employee(id: str, db: Session = Depends(get_db)):
    emp = employee_repository.get_by_id(id, db)
    if not emp:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    response = Employee.model_validate(emp)
    
    employee_repository.remove(emp, db)
    return response

@employee_router.get("/", response_model=List[Employee])
def list_employees(db: Session = Depends(get_db)):
    employees = employee_repository.list_all(db)
    log_repository.add({
        "PartitionKey": "list",
        "RowKey": str(uuid4()),
        "tipo_acao": TipoAcao.LIST.value
    })
    return employees