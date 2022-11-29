"""
Tesis Jurisprudencias v2, esquemas de pydantic
"""
from datetime import date, datetime
from pydantic import BaseModel


class TesisJurisprudenciaOut(BaseModel):
    """Esquema para entregar tesis jurisprudencias"""

    id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    epoca_nombre: str
    materia_nombre: str
    titulo: str
    subtitulo: str
    tipo: str
    estado: str
    clave_control: str
    clase: str
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
