import uuid

from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class EmployeeModel(Base):
    __tablename__ = "employees"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    nome = Column(String(100), nullable=False)
    endereco = Column(String(255), nullable=False)
    ramal = Column(String(20), nullable=False)
    emailProfissional = Column(String(255), nullable=False)
    departamento = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    dataAdmissao = Column(DateTime, nullable=False)