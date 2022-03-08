"""
REPSVM Delitos Genericos, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoGenericoOut(BaseModel):
    """Esquema para consultar delito generico"""

    id: int
    delito_generico: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
