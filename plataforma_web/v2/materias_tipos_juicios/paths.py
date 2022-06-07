"""
Materias Tipos de Juicios v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.materias_tipos_juicios.crud import get_materias_tipos_juicios, get_materia_tipo_juicio
from plataforma_web.v2.materias_tipos_juicios.schemas import MateriaTipoJuicioOut

materias_tipos_juicios = APIRouter()


@materias_tipos_juicios.get("", response_model=LimitOffsetPage[MateriaTipoJuicioOut])
async def listado_materias_tipos_juicios(
    materia_id: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Tipos de Juicios"""
    try:
        listado = get_materias_tipos_juicios(db, materia_id=materia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@materias_tipos_juicios.get("/{materia_tipo_juicio_id}", response_model=MateriaTipoJuicioOut)
async def detalle_materia_tipo_juicio(
    materia_tipo_juicio_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Tipo de Juicio a partir de su id"""
    try:
        materia_tipo_juicio = get_materia_tipo_juicio(db, materia_tipo_juicio_id=materia_tipo_juicio_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaTipoJuicioOut.from_orm(materia_tipo_juicio)
