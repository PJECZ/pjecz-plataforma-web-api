"""
Distritos, esquemas de pydantic
"""
from pydantic import BaseModel


class Distrito(BaseModel):
    """ Esquema Distrito """

    id: int
    nombre: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True
