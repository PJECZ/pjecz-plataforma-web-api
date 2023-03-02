"""
Distritos v2, esquemas
"""
from pydantic import BaseModel


class DistritoOut(BaseModel):
    """Esquema para entregar distritos"""

    id: int
    clave: str
    nombre: str
    nombre_corto: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
