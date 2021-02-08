"""
Abogados, vistas
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.abogados.models import Abogado

router = APIRouter()


@router.get("/")
async def list_activos():
    """ Lista de Abogados activos """
    return db.session.query(Abogado).filter(Abogado.estatus == "A").limit(100).all()
