"""
Distritos, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from plataforma_web.distritos import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Distrito])
async def listar_distritos(solo_distritos: bool = False, db: Session = Depends(get_db)):
    """Lista de Distritos"""
    resultados = []
    for distrito in crud.get_distritos(db, solo_distritos=solo_distritos):
        resultados.append(
            schemas.Distrito(
                id=distrito.id,
                distrito=distrito.nombre,
                distrito_corto=distrito.nombre_corto,
            )
        )
    return resultados


@router.get("/{distrito_id}", response_model=schemas.Distrito)
async def consultar_un_distrito(distrito_id: int, db: Session = Depends(get_db)):
    """Consultar un Distrito"""
    try:
        distrito = crud.get_distrito(db, distrito_id=distrito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return schemas.Distrito(
        id=distrito.id,
        distrito=distrito.nombre,
        distrito_corto=distrito.nombre_corto,
    )
