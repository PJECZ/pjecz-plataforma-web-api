"""
Abogados v2, esquemas de pydantic
"""
from datetime import date
from typing import List
from pydantic import BaseModel

from ...schemas.datatable import DataTableResponse


class AbogadoOut(BaseModel):
    """Esquema para entregar abogados"""

    id: int
    fecha: date
    libro: str
    numero: str
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class AbogadoDataTableResponse(DataTableResponse):
    """Esquema para entregar abogados"""

    data: List[AbogadoOut] = []
