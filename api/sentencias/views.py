"""
Sentencias, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.autoridades.crud import get_autoridad
from api.sentencias import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Sentencia])
async def listar_sentencias(autoridad_id: int, ano: int = None, db: Session = Depends(get_db)):
    """Lista de sentencias"""
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    resultados = []
    for sentencia, autoridad, distrito in crud.get_sentencias(db, autoridad_id=autoridad_id, ano=ano):
        resultados.append(
            schemas.Sentencia(
                id=sentencia.id,
                distrito_id=distrito.id,
                distrito=distrito.nombre,
                autoridad_id=autoridad.id,
                autoridad=autoridad.descripcion,
                fecha=sentencia.fecha,
                sentencia=sentencia.sentencia,
                expediente=sentencia.expediente,
                es_paridad_genero=sentencia.es_paridad_genero,
                archivo=sentencia.archivo,
                url=sentencia.url,
            )
        )
    return resultados


@router.get("/{sentencia_id}", response_model=schemas.Sentencia)
async def consultar_un_sentencia(sentencia_id: int, db: Session = Depends(get_db)):
    """Consultar un sentencia"""
    sentencia = crud.get_sentencia(db, sentencia_id=sentencia_id)
    if sentencia is None:
        raise HTTPException(status_code=400, detail="No existe el sentencia.")
    return schemas.Sentencia(
        id=sentencia.id,
        distrito_id=sentencia.autoridad.distrito.id,
        distrito=sentencia.autoridad.distrito.nombre,
        autoridad_id=sentencia.autoridad.id,
        autoridad=sentencia.autoridad.descripcion,
        fecha=sentencia.fecha,
        sentencia=sentencia.sentencia,
        expediente=sentencia.expediente,
        es_paridad_genero=sentencia.es_paridad_genero,
        archivo=sentencia.archivo,
        url=sentencia.url,
    )
