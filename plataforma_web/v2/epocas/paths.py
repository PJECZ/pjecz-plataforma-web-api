"""
Epocas v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.epocas.crud import get_epocas, get_epoca
from plataforma_web.v2.epocas.schemas import EpocaOut

epocas = APIRouter()


@epocas.get("", response_model=LimitOffsetPage[EpocaOut])
async def listado_epocas(db: Session = Depends(get_db)):
    """Listado de Epocas"""
    try:
        listado = get_epocas(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@epocas.get("/{epoca_id}", response_model=EpocaOut)
async def detalle_epoca(
    epoca_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Epoca a partir de su id"""
    try:
        epoca = get_epoca(db, epoca_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return EpocaOut.from_orm(epoca)
