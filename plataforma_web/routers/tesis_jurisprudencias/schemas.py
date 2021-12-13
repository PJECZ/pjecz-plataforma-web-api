"""
Tesis Jurisprudencias, esquemas de pydantic
"""
from datetime import date, datetime
from pydantic import BaseModel


class TesisJurisprudenciaOut(BaseModel):
    """Esquema para tesis jurisprudencias"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    epoca_id: int
    epoca: str
    materia_id: int
    materia: str
    titulo: str
    subtitulo: str
    tipo: str
    estado: str
    clave_control: str
    clase: str
    instancia: str
    rubro: str
    texto: str
    precedentes: str
    votacion: str
    votos_particulares: str
    aprobacion_fecha: date
    publicacion_tiempo: datetime
    aplicacion_tiempo: datetime

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
