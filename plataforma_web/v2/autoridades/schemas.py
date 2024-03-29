"""
Autoridades v2, esquemas
"""
from pydantic import BaseModel


class AutoridadOut(BaseModel):
    """Esquema para entregar autoridades"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    materia_id: int
    materia_nombre: str
    clave: str
    descripcion: str
    descripcion_corta: str
    organo_jurisdiccional: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
