"""
Audiencias v2, rutas (paths)
"""
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.audiencias.crud import get_audiencias, get_audiencia
from plataforma_web.v2.audiencias.schemas import AudienciaOut

audiencias = APIRouter()


@audiencias.get("", response_model=LimitOffsetPage[AudienciaOut])
async def listado_audiencias(
    autoridad_id: int = None,
    fecha: date = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Audiencias"""
    try:
        listado = get_audiencias(db, autoridad_id=autoridad_id, fecha=fecha, anio=anio)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@audiencias.get("/{audiencia_id}", response_model=AudienciaOut)
async def detalle_audiencia(
    audiencia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Audiencia a partir de su id"""
    try:
        audiencia = get_audiencia(db, audiencia_id=audiencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AudienciaOut.from_orm(audiencia)
