"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_redams, get_redam
from .schemas import RedamOut, RedamDataTableRequest, RedamDataTableResponse

redams = APIRouter()


@redams.post("")
async def datatable_redams(
    request: RedamDataTableRequest,
    db: Session = Depends(get_db),
) -> RedamDataTableResponse:
    """Listado de deudores"""
    try:
        listado = get_redams(
            db,
            distrito_id=request.distrito_id,
            autoridad_id=request.autoridad_id,
            nombre=request.nombre,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return RedamDataTableResponse(
        draw=request.draw,
        iTotalRecords=listado.count(),
        iTotalDisplayRecords=listado.count(),
        aaData=listado.offset(request.start).limit(request.length).all(),
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
