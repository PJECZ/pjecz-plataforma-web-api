"""
REPSVM Delitos Genericos v2, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoGenericoOut(BaseModel):
    """Esquema para entregar delitos genericos"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
