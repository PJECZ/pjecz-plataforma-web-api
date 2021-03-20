"""
Peritos, esquemas
"""
from typing import Optional
from pydantic import BaseModel


class Perito(BaseModel):
    """ Esquema Perito """

    id: int
    distrito_id: int
    distrito: str
    nombre: Optional[str] = None
    tipo: str
    domicilio: str
    telefono_fijo: str
    telefono_celular: str
    email: str
    notas: str
