"""
Materias, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from . import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Materia])
async def listar_materias(db: Session = Depends(get_db)):
    """Lista de materias"""
    resultados = []
    for materia in crud.get_materias(db):
        resultados.append(schemas.Materia(id=materia.id, materia=materia.nombre))
    return resultados


@router.get("/{materia_id}", response_model=schemas.Materia)
async def consultar_un_materia(materia_id: int, db: Session = Depends(get_db)):
    """Consultar un materia"""
    try:
        materia = crud.get_materia(db, materia_id=materia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return schemas.Materia(id=materia.id, materia=materia.nombre)
