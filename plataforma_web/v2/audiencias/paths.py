"""
Audiencias v2, rutas (paths)
"""
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_audiencias, get_audiencia
from .schemas import AudienciaOut, AudienciaDataTableReponse

audiencias = APIRouter()


@audiencias.get("", response_model=AudienciaDataTableReponse)
async def datatable_audiencias(
    draw: int = 0,
    start: int = 0,
    length: int = 10,
    autoridad_id: int = None,
    fecha: date = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """DataTable de audiencias"""
    try:
        consulta = get_audiencias(
            db,
            autoridad_id=autoridad_id,
            fecha=fecha,
            anio=anio,
        )
        cantidad_total = consulta.count()
        cantidad_filtrados = cantidad_total
        listado = consulta.offset(start).limit(length).all()
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AudienciaDataTableReponse(
        draw=draw,
        recordsTotal=cantidad_total,
        recordsFiltered=cantidad_filtrados,
        data=listado,
    )


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
