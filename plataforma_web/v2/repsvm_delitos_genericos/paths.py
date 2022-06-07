"""
REPSVM Delitos Genericos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.repsvm_delitos_genericos.crud import get_repsvm_delitos_genericos, get_repsvm_delito_generico
from plataforma_web.v2.repsvm_delitos_genericos.schemas import REPSVMDelitoGenericoOut

repsvm_delitos_genericos = APIRouter()


@repsvm_delitos_genericos.get("", response_model=LimitOffsetPage[REPSVMDelitoGenericoOut])
async def listado_repsvm_delitos_genericos(
    db: Session = Depends(get_db),
):
    """Listado de Delitos Genericos"""
    try:
        listado = get_repsvm_delitos_genericos(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_delitos_genericos.get("/{repsvm_delito_generico_id}", response_model=REPSVMDelitoGenericoOut)
async def detalle_repsvm_delito_generico(
    repsvm_delito_generico_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Delito Generico a partir de su id"""
    try:
        repsvm_delito_generico = get_repsvm_delito_generico(db, repsvm_delito_generico_id=repsvm_delito_generico_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMDelitoGenericoOut.from_orm(repsvm_delito_generico)
