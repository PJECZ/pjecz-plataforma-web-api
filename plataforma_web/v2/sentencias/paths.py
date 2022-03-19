"""
Sentencias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.sentencias.crud import get_sentencias, get_sentencia
from plataforma_web.v2.sentencias.schemas import SentenciaOut

sentencias = APIRouter()


@sentencias.get("", response_model=LimitOffsetPage[SentenciaOut])
async def listado_sentencias(
    autoridad_id: int,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Sentencias"""
    try:
        listado = get_sentencias(db, autoridad_id, ano)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@sentencias.get("/{sentencia_id}", response_model=SentenciaOut)
async def detalle_sentencia(
    sentencia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Sentencia a partir de su id"""
    try:
        sentencia = get_sentencia(db, sentencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return SentenciaOut.from_orm(sentencia)
