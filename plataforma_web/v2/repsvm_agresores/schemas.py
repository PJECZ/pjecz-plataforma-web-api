"""
REPSVM Agresores v2, esquemas de pydantic
"""
from pydantic import BaseModel


class REPSVMAgresorOut(BaseModel):
    """Esquema para entregar agresores"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    materia_tipo_juzgado_descripcion: str
    repsvm_delito_generico_nombre: str
    repsvm_delito_especifico_descripcion: str
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
