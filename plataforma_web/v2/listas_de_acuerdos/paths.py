"""
Listas de Acuerdos v2, rutas (paths)
"""
from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.orm import Session

from lib.database import get_db
from lib.fastapi_pagination import LimitOffsetPage

from plataforma_web.v2.listas_de_acuerdos.crud import get_listas_de_acuerdos, get_lista_de_acuerdo
from plataforma_web.v2.listas_de_acuerdos.schemas import ListaDeAcuerdoOut

listas_de_acuerdos = APIRouter()


@listas_de_acuerdos.get("", response_model=LimitOffsetPage[ListaDeAcuerdoOut])
async def listado_listas_de_acuerdos(
    autoridad_id: int = None,
    fecha: date = None,
    anio: int = None,
    db: Session = Depends(get_db),
):
    """Listado de Listas de Acuerdos"""
    try:
        listado = get_listas_de_acuerdos(db, autoridad_id=autoridad_id, fecha=fecha, anio=anio)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return paginate(listado)


@listas_de_acuerdos.get("/{lista_de_acuerdo_id}", response_model=ListaDeAcuerdoOut)
async def detalle_lista_de_acuerdo(
    lista_de_acuerdo_id: int,
    db: Session = Depends(get_db),
):
    """Detalle de un Lista de Acuerdo a partir de su id"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return ListaDeAcuerdoOut.from_orm(lista_de_acuerdo)
