"""
Abogados, vistas
"""
from datetime import date, datetime
from typing import Optional
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.abogados.models import Abogado

router = APIRouter()


@router.get("")
async def abogados_activos(
    ano: Optional[int] = None,
    ano_desde: Optional[int] = None,
    ano_hasta: Optional[int] = None,
    fecha: Optional[date] = None,
    libro: Optional[str] = None,
    nombre: Optional[str] = None,
):
    """ Lista de Abogados activos """
    consulta = db.session.query(Abogado)
    if ano_desde:
        desde = datetime.strptime(f"{ano_desde}-01-01", "%Y-%m-%d")
        consulta = consulta.filter(Abogado.fecha >= desde)
    if ano_hasta:
        hasta = datetime.strptime(f"{ano_hasta}-12-31", "%Y-%m-%d")
        consulta = consulta.filter(Abogado.fecha <= hasta)
    if ano and not (ano_desde or ano_hasta):
        desde = datetime.strptime(f"{ano}-01-01", "%Y-%m-%d")
        hasta = datetime.strptime(f"{ano}-12-31", "%Y-%m-%d")
        consulta = consulta.filter(Abogado.fecha >= desde).filter(Abogado.fecha <= hasta)
    if nombre:
        consulta = consulta.filter(Abogado.nombre.like(f"%{nombre.upper()}%"))
    if libro:
        consulta = consulta.filter(Abogado.libro == libro)
    if fecha:
        consulta = consulta.filter(Abogado.fecha == fecha)
    return consulta.filter(Abogado.estatus == "A").limit(100).all()


@router.get("/{abogado_id}")
async def abogado(abogado_id: int):
    """ Un Abogado """
    return db.session.query(Abogado).get(abogado_id)
