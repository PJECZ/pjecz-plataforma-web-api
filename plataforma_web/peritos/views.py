"""
Peritos, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from plataforma_web.peritos import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Perito])
async def listar_peritos(distrito_id: int, nombre: str = None, db: Session = Depends(get_db)):
    """Lista de Peritos"""
    resultados = []
    for perito, distrito in crud.get_peritos(db, distrito_id=distrito_id, nombre=nombre):
        resultados.append(
            schemas.Perito(
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
    return resultados


@router.get("/{perito_id}", response_model=schemas.Perito)
async def consultar_un_perito(perito_id: int, db: Session = Depends(get_db)):
    """Consultar un Perito"""
    perito = crud.get_perito(db, perito_id=perito_id)
    if perito is None:
        raise HTTPException(status_code=400, detail="No existe el perito.")
    return schemas.Perito(
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
