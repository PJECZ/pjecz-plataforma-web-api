"""
Distritos, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.distritos import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Distrito])
async def listar_distritos(db: Session = Depends(get_db)):
    """ Lista de Distritos """
    resultados = []
    for distrito in crud.get_distritos(db):
        resultados.append(schemas.Distrito(id=distrito.id, distrito=distrito.nombre))
    return resultados


@router.get("/{distrito_id}", response_model=schemas.Distrito)
async def consultar_un_distrito(distrito_id: int, db: Session = Depends(get_db)):
    """ Consultar un Distrito """
    distrito = crud.get_distrito(db, distrito_id=distrito_id)
    if distrito is None:
        raise HTTPException(status_code=400, detail="No existe el distrito.")
    return schemas.Distrito(id=distrito.id, distrito=distrito.nombre)
