"""
REPSVM Agresores v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_repsvm_agresores, get_repsvm_agresor
from .schemas import REPSVMAgresorOut

repsvm_agresores = APIRouter()


@repsvm_agresores.get("", response_model=LimitOffsetPage[REPSVMAgresorOut])
async def listado_repsvm_agresores(
    distrito_id: int = None,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """Listado de Agresores"""
    try:
        listado = get_repsvm_agresores(db, distrito_id=distrito_id, nombre=nombre)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_agresores.get("/{repsvm_agresor_id}", response_model=REPSVMAgresorOut)
async def detalle_repsvm_agresor(
    repsvm_agresor_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Agresor a partir de su id"""
    try:
        repsvm_agresor = get_repsvm_agresor(db, repsvm_agresor_id=repsvm_agresor_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMAgresorOut.from_orm(repsvm_agresor)
