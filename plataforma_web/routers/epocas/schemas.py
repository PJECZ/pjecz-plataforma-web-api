"""
Epocas, esquemas de pydantic
"""
from pydantic import BaseModel


class EpocaOut(BaseModel):
    """Esquema Epoca"""

    id: int
    nombre: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
