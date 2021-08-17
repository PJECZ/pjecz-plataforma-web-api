"""
Sentencias, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_sentencia, get_sentencias
from .schemas import SentenciaOut

router = APIRouter()


@router.get("", response_model=List[SentenciaOut])
async def listar_sentencias(
    autoridad_id: int,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Lista de sentencias"""
    resultados = []
    try:
        for sentencia, autoridad, distrito in get_sentencias(db, autoridad_id=autoridad_id, ano=ano):
            resultados.append(
                SentenciaOut(
                    id=sentencia.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    fecha=sentencia.fecha,
                    sentencia=sentencia.sentencia,
                    expediente=sentencia.expediente,
                    es_perspectiva_genero=sentencia.es_perspectiva_genero,
                    archivo=sentencia.archivo,
                    url=sentencia.url,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{sentencia_id}", response_model=SentenciaOut)
async def consultar_un_sentencia(sentencia_id: int, db: Session = Depends(get_db)):
    """Consultar un sentencia"""
    try:
        sentencia = get_sentencia(db, sentencia_id=sentencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return SentenciaOut(
        id=sentencia.id,
        distrito_id=sentencia.autoridad.distrito.id,
        distrito=sentencia.autoridad.distrito.nombre,
        autoridad_id=sentencia.autoridad.id,
        autoridad=sentencia.autoridad.descripcion,
        fecha=sentencia.fecha,
        sentencia=sentencia.sentencia,
        expediente=sentencia.expediente,
        es_perspectiva_genero=sentencia.es_perspectiva_genero,
        archivo=sentencia.archivo,
        url=sentencia.url,
    )
