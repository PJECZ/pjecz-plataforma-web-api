"""
Tesis Jurisprudencias v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.tesis_jurisprudencias.crud import get_tesis_jurisprudencias, get_tesis_jurisprudencia
from plataforma_web.v2.tesis_jurisprudencias.schemas import TesisJurisprudenciaOut

tesis_jurisprudencias = APIRouter()


@tesis_jurisprudencias.get("", response_model=LimitOffsetPage[TesisJurisprudenciaOut])
async def listado_tesis_jurisprudencias(
    autoridad_id: int = None,
    epoca_id: int = None,
    materia_id: int = None,
    clase: str = None,
    titulo: str = None,
    texto: str = None,
    aprobacion_anio: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Tesis Jurisprudencias"""
    try:
        listado = get_tesis_jurisprudencias(db, autoridad_id, epoca_id, materia_id, clase, titulo, texto, aprobacion_anio)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@tesis_jurisprudencias.get("/{tesis_jurisprudencia_id}", response_model=TesisJurisprudenciaOut)
async def detalle_tesis_jurisprudencia(
    tesis_jurisprudencia_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Tesis Jurisprudencia a partir de su id"""
    try:
        tesis_jurisprudencia = get_tesis_jurisprudencia(db, tesis_jurisprudencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return TesisJurisprudenciaOut.from_orm(tesis_jurisprudencia)
