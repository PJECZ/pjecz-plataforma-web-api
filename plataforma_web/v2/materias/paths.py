"""
Materias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.materias.crud import get_materias, get_materia
from plataforma_web.v2.materias.schemas import MateriaOut

materias = APIRouter()


@materias.get("", response_model=LimitOffsetPage[MateriaOut])
async def listado_materias(
    db: Session = Depends(get_db),
):
    """Listado de Materias"""
    try:
        listado = get_materias(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


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
