"""
Peritos Tipos, esquemas de pydantic
"""
from pydantic import BaseModel


class PeritoTipoOut(BaseModel):
    """Esquema Tipo de Perito"""

    id: int
    perito_tipo: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
