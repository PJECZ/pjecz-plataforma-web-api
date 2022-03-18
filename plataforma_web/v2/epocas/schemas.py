"""
Epocas v2, esquemas de pydantic
"""
from pydantic import BaseModel


class EpocaOut(BaseModel):
    """Esquema para entregar epocas"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
