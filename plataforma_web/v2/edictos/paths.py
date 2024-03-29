"""
Edictos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_edictos, get_edicto
from .schemas import EdictoOut

edictos = APIRouter()


@edictos.get("", response_model=LimitOffsetPage[EdictoOut])
async def datatable_edictos(
    autoridad_id: int = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """DataTable de edictos"""
    try:
        consulta = get_edictos(
            db,
            autoridad_id=autoridad_id,
            anio=anio,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(consulta)


@edictos.get("/{edicto_id}", response_model=EdictoOut)
async def detalle_edicto(
    edicto_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Edicto a partir de su id"""
    try:
        edicto = get_edicto(db, edicto_id=edicto_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return EdictoOut.from_orm(edicto)
