"""
REPSVM Delitos Especificos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_repsvm_delito_especifico, get_repsvm_delitos_especificos
from .schemas import REPSVMDelitoEspecificoOut

repsvm_delitos_especificos = APIRouter()


@repsvm_delitos_especificos.get("", response_model=List[REPSVMDelitoEspecificoOut])
async def listar_repsvm_delitos_especificos(db: Session = Depends(get_db)):
    """Lista de repsvm_delitos_especificos"""
    resultados = []
    try:
        for repsvm_delito_especifico in get_repsvm_delitos_especificos(db):
            resultados.append(
                REPSVMDelitoEspecificoOut(
                    id=repsvm_delito_especifico.id,
                    delito_generico_id=repsvm_delito_especifico.repsvm_delito_generico_id,
                    delito_generico=repsvm_delito_especifico.repsvm_delito_generico.nombre,
                    delito_especifico=repsvm_delito_especifico.descripcion,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@repsvm_delitos_especificos.get("/{repsvm_delito_especifico_id}", response_model=REPSVMDelitoEspecificoOut)
async def consultar_un_repsvm_delito_especifico(repsvm_delito_especifico_id: int, db: Session = Depends(get_db)):
    """Consultar un repsvm_delito_especifico"""
    try:
        repsvm_delito_especifico = get_repsvm_delito_especifico(db, repsvm_delito_especifico_id=repsvm_delito_especifico_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMDelitoEspecificoOut(
        id=repsvm_delito_especifico.id,
        delito_generico_id=repsvm_delito_especifico.repsvm_delito_generico_id,
        delito_generico=repsvm_delito_especifico.repsvm_delito_generico.nombre,
        repsvm_delito_especifico=repsvm_delito_especifico.descripcion,
    )
