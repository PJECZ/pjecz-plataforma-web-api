"""
Audiencias v2, esquemas de pydantic
"""
from datetime import datetime
from pydantic import BaseModel


class AudienciaOut(BaseModel):
    """Esquema para entregar audiencias"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    tiempo: datetime
    tipo_audiencia: str
    expediente: str
    actores: str
    demandados: str
    sala: str
    caracter: str
    causa_penal: str
    delitos: str
    toca: str
    expediente_origen: str
    imputados: str
    origen: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
