"""
Ubicaciones de Expedientes, vistas
"""
from fastapi import APIRouter
from fastapi_sqlalchemy import db

from api.ubicaciones_expedientes.models import UbicacionExpediente

router = APIRouter()


@router.get("")
async def ubicaciones_expedientes_activos(
    autoridad: int,
    expediente: str,
):
    """ Ubicación de Expedientes """
    consulta = db.session.query(UbicacionExpediente)
    consulta = consulta.filter(UbicacionExpediente.autoridad_id == autoridad)
    consulta = consulta.filter(UbicacionExpediente.expediente.like(f"%{expediente}%"))
    return consulta.filter(UbicacionExpediente.estatus == "A").limit(100).all()
