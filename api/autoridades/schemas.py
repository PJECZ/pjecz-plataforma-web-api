"""
Autoridades, esquemas de pydantic
"""
from pydantic import BaseModel


class AutoridadList(BaseModel):
    """ Esquema Autoridad Listado """

    id: int
    distrito_id: int
    distrito_nombre: str
    descripcion: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True


class Autoridad(AutoridadList):
    """ Esquema Autoridad Detalle """

    email: str
    directorio_listas_de_acuerdos: str
    directorio_sentencias: str
