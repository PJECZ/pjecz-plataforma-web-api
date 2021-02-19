"""
Listas de Acuerdos, esquemas
"""
from datetime import date
from typing import Optional
from pydantic import BaseModel


class ListaDeAcuerdoBase(BaseModel):
    """ Esquema para consultar Listas de Acuerdos """

    autoridad_id: int
    fecha: Optional[date] = None
    archivo: Optional[str] = None
    descripcion: Optional[str] = None
    url: Optional[str] = None


class ListaDeAcuerdoNew(ListaDeAcuerdoBase):
    """ Esquema para crear una nueva Lista de Acuerdos """


class ListaDeAcuerdo(ListaDeAcuerdoNew):
    """ Esquema Lista de Acuerdos """

    id: int

    class Config:
        """ Configurar modo ORM """

        orm_mode = True
