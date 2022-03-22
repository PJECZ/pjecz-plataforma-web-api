"""
REPSVM Delitos Genericos, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_repsvm_delito_generico, get_repsvm_delitos_genericos
from .schemas import REPSVMDelitoGenericoOut

repsvm_delitos_genericos = APIRouter()


@repsvm_delitos_genericos.get('', response_model=List[REPSVMDelitoGenericoOut])
async def listar_repsvm_delitos_genericos(db: Session = Depends(get_db)):
    """ Lista de repsvm_delitos_genericos """
    resultados = []
    try:
        for repsvm_delito_generico in get_repsvm_delitos_genericos(db):
            resultados.append(REPSVMDelitoGenericoOut(id=repsvm_delito_generico.id, delito_generico=repsvm_delito_generico.nombre))
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f'Not found: {str(error)}') from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f'Not acceptable: {str(error)}') from error
    return resultados


@repsvm_delitos_genericos.get('/{repsvm_delito_generico_id}', response_model=REPSVMDelitoGenericoOut)
async def consultar_un_repsvm_delito_generico(repsvm_delito_generico_id: int, db: Session = Depends(get_db)):
    """ Consultar un repsvm_delito_generico """
    try:
        repsvm_delito_generico = get_repsvm_delito_generico(db, repsvm_delito_generico_id=repsvm_delito_generico_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f'Not found: {str(error)}') from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f'Not acceptable: {str(error)}') from error
    return REPSVMDelitoGenericoOut(id=repsvm_delito_generico.id, delito_generico=repsvm_delito_generico.nombre)
