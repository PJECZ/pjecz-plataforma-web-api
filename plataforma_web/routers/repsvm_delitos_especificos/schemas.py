"""
REPSVM Delitos Especificos, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoEspecificoOut(BaseModel):
    """Esquema para consultar delito especifico"""

    id: int
    delito_generico_id: int
    delito_generico: str
    delito_especifico: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
