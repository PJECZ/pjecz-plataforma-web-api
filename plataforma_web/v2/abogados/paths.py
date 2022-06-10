"""
Abogados v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_abogados, get_abogado
from .schemas import AbogadoOut, AbogadoDataTableResponse

abogados = APIRouter()


@abogados.get("", response_model=AbogadoDataTableResponse)
async def datatable_abogados(
    draw: int = 0,
    start: int = 0,
    length: int = 10,
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
    db: Session = Depends(get_db),
):
    """DataTable de abogados"""
    try:
        consulta = get_abogados(
            db,
            nombre=nombre,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
        )
        cantidad_total = consulta.count()
        cantidad_filtrados = cantidad_total
        listado = consulta.offset(start).limit(length).all()
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AbogadoDataTableResponse(
        draw=draw,
        recordsTotal=cantidad_total,
        recordsFiltered=cantidad_filtrados,
        data=listado,
    )


@abogados.get("/{abogado_id}", response_model=AbogadoOut)
async def detalle_abogado(
    abogado_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Abogado a partir de su id"""
    try:
        abogado = get_abogado(db, abogado_id=abogado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AbogadoOut.from_orm(abogado)
