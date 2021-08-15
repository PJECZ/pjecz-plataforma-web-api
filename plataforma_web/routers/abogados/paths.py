"""
Abogados, paths
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_abogado, get_abogados
from .schemas import AbogadoOut

router = APIRouter()


@router.get("", response_model=List[AbogadoOut])
async def listar_abogados(
    nombre: str,
    ano_desde: int = None,
    ano_hasta: int = None,
    db: Session = Depends(get_db),
):
    """Lista de Abogados"""
    return get_abogados(db, nombre=nombre, ano_desde=ano_desde, ano_hasta=ano_hasta)


@router.get("/{abogado_id}", response_model=AbogadoOut)
async def consultar_un_abogado(abogado_id: int, db: Session = Depends(get_db)):
    """Consultar un Abogado"""
    try:
        abogado = get_abogado(db, abogado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return abogado
