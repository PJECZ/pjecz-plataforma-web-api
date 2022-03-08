"""
Materias Tipos de Juzgados, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_materia_tipo_juzgado, get_materias_tipos_juzgados
from .schemas import MateriaTipoJuzgadoOut

router = APIRouter()


@router.get("", response_model=List[MateriaTipoJuzgadoOut])
async def listar_materias_tipos_juzgados(materia_id: int, db: Session = Depends(get_db)):
    """Lista de materias_tipos_juzgados"""
    resultados = []
    try:
        for materia_tipo_juzgado, materia in get_materias_tipos_juzgados(db, materia_id):
            resultados.append(
                MateriaTipoJuzgadoOut(
                    id=materia_tipo_juzgado.id,
                    materia_id=materia.id,
                    materia=materia.nombre,
                    descripcion=materia_tipo_juzgado.nombre,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{materia_tipo_juzgado_id}", response_model=MateriaTipoJuzgadoOut)
async def consultar_un_materia_tipo_juzgado(materia_tipo_juzgado_id: int, db: Session = Depends(get_db)):
    """Consultar un materia_tipo_juzgado"""
    try:
        materia_tipo_juzgado = get_materia_tipo_juzgado(db, materia_tipo_juzgado_id=materia_tipo_juzgado_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return MateriaTipoJuzgadoOut(
        id=materia_tipo_juzgado.id,
        materia_id=materia_tipo_juzgado.materia_id,
        materia=materia_tipo_juzgado.materia.nombre,
        descripcion=materia_tipo_juzgado.nombre,
    )
