"""
Autoriades, paths
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db

from .crud import get_autoridad, get_autoridades, get_autoridad_from_clave
from .schemas import AutoridadOut

autoridades = APIRouter()


@autoridades.get("", response_model=List[AutoridadOut])
async def listar_autoridades(
    distrito_id: int = None,
    materia_id: int = None,
    organo_jurisdiccional: str = None,
    con_notarias: bool = False,
    para_glosas: bool = False,
    db: Session = Depends(get_db),
):
    """Lista de Autoridades"""
    resultados = []
    try:
        for autoridad, distrito, materia in get_autoridades(
            db,
            distrito_id=distrito_id,
            materia_id=materia_id,
            organo_jurisdiccional=organo_jurisdiccional,
            con_notarias=con_notarias,
            para_glosas=para_glosas,
        ):
            resultados.append(
                AutoridadOut(
                    id=autoridad.id,
                    distrito_id=autoridad.distrito_id,
                    distrito=distrito.nombre,
                    materia_id=autoridad.materia_id,
                    materia=materia.nombre,
                    autoridad=autoridad.descripcion,
                    autoridad_corta=autoridad.descripcion_corta,
                    organo_jurisdiccional=autoridad.organo_jurisdiccional,
                    audiencia_categoria=autoridad.audiencia_categoria,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@autoridades.get("/{autoridad_id}", response_model=AutoridadOut)
async def consultar_una_autoridad(autoridad_id: int, db: Session = Depends(get_db)):
    """Consultar una Autoridad"""
    try:
        autoridad = get_autoridad(db, autoridad_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AutoridadOut(
        id=autoridad.id,
        distrito_id=autoridad.distrito_id,
        distrito=autoridad.distrito.nombre,
        materia_id=autoridad.materia_id,
        materia=autoridad.materia.nombre,
        autoridad=autoridad.descripcion,
        autoridad_corta=autoridad.descripcion_corta,
        organo_jurisdiccional=autoridad.organo_jurisdiccional,
        audiencia_categoria=autoridad.audiencia_categoria,
    )


@autoridades.get("/clave/{clave}", response_model=AutoridadOut)
async def detail_from_clave(clave: str, db: Session = Depends(get_db)):
    """Detalle de una autoridad a partir de su clave"""
    try:
        autoridad = get_autoridad_from_clave(db, clave=clave)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AutoridadOut(
        id=autoridad.id,
        distrito_id=autoridad.distrito_id,
        distrito=autoridad.distrito.nombre,
        materia_id=autoridad.materia_id,
        materia=autoridad.materia.nombre,
        autoridad=autoridad.descripcion,
        autoridad_corta=autoridad.descripcion_corta,
        organo_jurisdiccional=autoridad.organo_jurisdiccional,
        audiencia_categoria=autoridad.audiencia_categoria,
    )
