"""
Materias Tipos de Juzgados, esquemas de pydantic
"""
from pydantic import BaseModel


class MateriaTipoJuzgadoOut(BaseModel):
    """Esquema para consultar tipo de juzgado"""

    id: int
    materia_id: int
    materia: str
    materia_tipo_juzgado: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
