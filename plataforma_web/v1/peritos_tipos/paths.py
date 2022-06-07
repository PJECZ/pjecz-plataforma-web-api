"""
Peritos Tipos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_perito_tipo, get_peritos_tipos
from .schemas import PeritoTipoOut

peritos_tipos = APIRouter()


@peritos_tipos.get("", response_model=List[PeritoTipoOut])
async def listar_peritos_tipos(db: Session = Depends(get_db)):
    """Lista de peritos_tipos"""
    resultados = []
    try:
        for perito_tipo in get_peritos_tipos(db):
            resultados.append(PeritoTipoOut(id=perito_tipo.id, perito_tipo=perito_tipo.nombre))
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@peritos_tipos.get("/{perito_tipo_id}", response_model=PeritoTipoOut)
async def consultar_un_perito_tipo(perito_tipo_id: int, db: Session = Depends(get_db)):
    """Consultar un perito_tipo"""
    try:
        perito_tipo = get_perito_tipo(db, perito_tipo_id=perito_tipo_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return PeritoTipoOut(id=perito_tipo.id, perito_tipo=perito_tipo.nombre)
