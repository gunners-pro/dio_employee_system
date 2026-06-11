from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

class Employee(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4, description="Unique identifier for the employee")
    nome: str = Field(..., min_length=1, max_length=100)
    endereco: str = Field(..., min_length=1, max_length=255)
    ramal: str = Field(..., min_length=1, max_length=20)
    emailProfissional: EmailStr
    departamento: str = Field(..., min_length=1, max_length=50)
    salario: float = Field(..., gt=0)
    dataAdmissao: datetime = Field(...)

    @model_validator(mode='before')
    def validate_employee(cls, values):
        if not values['nome'].strip():
            raise ValueError("Nome cannot be empty or contain only whitespace")
        if not values['endereco'].strip():
            raise ValueError("Endereço cannot be empty or contain only whitespace")
        if not values['ramal'].strip():
            raise ValueError("Ramal cannot be empty or contain only whitespace")
        if not values['departamento'].strip():
            raise ValueError("Departamento cannot be empty or contain only whitespace")
        return values

    model_config = ConfigDict(validate_by_name=True)