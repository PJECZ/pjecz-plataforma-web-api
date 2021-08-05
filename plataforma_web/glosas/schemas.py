"""
Glosas, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class Glosa(BaseModel):
    """ Esquema para consultar glosas """

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    fecha: date
    tipo_juicio: str
    descripcion: str
    expediente: str
    archivo: str
    url: str
