"""
Sentencias, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class SentenciaOut(BaseModel):
    """Esquema Sentencia"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    materia_tipo_juicio_id: int
    materia_tipo_juicio: str
    fecha: date
    sentencia: str
    expediente: str
    es_perspectiva_genero: bool
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
