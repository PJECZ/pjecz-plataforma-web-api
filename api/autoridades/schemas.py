"""
Autoridades, esquemas de pydantic
"""
from pydantic import BaseModel


class AutoridadList(BaseModel):
    """ Esquema Autoridad para listado """

    id: int
    distrito_id: int
    distrito: str
    autoridad: str


class Autoridad(AutoridadList):
    """ Esquema Autoridad para detalle """

    email: str
