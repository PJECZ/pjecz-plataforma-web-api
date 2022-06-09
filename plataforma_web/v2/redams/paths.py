"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_redams, get_redam
from .schemas import RedamOut, RedamDataTableRequest, RedamDataTableResponse

redams = APIRouter()


@redams.get("")
async def datatable_redams(
    draw: int = 0,
    start: int = 0,
    length: int = 10,
    autoridad_id: int = None,
    distrito_id: int = None,
    nombre: str = None,
    db: Session = Depends(get_db),
) -> RedamDataTableResponse:
    """Listado de deudores"""
    try:
        listado = get_redams(
            db,
            distrito_id=distrito_id,
            autoridad_id=autoridad_id,
            nombre=nombre,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return RedamDataTableResponse(
        draw=draw,
        recordsTotal=listado.count(),
        recordsFiltered=listado.count(),
        data=listado.offset(start).limit(length).all(),
    )


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
