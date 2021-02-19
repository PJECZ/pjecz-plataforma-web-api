"""
Listas de Acuerdos, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.autoridades.crud import get_autoridad
from api.listas_de_acuerdos import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.ListaDeAcuerdo])
async def listar_listas_de_acuerdos(autoridad_id: int, db: Session = Depends(get_db)):
    """ Lista de Listas de Acuerdos """
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    return crud.get_listas_de_acuerdos(db, autoridad_id=autoridad_id)


@router.get("/", response_model=schemas.ListaDeAcuerdo)
async def consultar_una_lista_de_acuerdos(lista_de_acuerdo_id: int, db: Session = Depends(get_db)):
    """ Consultar una Lista de Acuerdos """
    lista_de_acuerdo = crud.get_lista_de_acuerdo(db, lista_de_acuerdo_id=lista_de_acuerdo_id)
    if lista_de_acuerdo is None:
        raise HTTPException(status_code=400, detail="No existe la lista de acuerdos.")
    return lista_de_acuerdo


@router.post("/nuevo", response_model=schemas.ListaDeAcuerdo)
async def nueva_lista_de_acuerdo(lista_de_acuerdo: schemas.ListaDeAcuerdoNew, db: Session = Depends(get_db)):
    """ Nueva Lista de Acuerdos """
    return crud.new_lista_de_acuerdo(db, esquema=lista_de_acuerdo)
