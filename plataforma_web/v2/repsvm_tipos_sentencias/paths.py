"""
REPSVM Tipos de Sentencias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination_datatable import LimitOffsetPage

from .crud import get_repsvm_tipos_sentencias, get_repsvm_tipo_sentencia
from .schemas import REPSVMTipoSentenciaOut

repsvm_tipos_sentencias = APIRouter()


@repsvm_tipos_sentencias.get("", response_model=LimitOffsetPage[REPSVMTipoSentenciaOut])
async def listado_repsvm_tipos_sentencias(
    db: Session = Depends(get_db),
):
    """Listado de Tipos de Sentencias"""
    try:
        listado = get_repsvm_tipos_sentencias(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@repsvm_tipos_sentencias.get("/{repsvm_tipo_sentencia_id}", response_model=REPSVMTipoSentenciaOut)
async def detalle_repsvm_tipo_sentencia(
    repsvm_tipo_sentencia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Tipo de Sentencia a partir de su id"""
    try:
        repsvm_tipo_sentencia = get_repsvm_tipo_sentencia(db, repsvm_tipo_sentencia_id=repsvm_tipo_sentencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMTipoSentenciaOut.from_orm(repsvm_tipo_sentencia)
