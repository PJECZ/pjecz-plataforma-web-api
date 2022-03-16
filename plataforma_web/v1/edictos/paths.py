"""
Edictos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_edicto, get_edictos
from .schemas import EdictoOut

edictos = APIRouter()


@edictos.get("", response_model=List[EdictoOut])
async def listar_edictos(
    autoridad_id: int,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Lista de Edictos"""
    resultados = []
    try:
        for edicto, autoridad, distrito in get_edictos(db, autoridad_id=autoridad_id, ano=ano):
            resultados.append(
                EdictoOut(
                    id=edicto.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    fecha=edicto.fecha,
                    descripcion=edicto.descripcion,
                    expediente=edicto.expediente,
                    numero_publicacion=edicto.numero_publicacion,
                    archivo=edicto.archivo,
                    url=edicto.url,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@edictos.get("/{edicto_id}", response_model=EdictoOut)
async def consultar_un_edicto(edicto_id: int, db: Session = Depends(get_db)):
    """Consultar un Edicto"""
    try:
        edicto = get_edicto(db, edicto_id=edicto_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return EdictoOut(
        id=edicto.id,
        distrito_id=edicto.autoridad.distrito_id,
        distrito=edicto.autoridad.distrito.nombre,
        autoridad_id=edicto.autoridad.id,
        autoridad=edicto.autoridad.descripcion,
        fecha=edicto.fecha,
        descripcion=edicto.descripcion,
        expediente=edicto.expediente,
        numero_publicacion=edicto.numero_publicacion,
        archivo=edicto.archivo,
        url=edicto.url,
    )
