"""
Autoriades, vistas
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.autoridades.models import Autoridad

router = APIRouter()


@router.get("/")
async def autoridades_activas():
    """ Lista de Autoriades activas """
    return db.session.query(Autoridad).filter(Autoridad.estatus == "A").limit(100).all()
