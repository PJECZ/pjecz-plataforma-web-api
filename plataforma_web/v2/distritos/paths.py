"""
Distritos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.distritos.crud import get_distritos, get_distrito
from plataforma_web.v2.distritos.schemas import DistritoOut

distritos = APIRouter()


@distritos.get("", response_model=LimitOffsetPage[DistritoOut])
async def listado_distritos(
    solo_distritos: bool = False,
    db: Session = Depends(get_db),
):
    """Listado de Distritos"""
    try:
        listado = get_distritos(db, solo_distritos=solo_distritos)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@distritos.get("/{distrito_id}", response_model=DistritoOut)
async def detalle_distrito(
    distrito_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Distrito a partir de su id"""
    try:
        distrito = get_distrito(db, distrito_id=distrito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return DistritoOut.from_orm(distrito)
