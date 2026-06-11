from src.schemas.employee_schema import Employee
from typing import List, Optional

class EmployeeRepository:
    def __init__(self):
        self._employees: List[Employee] = []

    def get_by_id(self, id: str) -> Optional[Employee]:
        for emp in self._employees:
            if emp.id == id:
                return emp
        return None
    
    def add(self, employee: Employee):
        self._employees.append(employee)

    def remove(self, employee: Employee):
        self._employees.remove(employee)

    def list_all(self) -> List[Employee]:
        return self._employees