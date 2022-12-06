"""
REPSVM Delitos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from plataforma_web.v2.repsvm_delitos.crud import get_repsvm_delitos, get_repsvm_delito
from plataforma_web.v2.repsvm_delitos.schemas import REPSVMDelitoOut

repsvm_delitos = APIRouter()


@repsvm_delitos.get("", response_model=LimitOffsetPage[REPSVMDelitoOut])
async def listado_repsvm_delitos(
    db: Session = Depends(get_db),
):
    """Listado de delitos"""
    try:
        listado = get_repsvm_delitos(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_delitos.get("/{repsvm_delito_id}", response_model=REPSVMDelitoOut)
async def detalle_repsvm_delito(
    repsvm_delito_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un delito a partir de su id"""
    try:
        repsvm_delito = get_repsvm_delito(db, repsvm_delito_id=repsvm_delito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMDelitoOut.from_orm(repsvm_delito)
