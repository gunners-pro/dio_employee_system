from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, ConfigDict, EmailStr, Field, model_validator

class Employee(BaseModel):
    id: Optional[UUID] = Field(default_factory=uuid4, description="Unique identifier for the employee")
    nome: str = Field(..., min_length=6, max_length=100)
    endereco: str = Field(..., min_length=6, max_length=255)
    ramal: str = Field(..., min_length=1, max_length=20)
    emailProfissional: EmailStr
    departamento: str = Field(..., min_length=6, max_length=50)
    salario: float = Field(..., gt=0)
    dataAdmissao: datetime = Field(...)

    @model_validator(mode='before')
    @classmethod
    def validate_employee(cls, values):
        if isinstance(values, dict):
            nome = values.get('nome', '')
            endereco = values.get('endereco', '')
            ramal = values.get('ramal', '')
            departamento = values.get('departamento', '')
        else:
            nome = getattr(values, 'nome', '')
            endereco = getattr(values, 'endereco', '')
            ramal = getattr(values, 'ramal', '')
            departamento = getattr(values, 'departamento', '')

        if not nome.strip():
            raise ValueError("Nome cannot be empty or contain only whitespace")
        if not endereco.strip():
            raise ValueError("Endereço cannot be empty or contain only whitespace")
        if not ramal.strip():
            raise ValueError("Ramal cannot be empty or contain only whitespace")
        if not departamento.strip():
            raise ValueError("Departamento cannot be empty or contain only whitespace")

        return values

    model_config = ConfigDict(validate_by_name=True)