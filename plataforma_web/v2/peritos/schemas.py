"""
Peritos v2, esquemas de pydantic
"""
from pydantic import BaseModel


class PeritoOut(BaseModel):
    """Esquema para entregar peritos"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    perito_tipo_id: int
    perito_tipo_nombre: str
    nombre: str
    domicilio: str
    telefono_fijo: str
    telefono_celular: str
    email: str
    notas: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
