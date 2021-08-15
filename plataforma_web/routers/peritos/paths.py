"""
Peritos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_perito, get_peritos
from .schemas import PeritoOut

router = APIRouter()


@router.get("", response_model=List[PeritoOut])
async def listar_peritos(
    distrito_id: int,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """Lista de Peritos"""
    resultados = []
    try:
        for perito, distrito in get_peritos(db, distrito_id=distrito_id, nombre=nombre):
            resultados.append(
                PeritoOut(
                    id=perito.id,
                    distrito_id=perito.distrito_id,
                    distrito=distrito.nombre,
                    nombre=perito.nombre,
                    tipo=perito.tipo,
                    domicilio=perito.domicilio,
                    telefono_fijo=perito.telefono_fijo,
                    telefono_celular=perito.telefono_celular,
                    email=perito.email,
                    notas=perito.notas,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{perito_id}", response_model=PeritoOut)
async def consultar_un_perito(perito_id: int, db: Session = Depends(get_db)):
    """Consultar un Perito"""
    try:
        perito = get_perito(db, perito_id=perito_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return PeritoOut(
        id=perito.id,
        distrito_id=perito.distrito_id,
        distrito=perito.distrito.nombre,
        nombre=perito.nombre,
        tipo=perito.tipo,
        domicilio=perito.domicilio,
        telefono_fijo=perito.telefono_fijo,
        telefono_celular=perito.telefono_celular,
        email=perito.email,
        notas=perito.notas,
    )
