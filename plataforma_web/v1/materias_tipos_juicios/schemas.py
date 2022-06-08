"""
Materias Tipos Juicios, esquemas de pydantic
"""
from pydantic import BaseModel


class MateriaTipoJuicioOut(BaseModel):
    """Esquema para consultar tipos de juicios"""

    id: int
    materia_id: int
    materia: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
