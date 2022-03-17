"""
Materias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from .crud import get_materias, get_materia
from .schemas import MateriaOut

materias = APIRouter()


@materias.get("", response_model=LimitOffsetPage[MateriaOut])
async def listado_materias(
    db: Session = Depends(get_db),
):
    """Listado de Materias"""
    return paginate(get_materias(db))


@materias.get("/{materia_id}", response_model=MateriaOut)
async def detalle_materia(
    materia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Materia a partir de su id"""
    try:
        materia = get_materia(db, materia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaOut.from_orm(materia)