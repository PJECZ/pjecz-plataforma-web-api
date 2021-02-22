"""
Ubicaciones de Expedientes, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.autoridades.crud import get_autoridad
from api.ubicaciones_expedientes import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.UbicacionExpediente])
async def listar_ubicaciones_expedientes(autoridad_id: int, expediente: str = None, db: Session = Depends(get_db)):
    """ Lista de Ubicaciones de Expedientes """
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    return crud.get_ubicaciones_expedientes(db, autoridad_id=autoridad_id, expediente=expediente)


@router.get("/{ubicacion_expediente_id}", response_model=schemas.UbicacionExpediente)
async def consultar_una_ubicacion_expediente(ubicacion_expediente_id: int, db: Session = Depends(get_db)):
    """ Consultar una Ubicación de Expedientes """
    ubicacion_expediente = crud.get_ubicacion_expediente(db, ubicacion_expediente_id=ubicacion_expediente_id)
    if ubicacion_expediente is None:
        raise HTTPException(status_code=400, detail="No existe la ubicación de expediente.")
    return ubicacion_expediente