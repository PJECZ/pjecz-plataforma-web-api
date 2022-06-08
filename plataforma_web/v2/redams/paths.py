"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from .crud import get_redams, get_redam
from .schemas import RedamOut

redams = APIRouter()


@redams.get("", response_model=LimitOffsetPage[RedamOut])
async def listado_redams(
    autoridad_id: int = None,
    distrito_id: int = None,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """Listado de deudores"""
    try:
        listado = get_redams(db, autoridad_id=autoridad_id, distrito_id=distrito_id, nombre=nombre)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@redams.get("/{redam_id}", response_model=RedamOut)
async def detalle_redam(
    redam_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un deudor a partir de su id"""
    try:
        redam = get_redam(db, redam_id=redam_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return RedamOut.from_orm(redam)
