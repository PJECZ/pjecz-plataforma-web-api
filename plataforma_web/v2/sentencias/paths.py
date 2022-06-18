"""
Sentencias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_sentencias, get_sentencia
from .schemas import SentenciaOut

sentencias = APIRouter()


@sentencias.get("", response_model=LimitOffsetPage[SentenciaOut])
async def datatable_sentencias(
    autoridad_id: int = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """DataTable de sentencias"""
    try:
        consulta = get_sentencias(
            db,
            autoridad_id=autoridad_id,
            anio=anio,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(consulta)


@sentencias.get("/{sentencia_id}", response_model=SentenciaOut)
async def detalle_sentencia(
    sentencia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Sentencia a partir de su id"""
    try:
        sentencia = get_sentencia(db, sentencia_id=sentencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return SentenciaOut.from_orm(sentencia)
