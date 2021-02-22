"""
Peritos, esquemas
"""
from pydantic import BaseModel
from typing import Optional


class Perito(BaseModel):
    """ Esquema Perito """

    id: int
    distrito_id: int
    nombre: Optional[str] = None
    tipo: str
    domicilio: str
    telefono_fijo: str
    telefono_celular: str
    email: str
    notas: str

    class Config:
        """ Configurar modo ORM """

        orm_mode = True
