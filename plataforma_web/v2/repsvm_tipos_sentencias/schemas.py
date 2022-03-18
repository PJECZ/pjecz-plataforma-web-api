"""
REPSVM Tipos Sentencias v2, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMTipoSentenciaOut(BaseModel):
    """Esquema para entregar tipos de sentencias"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
