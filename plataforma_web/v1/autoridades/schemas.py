"""
Autoridades, esquemas de pydantic
"""
from pydantic import BaseModel


class AutoridadOut(BaseModel):
    """Esquema Autoridad"""

    id: int
    distrito_id: int
    distrito: str
    materia_id: int
    materia: str
    autoridad: str
    autoridad_corta: str
    organo_jurisdiccional: str
    audiencia_categoria: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
