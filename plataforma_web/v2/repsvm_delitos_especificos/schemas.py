"""
REPSVM Delitos Especificos v2, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMDelitoEspecificoOut(BaseModel):
    """Esquema para entregar delitos especificos"""

    id: int
    repsvm_delito_generico_id: int
    repsvm_delito_generico_nombre: str
    descripcion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
