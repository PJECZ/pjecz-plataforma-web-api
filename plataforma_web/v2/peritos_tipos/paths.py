"""
Peritos Tipos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.peritos_tipos.crud import get_peritos_tipos, get_perito_tipo
from plataforma_web.v2.peritos_tipos.schemas import PeritoTipoOut

peritos_tipos = APIRouter()


@peritos_tipos.get("", response_model=LimitOffsetPage[PeritoTipoOut])
async def listado_peritos_tipos(db: Session = Depends(get_db)):
    """Listado de Tipos de Peritos"""
    try:
        listado = get_peritos_tipos(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@peritos_tipos.get("/{perito_tipo_id}", response_model=PeritoTipoOut)
async def detalle_perito_tipo(
    perito_tipo_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Tipo de Perito a partir de su id"""
    try:
        perito_tipo = get_perito_tipo(db, perito_tipo_id=perito_tipo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return PeritoTipoOut.from_orm(perito_tipo)
