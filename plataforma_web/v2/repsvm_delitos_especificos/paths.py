"""
REPSVM Delitos Especificos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.repsvm_delitos_especificos.crud import get_repsvm_delitos_especificos, get_repsvm_delito_especifico
from plataforma_web.v2.repsvm_delitos_especificos.schemas import REPSVMDelitoEspecificoOut

repsvm_delitos_especificos = APIRouter()


@repsvm_delitos_especificos.get("", response_model=LimitOffsetPage[REPSVMDelitoEspecificoOut])
async def listado_repsvm_delitos_especificos(
    repsvm_delito_generico_id: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Delitos Especificos"""
    try:
        listado = get_repsvm_delitos_especificos(db, repsvm_delito_generico_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_delitos_especificos.get("/{repsvm_delito_especifico_id}", response_model=REPSVMDelitoEspecificoOut)
async def detalle_repsvm_delito_especifico(
    repsvm_delito_especifico_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Delito Especifico a partir de su id"""
    try:
        repsvm_delito_especifico = get_repsvm_delito_especifico(db, repsvm_delito_especifico_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMDelitoEspecificoOut.from_orm(repsvm_delito_especifico)
