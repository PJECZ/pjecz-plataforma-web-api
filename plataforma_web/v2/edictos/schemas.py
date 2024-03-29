"""
Edictos v2, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class EdictoOut(BaseModel):
    """Esquema para entregar edictos"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    fecha: date
    descripcion: str
    expediente: str
    numero_publicacion: str
    archivo: str
    url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
