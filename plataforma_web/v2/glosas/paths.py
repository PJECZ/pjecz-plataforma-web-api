"""
Glosas v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_glosas, get_glosa
from .schemas import GlosaOut

glosas = APIRouter()


@glosas.get("", response_model=LimitOffsetPage[GlosaOut])
async def datatable_glosas(
    autoridad_id: int = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """DataTable de glosas"""
    try:
        consulta = get_glosas(
            db,
            autoridad_id=autoridad_id,
            anio=anio,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(consulta)


@glosas.get("/{glosa_id}", response_model=GlosaOut)
async def detalle_glosa(
    glosa_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de una Glosa a partir de su id"""
    try:
        glosa = get_glosa(db, glosa_id=glosa_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return GlosaOut.from_orm(glosa)
