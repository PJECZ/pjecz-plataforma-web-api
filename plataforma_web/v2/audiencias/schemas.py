"""
Audiencias v2, esquemas de pydantic
"""
from datetime import datetime
from typing import List
from pydantic import BaseModel

from ...schemas.datatable import DataTableResponse


class AudienciaOut(BaseModel):
    """Esquema para entregar audiencias"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_id: int
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    tiempo: datetime
    tipo_audiencia: str
    expediente: str
    actores: str
    demandados: str
    sala: str
    caracter: str
    causa_penal: str
    delitos: str
    toca: str
    expediente_origen: str
    imputados: str
    origen: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True


class AudienciaDataTableReponse(DataTableResponse):
    """Esquema para entregar audiencias"""

    data: List[AudienciaOut] = []
