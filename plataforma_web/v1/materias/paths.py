"""
Materias, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_materia, get_materias
from .schemas import MateriaOut

materias = APIRouter()


@materias.get("", response_model=List[MateriaOut])
async def listar_materias(db: Session = Depends(get_db)):
    """Lista de materias"""
    resultados = []
    for materia in get_materias(db):
        resultados.append(MateriaOut(id=materia.id, materia=materia.nombre))
    return resultados


@materias.get("/{materia_id}", response_model=MateriaOut)
async def consultar_una_materia(materia_id: int, db: Session = Depends(get_db)):
    """Consultar un materia"""
    try:
        materia = get_materia(db, materia_id=materia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaOut(id=materia.id, materia=materia.nombre)
