"""
Peritos, esquemas
"""
from pydantic import BaseModel


class PeritoOut(BaseModel):
    """Esquema Perito"""

    id: int
    distrito_id: int
    distrito: str
    nombre: str
    tipo: str
    domicilio: str
    telefono_fijo: str
    telefono_celular: str
    email: str
    notas: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
