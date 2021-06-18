"""
Autoriades, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.autoridades import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Autoridad])
async def listar_autoridades(distrito_id: int = None, con_notarias: bool = False, para_glosas: bool = False, db: Session = Depends(get_db)):
    """ Lista de Autoridades """
    resultados = []
    for autoridad, distrito in crud.get_autoridades(db, distrito_id=distrito_id, con_notarias=con_notarias, para_glosas=para_glosas):
        resultados.append(
            schemas.Autoridad(
                id=autoridad.id,
                distrito_id=autoridad.distrito_id,
                distrito=distrito.nombre,
                autoridad=autoridad.descripcion,
            )
        )
    return resultados


@router.get("/{autoridad_id}", response_model=schemas.Autoridad)
async def consultar_una_autoridad(autoridad_id: int, db: Session = Depends(get_db)):
    """ Consultar una Autoridad """
    autoridad = crud.get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    return schemas.Autoridad(
        id=autoridad.id,
        distrito_id=autoridad.distrito_id,
        distrito=autoridad.distrito.nombre,
        autoridad=autoridad.descripcion,
    )
