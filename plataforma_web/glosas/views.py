"""
Glosas, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from plataforma_web.autoridades.crud import get_autoridad
from plataforma_web.glosas import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get("", response_model=List[schemas.Glosa])
async def listar_glosas(autoridad_id: int, ano: int = None, db: Session = Depends(get_db)):
    """Lista de glosas"""
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail="No existe la autoridad.")
    resultados = []
    for glosa, autoridad, distrito in crud.get_glosas(db, autoridad_id=autoridad_id, ano=ano):
        resultados.append(
            schemas.Glosa(
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
    return resultados


@router.get("/{glosa_id}", response_model=schemas.Glosa)
async def consultar_un_glosa(glosa_id: int, db: Session = Depends(get_db)):
    """Consultar un glosa"""
    try:
        glosa = crud.get_glosa(db, glosa_id=glosa_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return schemas.Glosa(
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
