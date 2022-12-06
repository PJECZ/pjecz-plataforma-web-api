"""
REPSVM Agresores-Delitos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_repsvm_agresores_delitos, get_repsvm_agresor_delito
from .schemas import REPSVMAgresorDelitoOut

repsvm_agresores_delitos = APIRouter()


@repsvm_agresores_delitos.get("", response_model=LimitOffsetPage[REPSVMAgresorDelitoOut])
async def listado_repsvm_agresores_delitos(
    repsvm_agresor_id: int = None,
    repsvm_delito_id: int = None,
    db: Session = Depends(get_db),
):
    """Listado de agresores-delitos"""
    try:
        listado = get_repsvm_agresores_delitos(
            db,
            repsvm_agresor_id=repsvm_agresor_id,
            repsvm_delito_id=repsvm_delito_id,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_agresores_delitos.get("/{repsvm_agresor_delito_id}", response_model=REPSVMAgresorDelitoOut)
async def detalle_repsvm_agresor_delito(
    repsvm_agresor_delito_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un agresor-delito a partir de su id"""
    try:
        repsvm_agresor_delito = get_repsvm_agresor_delito(db, repsvm_agresor_delito_id=repsvm_agresor_delito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMAgresorDelitoOut.from_orm(repsvm_agresor_delito)
