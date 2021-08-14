"""
Materias, esquemas de pydantic
"""
from pydantic import BaseModel


class Materia(BaseModel):
    """Esquema Materia"""

    id: int
    materia: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
