"""
Ubicaciones de Expedientes, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_ubicacion_expediente, get_ubicaciones_expedientes
from .schemas import UbicacionExpedienteOut

ubicaciones_expedientes = APIRouter()


@ubicaciones_expedientes.get("", response_model=List[UbicacionExpedienteOut])
async def listar_ubicaciones_expedientes(
    autoridad_id: int,
    expediente: str = None,
    db: Session = Depends(get_db),
):
    """Lista de Ubicaciones de Expedientes"""
    resultados = []
    try:
        for ubicacion_expediente, autoridad, distrito in get_ubicaciones_expedientes(db, autoridad_id=autoridad_id, expediente=expediente):
            resultados.append(
                UbicacionExpedienteOut(
                    id=ubicacion_expediente.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    expediente=ubicacion_expediente.expediente,
                    ubicacion=ubicacion_expediente.ubicacion,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@ubicaciones_expedientes.get("/{ubicacion_expediente_id}", response_model=UbicacionExpedienteOut)
async def consultar_una_ubicacion_expediente(ubicacion_expediente_id: int, db: Session = Depends(get_db)):
    """Consultar una Ubicación de Expedientes"""
    try:
        ubicacion_expediente = get_ubicacion_expediente(db, ubicacion_expediente_id=ubicacion_expediente_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return UbicacionExpedienteOut(
        id=ubicacion_expediente.id,
        distrito_id=ubicacion_expediente.autoridad.distrito_id,
        distrito=ubicacion_expediente.autoridad.distrito.nombre,
        autoridad_id=ubicacion_expediente.autoridad_id,
        autoridad=ubicacion_expediente.autoridad.descripcion,
        expediente=ubicacion_expediente.expediente,
        ubicacion=ubicacion_expediente.ubicacion,
    )
