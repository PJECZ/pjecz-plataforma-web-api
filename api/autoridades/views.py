"""
Autoriades, vistas
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.autoridades.models import Autoridad

router = APIRouter()


@router.get("/")
async def list_activos():
    """ Lista de Autoriades activas """
    return db.session.query(Autoridad).filter(Autoridad.estatus == "A").limit(100).all()
