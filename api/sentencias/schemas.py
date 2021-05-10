"""
Sentencias, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class Sentencia(BaseModel):
    """Esquema para consultar sentencias"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    fecha: date
    sentencia: str
    expediente: str
    es_paridad_genero: bool
    archivo: str
    url: str
