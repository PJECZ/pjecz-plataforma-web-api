"""
Ubicaciones de Expedientes, esquemas de pydantic
"""
from pydantic import BaseModel


class UbicacionExpediente(BaseModel):
    """ Esquema UbicacionExpediente """

    id: int
    autoridad_id: int
    # TODO: autoridad: str
    expediente: str
    ubicacion: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True
