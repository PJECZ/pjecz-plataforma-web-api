"""
Materias Tipos de Juzgados v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.materias_tipos_juzgados.crud import get_materias_tipos_juzgados, get_materia_tipo_juzgado
from plataforma_web.v2.materias_tipos_juzgados.schemas import MateriaTipoJuzgadoOut

materias_tipos_juzgados = APIRouter()


@materias_tipos_juzgados.get("", response_model=LimitOffsetPage[MateriaTipoJuzgadoOut])
async def listado_materias_tipos_juzgados(
    materia_id: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Tipos de Juzgados"""
    try:
        listado = get_materias_tipos_juzgados(db, materia_id=materia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@materias_tipos_juzgados.get("/{materia_tipo_juzgado_id}", response_model=MateriaTipoJuzgadoOut)
async def detalle_materia_tipo_juzgado(
    materia_tipo_juzgado_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Tipo de Juzgado a partir de su id"""
    try:
        materia_tipo_juzgado = get_materia_tipo_juzgado(db, materia_tipo_juzgado_id=materia_tipo_juzgado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaTipoJuzgadoOut.from_orm(materia_tipo_juzgado)
