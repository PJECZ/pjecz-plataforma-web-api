"""
Abogados, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from plataforma_web.abogados import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Abogado])
async def listar_abogados(nombre: str, ano_desde: int = None, ano_hasta: int = None, db: Session = Depends(get_db)):
    """Lista de Abogados"""
    return crud.get_abogados(db, nombre=nombre, ano_desde=ano_desde, ano_hasta=ano_hasta)


@router.get("/{abogado_id}", response_model=schemas.Abogado)
async def consultar_un_abogado(abogado_id: int, db: Session = Depends(get_db)):
    """Consultar un Abogado"""
    try:
        abogado = crud.get_abogado(db, abogado_id=abogado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return abogado
