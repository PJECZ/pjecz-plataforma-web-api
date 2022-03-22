"""
Glosas v2, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class GlosaOut(BaseModel):
    """Esquema para entregar glosas"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_id: int
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    fecha: date
    tipo_juicio: str
    descripcion: str
    expediente: str
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
