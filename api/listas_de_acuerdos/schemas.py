"""
Listas de Acuerdos, esquemas de pydantic
"""
from datetime import date
from typing import Optional
from pydantic import BaseModel


class ListaDeAcuerdo(BaseModel):
    """ Esquema para consultar Listas de Acuerdos """

    id: int
    autoridad_id: int
    fecha: Optional[date] = None
    archivo: Optional[str] = None
    descripcion: Optional[str] = None
    url: Optional[str] = None

    class Config:
        """ Configurar modo ORM """

        orm_mode = True


class ListaDeAcuerdoNew(BaseModel):
    """ Esquema para crear una nueva Lista de Acuerdos """

    autoridad_email: str
    fecha: date
    archivo: str
    descripcion: Optional[str] = None
    url: Optional[str] = None
