"""
Listas de Acuerdos, vistas
"""
from datetime import date
from typing import Optional
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.listas_de_acuerdos.models import ListaDeAcuerdo

router = APIRouter()


@router.get("")
async def listas_de_acuerdos_activas(
    autoridad: int,
    desde: Optional[date] = None,
    hasta: Optional[date] = None,
):
    """ Listas de Acuerdos activas """
    consulta = db.session.query(ListaDeAcuerdo)
    consulta = consulta.filter(ListaDeAcuerdo.autoridad_id == autoridad)
    if desde:
        consulta = consulta.filter(ListaDeAcuerdo.fecha >= desde)
    if hasta:
        consulta = consulta.filter(ListaDeAcuerdo.fecha <= hasta)
    return consulta.filter(ListaDeAcuerdo.estatus == "A").limit(100).all()
