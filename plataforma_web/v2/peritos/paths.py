"""
Peritos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from .crud import get_peritos, get_perito
from .schemas import PeritoOut

peritos = APIRouter()


from fastapi_pagination.ext.sqlalchemy import paginate
from lib.fastapi_pagination_datatable import LimitOffsetPage


@peritos.get("", response_model=LimitOffsetPage[PeritoOut])
async def datatable_peritos(
    distrito_id: int = None,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """DataTable de peritos"""
    try:
        consulta = get_peritos(
            db,
            distrito_id=distrito_id,
            nombre=nombre,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(consulta)


@peritos.get("/{perito_id}", response_model=PeritoOut)
async def detalle_perito(
    perito_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Perito a partir de su id"""
    try:
        perito = get_perito(db, perito_id=perito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return PeritoOut.from_orm(perito)
