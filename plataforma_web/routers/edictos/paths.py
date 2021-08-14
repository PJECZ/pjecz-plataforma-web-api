"""
Edictos, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..autoridades.crud import get_autoridad
from . import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Edicto])
async def listar_edictos(autoridad_id: int, ano: int = None, db: Session = Depends(get_db)):
    """Lista de Edictos"""
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    resultados = []
    for edicto, autoridad, distrito in crud.get_edictos(db, autoridad_id=autoridad_id, ano=ano):
        resultados.append(
            schemas.Edicto(
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
    return resultados


@router.get("/{edicto_id}", response_model=schemas.Edicto)
async def consultar_un_edicto(edicto_id: int, db: Session = Depends(get_db)):
    """Consultar un Edicto"""
    try:
        edicto = crud.get_edicto(db, edicto_id=edicto_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return schemas.Edicto(
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
