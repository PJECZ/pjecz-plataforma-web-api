"""
Autoridades, esquemas de pydantic
"""
from pydantic import BaseModel


class Autoridad(BaseModel):
    """ Esquema Autoridad para listado """

    id: int
    distrito_id: int
    distrito: str
    autoridad: str
