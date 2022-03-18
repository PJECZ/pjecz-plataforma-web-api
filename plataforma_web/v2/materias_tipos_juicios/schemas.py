"""
Materias Tipos de Juicios v2, esquemas de pydantic
"""
from pydantic import BaseModel


class MateriaTipoJuicioOut(BaseModel):
    """Esquema para entregar tipos de juicios"""

    id: int
    materia_id: int
    materia_nombre: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
