"""
Peritos Tipos v2, esquemas de pydantic
"""
from pydantic import BaseModel


class PeritoTipoOut(BaseModel):
    """ Esquema para entregar tipos de peritos """

    id: int
    nombre: str

    class Config:
        """ SQLAlchemy config """

        orm_mode = True
