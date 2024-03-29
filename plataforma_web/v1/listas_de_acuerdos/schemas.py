"""
Listas de Acuerdos, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class ListaDeAcuerdoOut(BaseModel):
    """Esquema Listas de Acuerdos"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    fecha: date
    descripcion: str
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
