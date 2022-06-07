"""
REPSVM Tipos de Sentencias, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_repsvm_tipo_sentencia, get_repsvm_tipos_sentencias
from .schemas import REPSVMTipoSentenciaOut

repsvm_tipos_sentencias = APIRouter()


@repsvm_tipos_sentencias.get("", response_model=List[REPSVMTipoSentenciaOut])
async def listar_repsvm_tipos_sentencias(db: Session = Depends(get_db)):
    """Lista de repsvm_tipos_sentencias"""
    resultados = []
    try:
        for repsvm_tipo_sentencia in get_repsvm_tipos_sentencias(db):
            resultados.append(
                REPSVMTipoSentenciaOut(
                    id=repsvm_tipo_sentencia.id,
                    tipo_sentencia=repsvm_tipo_sentencia.nombre,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@repsvm_tipos_sentencias.get("/{repsvm_tipo_sentencia_id}", response_model=REPSVMTipoSentenciaOut)
async def consultar_un_repsvm_tipo_sentencia(repsvm_tipo_sentencia_id: int, db: Session = Depends(get_db)):
    """Consultar un repsvm_tipo_sentencia"""
    try:
        repsvm_tipo_sentencia = get_repsvm_tipo_sentencia(db, repsvm_tipo_sentencia_id=repsvm_tipo_sentencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMTipoSentenciaOut(id=repsvm_tipo_sentencia.id, tipo_sentencia=repsvm_tipo_sentencia.nombre)
