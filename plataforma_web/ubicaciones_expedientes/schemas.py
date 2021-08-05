"""
Ubicaciones de Expedientes, esquemas de pydantic
"""
from pydantic import BaseModel


class UbicacionExpediente(BaseModel):
    """ Esquema UbicacionExpediente """

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    expediente: str
    ubicacion: str
