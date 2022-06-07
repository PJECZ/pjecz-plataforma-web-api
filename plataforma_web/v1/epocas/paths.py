"""
Epocas, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_epoca, get_epocas
from .schemas import EpocaOut

epocas = APIRouter()


@epocas.get("", response_model=List[EpocaOut])
async def listar_epocas(db: Session = Depends(get_db)):
    """Lista de epocas"""
    resultados = []
    for epoca in get_epocas(db):
        resultados.append(EpocaOut(id=epoca.id, epoca=epoca.nombre))
    return resultados


@epocas.get("/{epoca_id}", response_model=EpocaOut)
async def consultar_un_epoca(epoca_id: int, db: Session = Depends(get_db)):
    """Consultar una epoca"""
    try:
        epoca = get_epoca(db, epoca_id=epoca_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return EpocaOut(id=epoca.id, epoca=epoca.nombre)
