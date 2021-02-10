"""
Distritos, vistas
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.distritos.models import Distrito

router = APIRouter()


@router.get("")
async def distritos_activos():
    """ Lista de Distritos activos """
    return db.session.query(Distrito).filter(Distrito.estatus == "A").all()
