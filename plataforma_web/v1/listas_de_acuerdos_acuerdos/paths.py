"""
Listas de Acuerdos Acuerdos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_lista_de_acuerdo_acuerdo, get_listas_de_acuerdos_acuerdos
from .schemas import ListaDeAcuerdoAcuerdoOut

listas_de_acuerdos_acuerdos = APIRouter()


@listas_de_acuerdos_acuerdos.get("", response_model=List[ListaDeAcuerdoAcuerdoOut])
async def listar_listas_de_acuerdos_acuerdos(
    lista_de_acuerdo_id: int,
    db: Session = Depends(get_db),
):
    """Lista de listas_de_acuerdos_acuerdos"""
    resultados = []
    try:
        for acuerdo, lista_de_acuerdo in get_listas_de_acuerdos_acuerdos(db, lista_de_acuerdo_id=lista_de_acuerdo_id):
            resultados.append(
                ListaDeAcuerdoAcuerdoOut(
                    id=acuerdo.id,
                    lista_de_acuerdo_id=lista_de_acuerdo.id,
                    fecha=lista_de_acuerdo.fecha,
                    folio=acuerdo.folio,
                    expediente=acuerdo.expediente,
                    actor=acuerdo.actor,
                    demandado=acuerdo.demandado,
                    tipo_acuerdo=acuerdo.tipo_acuerdo,
                    tipo_juicio=acuerdo.tipo_juicio,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@listas_de_acuerdos_acuerdos.get("/{lista_de_acuerdo_acuerdo_id}", response_model=ListaDeAcuerdoAcuerdoOut)
async def consultar_un_acuerdo(lista_de_acuerdo_acuerdo_id: int, db: Session = Depends(get_db)):
    """Consultar un acuerdo"""
    try:
        acuerdo = get_lista_de_acuerdo_acuerdo(db, lista_de_acuerdo_acuerdo_id=lista_de_acuerdo_acuerdo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return ListaDeAcuerdoAcuerdoOut(
        id=acuerdo.id,
        lista_de_acuerdo_id=acuerdo.lista_de_acuerdo_id,
        fecha=acuerdo.lista_de_acuerdo.fecha,
        folio=acuerdo.folio,
        expediente=acuerdo.expediente,
        actor=acuerdo.actor,
        demandado=acuerdo.demandado,
        tipo_acuerdo=acuerdo.tipo_acuerdo,
        tipo_juicio=acuerdo.tipo_juicio,
    )
