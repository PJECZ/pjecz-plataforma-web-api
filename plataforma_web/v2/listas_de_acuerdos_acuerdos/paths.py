"""
Listas de Acuerdos Acuerdos v2, rutas (paths)
"""
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.listas_de_acuerdos_acuerdos.crud import get_listas_de_acuerdos_acuerdos, get_lista_de_acuerdo_acuerdo
from plataforma_web.v2.listas_de_acuerdos_acuerdos.schemas import ListaDeAcuerdoAcuerdoOut

listas_de_acuerdos_acuerdos = APIRouter()


@listas_de_acuerdos_acuerdos.get("", response_model=LimitOffsetPage[ListaDeAcuerdoAcuerdoOut])
async def listado_listas_de_acuerdos_acuerdos(
    lista_de_acuerdo_id: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Acuerdos"""
    try:
        listado = get_listas_de_acuerdos_acuerdos(db, lista_de_acuerdo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@listas_de_acuerdos_acuerdos.get("/{lista_de_acuerdo_id}", response_model=ListaDeAcuerdoAcuerdoOut)
async def detalle_lista_de_acuerdo(
    lista_de_acuerdo_acuerdo_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Acuerdo a partir de su id"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo_acuerdo(db, lista_de_acuerdo_acuerdo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return ListaDeAcuerdoAcuerdoOut.from_orm(lista_de_acuerdo)
