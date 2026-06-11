from datetime import datetime
from enum import Enum
from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field, ConfigDict

class TipoAcao(str, Enum):
    CREATE = "Create"
    UPDATE = "Update"
    DELETE = "Delete"
    LIST = "List"
    READ = "Read"

class EmployeeLog(BaseModel):
    tipo_acao: TipoAcao = Field(..., description="Tipo de ação ao modificar o employee")
    PartitionKey: str = Field(..., min_length=1, max_length=50)
    RowKey: UUID = Field(default_factory=uuid4, description="Unique identifier for the log entry")

    model_config = ConfigDict(validate_by_name=True)