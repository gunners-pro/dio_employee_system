from typing import List
from fastapi import APIRouter

from src.schemas.schemas import Employee
from src.repositories.employee_repository import EmployeeRepository

employee_router = APIRouter()
employee_repository = EmployeeRepository()

@employee_router.post("/", response_model=Employee)
def create_employee(employee: Employee):
    employee_repository.add(employee)
    return employee

@employee_router.get("/{id}", response_model=Employee)
def read_employee(id: str):
    employee = employee_repository.get_by_id(id)
    return employee

@employee_router.put("/{id}", response_model=Employee)
def update_employee(id: str, employee: Employee):
    emp = employee_repository.get_by_id(id)
    emp.nome = employee.nome
    emp.endereco = employee.endereco
    emp.ramal = employee.ramal
    emp.emailProfissional = employee.emailProfissional
    emp.departamento = employee.departamento
    emp.salario = employee.salario
    emp.dataAdmissao = employee.dataAdmissao
    return emp

@employee_router.delete("/{id}", response_model=Employee)
def delete_employee(id: str):
    emp = employee_repository.get_by_id(id)
    employee_repository.remove(emp)
    return emp

@employee_router.get("/", response_model=List[Employee])
def list_employees():
    return employee_repository.list_all()