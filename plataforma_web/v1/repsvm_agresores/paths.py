"""
REPSVM Agresores, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_repsvm_agresor, get_repsvm_agresores
from .schemas import REPSVMAgresorOut

repsvm_agresores = APIRouter()


@repsvm_agresores.get("", response_model=List[REPSVMAgresorOut])
async def listar_repsvm_agresores(
    distrito_id: int,
    nombre: str = None,
    db: Session = Depends(get_db),
):
    """Lista de repsvm_agresores"""
    resultados = []
    try:
        for repsvm_agresor in get_repsvm_agresores(db, distrito_id=distrito_id, nombre=nombre):
            resultados.append(
                REPSVMAgresorOut(
                    id=repsvm_agresor.id,
                    distrito_id=repsvm_agresor.distrito_id,
                    distrito=repsvm_agresor.distrito.nombre,
                    materia_tipo_juzgado_id=repsvm_agresor.materia_tipo_juzgado_id,
                    materia_tipo_juzgado=repsvm_agresor.materia_tipo_juzgado.descripcion,
                    delito_generico_id=repsvm_agresor.repsvm_delito_especifico.repsvm_delito_generico_id,
                    delito_generico=repsvm_agresor.repsvm_delito_especifico.repsvm_delito_generico.nombre,
                    delito_especifico_id=repsvm_agresor.repsvm_delito_especifico_id,
                    delito_especifico=repsvm_agresor.repsvm_delito_especifico.descripcion,
                    tipo_sentencia_id=repsvm_agresor.repsvm_tipo_sentencia_id,
                    tipo_sentencia=repsvm_agresor.repsvm_tipo_sentencia.nombre,
                    nombre=repsvm_agresor.nombre,
                    numero_causa=repsvm_agresor.numero_causa,
                    pena_impuesta=repsvm_agresor.pena_impuesta,
                    observaciones=repsvm_agresor.observaciones,
                    sentencia_url=repsvm_agresor.sentencia_url,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@repsvm_agresores.get("/{repsvm_agresor_id}", response_model=REPSVMAgresorOut)
async def consultar_un_repsvm_agresor(repsvm_agresor_id: int, db: Session = Depends(get_db)):
    """Consultar un repsvm_agresor"""
    try:
        repsvm_agresor = get_repsvm_agresor(db, repsvm_agresor_id=repsvm_agresor_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return REPSVMAgresorOut(
        id=repsvm_agresor.id,
        distrito_id=repsvm_agresor.distrito_id,
        distrito=repsvm_agresor.distrito.nombre,
        materia_tipo_juzgado_id=repsvm_agresor.materia_tipo_juzgado_id,
        materia_tipo_juzgado=repsvm_agresor.materia_tipo_juzgado.descripcion,
        delito_generico_id=repsvm_agresor.repsvm_delito_especifico.repsvm_delito_generico_id,
        delito_generico=repsvm_agresor.repsvm_delito_especifico.repsvm_delito_generico.nombre,
        delito_especifico_id=repsvm_agresor.repsvm_delito_especifico_id,
        delito_especifico=repsvm_agresor.repsvm_delito_especifico.descripcion,
        tipo_sentencia_id=repsvm_agresor.repsvm_tipo_sentencia_id,
        tipo_sentencia=repsvm_agresor.repsvm_tipo_sentencia.nombre,
        nombre=repsvm_agresor.nombre,
        numero_causa=repsvm_agresor.numero_causa,
        pena_impuesta=repsvm_agresor.pena_impuesta,
        observaciones=repsvm_agresor.observaciones,
        sentencia_url=repsvm_agresor.sentencia_url,
    )
