"""
Abogados, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class Abogado(BaseModel):
    """ Esquema Abogado """

    id: int
    fecha: date
    libro: str
    numero: str
    nombre: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True