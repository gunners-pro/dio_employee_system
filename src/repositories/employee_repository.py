from typing import List, Optional
from sqlalchemy.orm import Session

from src.schemas.employee_schema import Employee
from src.models.employee_model import EmployeeModel

class EmployeeRepository:
    def get_by_id(self, id: str, db: Session) -> Optional[EmployeeModel]:
        return db.query(EmployeeModel).filter(EmployeeModel.id == id).first()
    
    def add(self, employee: EmployeeModel, db: Session) -> EmployeeModel:
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee
    
    def update(self, id: str, employee: Employee, db: Session) -> Optional[EmployeeModel]:
        emp = db.query(EmployeeModel).filter(EmployeeModel.id == id).first()
        if not emp:
            return None

        emp.nome = employee.nome
        emp.endereco = employee.endereco
        emp.ramal = employee.ramal
        emp.emailProfissional = employee.emailProfissional
        emp.departamento = employee.departamento
        emp.salario = employee.salario
        emp.dataAdmissao = employee.dataAdmissao

        db.commit()
        db.refresh(emp)
        return emp

    def remove(self, employee: EmployeeModel, db: Session):
        db.delete(employee)
        db.commit()

    def list_all(self, db: Session) -> List[EmployeeModel]:
        return db.query(EmployeeModel).all()