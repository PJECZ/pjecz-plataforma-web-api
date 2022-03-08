"""
REPSVM Agresores, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMAgresorOut(BaseModel):
    """Esquema para consultar agresor"""

    id: int
    distrito_id: int
    distrito: str
    materia_tipo_juzgado_id: int
    materia_tipo_juzgado: str
    repsvm_delito_especifico_id: int
    repsvm_delito_especifico: str
    repsvm_tipo_sentencia_id: int
    repsvm_tipo_sentencia: str
    nombre: str
    numero_causa: str
    pena_impuesta: str
    observaciones: str
    sentencia_url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
