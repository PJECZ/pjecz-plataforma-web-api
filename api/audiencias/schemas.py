"""
Audiencias, esquemas de pydantic
"""
from datetime import datetime
from pydantic import BaseModel


class Audiencia(BaseModel):
    """ Esquema para consultar audencias """

    id: int
    distrito_id: int
    distrito: str
    autoridad_id: int
    autoridad: str
    tiempo: datetime
    tipo_audiencia: str
    expediente: str
    actores: str
    demandados: str
    sala: str
    caracter: str
    causa_penal: str
    delitos: str
    toca: str
    expediente_origen: str
    imputados: str
    origen: str
