"""
REPSVM Tipos de Sentencias, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMTipoSentenciaOut(BaseModel):
    """Esquema para consultar tipo de sentencia"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
