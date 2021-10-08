"""
Materias Tipos Juicios, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_materia_tipo_juicio, get_materias_tipos_juicios
from .schemas import MateriaTipoJuicioOut

router = APIRouter()


@router.get("", response_model=List[MateriaTipoJuicioOut])
async def listar_tipos_juicios(materia_id: int, db: Session = Depends(get_db)):
    """Lista de materias_tipos_juicios"""
    resultados = []
    try:
        for materia_tipo_juicio, materia in get_materias_tipos_juicios(db, materia_id):
            resultados.append(
                MateriaTipoJuicioOut(
                    id=materia_tipo_juicio.id,
                    materia_id=materia.id,
                    materia=materia.nombre,
                    descripcion=materia_tipo_juicio.descripcion,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{materia_tipo_juicio_id}", response_model=MateriaTipoJuicioOut)
async def consultar_un_tipo_juicio(materia_tipo_juicio_id: int, db: Session = Depends(get_db)):
    """Consultar un materia_tipo_juicio"""
    try:
        materia_tipo_juicio = get_materia_tipo_juicio(db, materia_tipo_juicio_id=materia_tipo_juicio_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaTipoJuicioOut(
        id=materia_tipo_juicio.id,
        materia_id=materia_tipo_juicio.materia_id,
        materia=materia_tipo_juicio.materia.nombre,
        descripcion=materia_tipo_juicio.descripcion,
    )
