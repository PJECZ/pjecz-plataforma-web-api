"""
Ubicaciones de Expedientes, esquemas de pydantic
"""
from pydantic import BaseModel


class UbicacionExpedienteOut(BaseModel):
    """Esquema Ubicación de Expediente"""

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    expediente: str
    ubicacion: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
