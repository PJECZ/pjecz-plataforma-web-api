"""
Distritos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_distrito, get_distritos
from .schemas import DistritoOut

router = APIRouter()


@router.get("", response_model=List[DistritoOut])
async def listar_distritos(
    solo_distritos: bool = False,
    db: Session = Depends(get_db),
):
    """Lista de Distritos"""
    resultados = []
    for distrito in get_distritos(db, solo_distritos=solo_distritos):
        resultados.append(
            DistritoOut(
                id=distrito.id,
                distrito=distrito.nombre,
                distrito_corto=distrito.nombre_corto,
            )
        )
    return resultados


@router.get("/{distrito_id}", response_model=DistritoOut)
async def consultar_un_distrito(distrito_id: int, db: Session = Depends(get_db)):
    """Consultar un Distrito"""
    try:
        distrito = get_distrito(db, distrito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return DistritoOut(
        id=distrito.id,
        distrito=distrito.nombre,
        distrito_corto=distrito.nombre_corto,
    )
