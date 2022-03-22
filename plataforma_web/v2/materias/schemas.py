"""
Materias v2, esquemas
"""
from pydantic import BaseModel


class MateriaOut(BaseModel):
    """Esquema para entregar materias"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
