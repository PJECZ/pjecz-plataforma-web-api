"""
Glosas, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_glosa, get_glosas
from .schemas import GlosaOut

glosas = APIRouter()


@glosas.get("", response_model=List[GlosaOut])
async def listar_glosas(
    autoridad_id: int,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Lista de glosas"""
    resultados = []
    try:
        for glosa, autoridad, distrito in get_glosas(db, autoridad_id=autoridad_id, ano=ano):
            resultados.append(
                GlosaOut(
                    id=glosa.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    fecha=glosa.fecha,
                    tipo_juicio=glosa.tipo_juicio,
                    expediente=glosa.expediente,
                    descripcion=glosa.descripcion,
                    archivo=glosa.archivo,
                    url=glosa.url,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@glosas.get("/{glosa_id}", response_model=GlosaOut)
async def consultar_un_glosa(glosa_id: int, db: Session = Depends(get_db)):
    """Consultar un glosa"""
    try:
        glosa = get_glosa(db, glosa_id=glosa_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return GlosaOut(
        id=glosa.id,
        distrito_id=glosa.autoridad.distrito.id,
        distrito=glosa.autoridad.distrito.nombre,
        autoridad_id=glosa.autoridad.id,
        autoridad=glosa.autoridad.descripcion,
        fecha=glosa.fecha,
        descripcion=glosa.descripcion,
        tipo_juicio=glosa.tipo_juicio,
        expediente=glosa.expediente,
        archivo=glosa.archivo,
        url=glosa.url,
    )
