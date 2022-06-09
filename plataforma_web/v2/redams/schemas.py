"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, esquemas de pydantic
"""
from datetime import date
from typing import List
from pydantic import BaseModel

from ...schemas.datatable import DataTableRequest, DataTableResponse


class RedamOut(BaseModel):
    """Esquema para entregar deudores"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    autoridad_clave: str
    nombre: str
    expediente: str
    fecha: date
    observaciones: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class RedamDataTableRequest(DataTableRequest):
    """Esquema para peticiones de datatable"""

    distrito_id: int = None
    autoridad_id: int = None
    nombre: str = None


class RedamDataTableResponse(DataTableResponse):
    """Esquema para entregar deudores"""

    aaData: List[RedamOut] = []
