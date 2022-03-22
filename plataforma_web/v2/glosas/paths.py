"""
Glosas v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.glosas.crud import get_glosas, get_glosa
from plataforma_web.v2.glosas.schemas import GlosaOut

glosas = APIRouter()


@glosas.get("", response_model=LimitOffsetPage[GlosaOut])
async def listado_glosas(
    autoridad_id: int = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Glosas"""
    try:
        listado = get_glosas(db, autoridad_id, anio)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@glosas.get("/{glosa_id}", response_model=GlosaOut)
async def detalle_glosa(
    glosa_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de una Glosa a partir de su id"""
    try:
        glosa = get_glosa(db, glosa_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return GlosaOut.from_orm(glosa)
