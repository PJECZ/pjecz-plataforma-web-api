"""
Listas de Acuerdos v2, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class ListaDeAcuerdoOut(BaseModel):
    """Esquema para entregar listas de acuerdos"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    fecha: date
    descripcion: str
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
