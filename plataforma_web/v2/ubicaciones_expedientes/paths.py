"""
Ubicaciones Expedientes v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from .crud import get_ubicaciones_expedientes, get_ubicacion_expediente
from .schemas import UbicacionExpedienteOut

ubicaciones_expedientes = APIRouter()


@ubicaciones_expedientes.get("", response_model=LimitOffsetPage[UbicacionExpedienteOut])
async def listado_ubicaciones_expedientes(
    autoridad_id: int = None,
    expediente: str = None,
    db: Session = Depends(get_db),
):
    """Listado de Ubicaciones Expedientes"""
    try:
        listado = get_ubicaciones_expedientes(db, autoridad_id=autoridad_id, expediente=expediente)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=UbicacionExpedienteOut)
async def detalle_ubicacion_expediente(
    ubicacion_expediente_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Ubicacion Expediente a partir de su id"""
    try:
        ubicacion_expediente = get_ubicacion_expediente(db, ubicacion_expediente_id=ubicacion_expediente_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return UbicacionExpedienteOut.from_orm(ubicacion_expediente)
