"""
Edictos, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class EdictoOut(BaseModel):
    """Esquema Edicto"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    fecha: date
    descripcion: str
    expediente: str
    numero_publicacion: str
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
