"""
REPSVM Delitos Genericos, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoGenericoOut(BaseModel):
    """Esquema para consultar delito generico"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
