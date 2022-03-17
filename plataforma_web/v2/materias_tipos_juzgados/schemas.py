"""
Materias Tipos de Juzgados v2, esquemas de pydantic
"""
from pydantic import BaseModel


class MateriaTipoJuzgadoOut(BaseModel):
    """Esquema para entregar tipo de juzgado"""

    id: int
    materia_id: int
    materia_nombre: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
