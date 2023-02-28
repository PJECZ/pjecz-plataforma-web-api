"""
Autoridades v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from .crud import get_autoridades, get_autoridad, get_cemascs, get_defensorias
from .schemas import AutoridadOut

autoridades = APIRouter()


@autoridades.get("/cemascs", response_model=LimitOffsetPage[AutoridadOut])
async def listado_cemascs(
    db: Session = Depends(get_db),
):
    """Listado de Centros de Medios Alternos de Solución de Controversias"""
    try:
        listado = get_cemascs(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@autoridades.get("/defensorias", response_model=LimitOffsetPage[AutoridadOut])
async def listado_defensorias(
    db: Session = Depends(get_db),
):
    """Listado de Defensorias"""
    try:
        listado = get_defensorias(db)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@autoridades.get("/{autoridad_id}", response_model=AutoridadOut)
async def detalle_autoridad(
    autoridad_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Autoridad a partir de su id"""
    try:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AutoridadOut.from_orm(autoridad)


@autoridades.get("", response_model=LimitOffsetPage[AutoridadOut])
async def listado_autoridades(
    distrito_id: int = None,
    materia_id: int = None,
    organo_jurisdiccional: str = None,
    con_notarias: bool = False,
    para_glosas: bool = False,
    db: Session = Depends(get_db),
):
    """Listado de Autoridades"""
    try:
        listado = get_autoridades(
            db,
            distrito_id=distrito_id,
            materia_id=materia_id,
            organo_jurisdiccional=organo_jurisdiccional,
            con_notarias=con_notarias,
            para_glosas=para_glosas,
        )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)
