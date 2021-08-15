"""
Distritos, esquemas de pydantic
"""
from pydantic import BaseModel


class DistritoOut(BaseModel):
    """Esquema Distrito"""

    id: int
    distrito: str
    distrito_corto: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
