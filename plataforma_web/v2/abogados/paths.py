"""
Abogados v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_abogados, get_abogado
from .schemas import AbogadoOut

abogados = APIRouter()


@abogados.get("", response_model=LimitOffsetPage[AbogadoOut])
async def datatable_abogados(
    anio_desde: int = None,
    anio_hasta: int = None,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """DataTable de abogados"""
    try:
        consulta = get_abogados(
            db,
            anio_desde=anio_desde,
            anio_hasta=anio_hasta,
            nombre=nombre,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(consulta)


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
