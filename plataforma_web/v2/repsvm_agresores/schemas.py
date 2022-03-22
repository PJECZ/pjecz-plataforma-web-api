"""
REPSVM Agresores v2, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMAgresorOut(BaseModel):
    """Esquema para entregar agresores"""

    id: int
    distrito_id: int
    distrito_nombre: str
    materia_tipo_juzgado_id: int
    materia_tipo_juzgado_descripcion: str
    repsvm_delito_especifico_id: int
    repsvm_delito_especifico_descripcion: str
    repsvm_tipo_sentencia_id: int
    repsvm_tipo_sentencia_nombre: str
    consecutivo: int
    nombre: str
    numero_causa: str
    pena_impuesta: str
    observaciones: str
    sentencia_url: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
