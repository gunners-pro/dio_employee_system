from typing import List, Optional
from sqlalchemy.orm import Session

from src.schemas.employee_schema import Employee

class EmployeeRepository:
    def __init__(self):
        pass

    def get_by_id(self, id: str, db: Session) -> Optional[Employee]:
        return db.query(Employee).filter(Employee.id == id).first()
    
    def add(self, employee: Employee, db: Session):
        db.add(employee)
        db.commit()
        db.refresh(employee)
        return employee
    
    def update(self, employee: Employee, id: str, db: Session):
        db.query(Employee).filter(Employee.id == id).update({
            Employee.nome: employee.nome,
            Employee.endereco: employee.endereco,
            Employee.ramal: employee.ramal,
            Employee.emailProfissional: employee.emailProfissional,
            Employee.departamento: employee.departamento,
            Employee.salario: employee.salario,
            Employee.dataAdmissao: employee.dataAdmissao
        })
        db.commit()
        return db.query(Employee).filter(Employee.id == id).first()

    def remove(self, employee: Employee, db: Session):
        db.delete(employee)
        db.commit()

    def list_all(self, db: Session) -> List[Employee]:
        return db.query(Employee).all()