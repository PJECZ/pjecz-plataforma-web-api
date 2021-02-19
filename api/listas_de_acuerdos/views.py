"""
Listas de Acuerdos, vistas
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from lib.database import get_db
from api.listas_de_acuerdos import crud, schemas

router = APIRouter()


@router.get("", response_model=List[schemas.ListaDeAcuerdo])
async def listar_listas_de_acuerdos(autoridad_id: int, db: Session = Depends(get_db)):
    """ Consultar Listas de Acuerdos """
    autoridad = crud.get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    return crud.get_listas_de_acuerdos(db, autoridad_id=autoridad_id)


@router.post("/nuevo", response_model=schemas.ListaDeAcuerdo)
async def nueva_lista_de_acuerdo(lista_de_acuerdo: schemas.ListaDeAcuerdoNew, db: Session = Depends(get_db)):
    """ Nueva Lista de Acuerdos """
    return crud.new_lista_de_acuerdo(db, esquema=lista_de_acuerdo)
