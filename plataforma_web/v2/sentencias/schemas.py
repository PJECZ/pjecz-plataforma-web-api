"""
Sentencias v2, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class SentenciaOut(BaseModel):
    """Esquema para entregar sentencias"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    fecha: date
    sentencia: str
    expediente: str
    es_perspectiva_genero: bool
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
