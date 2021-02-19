"""
Autoridades, esquemas de pydantic
"""
from pydantic import BaseModel


class AutoridadList(BaseModel):
    """ Esquema Autoridad """

    id: int
    distrito_id: int
    descripcion: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True


class Autoridad(AutoridadList):
    """ Esquema Autoridad """

    email: str
    directorio_listas_de_acuerdos: str
    directorio_sentencias: str
