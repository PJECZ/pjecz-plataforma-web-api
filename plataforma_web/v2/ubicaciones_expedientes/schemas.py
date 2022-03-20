"""
Ubicaciones Expedientes v2, esquemas de pydantic
"""
from pydantic import BaseModel


class UbicacionExpedienteOut(BaseModel):
    """Esquema para entregar ubicaciones expedientes"""

    id: int
    distrito_id: int
    distrito_nombre: str
    distrito_nombre_corto: str
    autoridad_id: int
    autoridad_clave: str
    autoridad_descripcion: str
    autoridad_descripcion_corta: str
    expediente: str
    ubicacion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
