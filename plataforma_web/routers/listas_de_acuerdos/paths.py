"""
Listas de Acuerdos, vistas
"""
from datetime import date
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_lista_de_acuerdo, get_listas_de_acuerdos
from .schemas import ListaDeAcuerdoOut

router = APIRouter()


@router.get("", response_model=List[ListaDeAcuerdoOut])
async def listar_listas_de_acuerdos(
    autoridad_id: int,
    fecha: date = None,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Lista de Listas de Acuerdos"""
    resultados = []
    try:
        for lista_de_acuerdo, autoridad, distrito in get_listas_de_acuerdos(db, autoridad_id=autoridad_id, fecha=fecha, ano=ano):
            resultados.append(
                ListaDeAcuerdoOut(
                    id=lista_de_acuerdo.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    fecha=lista_de_acuerdo.fecha,
                    descripcion=lista_de_acuerdo.descripcion,
                    archivo=lista_de_acuerdo.archivo,
                    url=lista_de_acuerdo.url,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{lista_de_acuerdo_id}", response_model=ListaDeAcuerdoOut)
async def consultar_una_lista_de_acuerdos(lista_de_acuerdo_id: int, db: Session = Depends(get_db)):
    """Consultar una Lista de Acuerdos"""
    try:
        lista_de_acuerdo = get_lista_de_acuerdo(db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return ListaDeAcuerdoOut(
        id=lista_de_acuerdo.id,
        distrito_id=lista_de_acuerdo.autoridad.distrito_id,
        distrito=lista_de_acuerdo.autoridad.distrito.nombre,
        autoridad_id=lista_de_acuerdo.autoridad_id,
        autoridad=lista_de_acuerdo.autoridad.descripcion,
        fecha=lista_de_acuerdo.fecha,
        descripcion=lista_de_acuerdo.descripcion,
        archivo=lista_de_acuerdo.archivo,
        url=lista_de_acuerdo.url,
    )
