"""
REPSVM Delitos Especificos, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoEspecificoOut(BaseModel):
    """Esquema para consultar delito especifico"""

    id: int
    repsvm_delito_generico_id: int
    repsvm_delito_generico: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
