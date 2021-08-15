"""
Glosas, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class GlosaOut(BaseModel):
    """Esquema Glosa"""

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

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
