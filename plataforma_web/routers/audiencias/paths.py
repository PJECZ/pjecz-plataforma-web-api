"""
Audiencias, paths
"""
from datetime import date
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_audiencia, get_audiencias
from .schemas import AudienciaOut

router = APIRouter()


@router.get("", response_model=List[AudienciaOut])
async def listar_audiencias(
    autoridad_id: int,
    fecha: date = None,
    ano: int = None,
    db: Session = Depends(get_db),
):
    """Lista de audiencias"""
    resultados = []
    try:
        for audiencia, autoridad, distrito in get_audiencias(db, autoridad_id=autoridad_id, fecha=fecha, ano=ano):
            resultados.append(
                AudienciaOut(
                    id=audiencia.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    tiempo=audiencia.tiempo,
                    tipo_audiencia=audiencia.tipo_audiencia,
                    expediente=audiencia.expediente,
                    actores=audiencia.actores,
                    demandados=audiencia.demandados,
                    sala=audiencia.sala,
                    caracter=audiencia.caracter,
                    causa_penal=audiencia.causa_penal,
                    delitos=audiencia.delitos,
                    toca=audiencia.toca,
                    expediente_origen=audiencia.expediente_origen,
                    imputados=audiencia.imputados,
                    origen=audiencia.origen,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{audiencia_id}", response_model=AudienciaOut)
async def consultar_un_audiencia(audiencia_id: int, db: Session = Depends(get_db)):
    """Consultar un audiencia"""
    try:
        audiencia = get_audiencia(db, audiencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return AudienciaOut(
        id=audiencia.id,
        distrito_id=audiencia.autoridad.distrito.id,
        distrito=audiencia.autoridad.distrito.nombre,
        autoridad_id=audiencia.autoridad.id,
        autoridad=audiencia.autoridad.descripcion,
        tiempo=audiencia.tiempo,
        tipo_audiencia=audiencia.tipo_audiencia,
        expediente=audiencia.expediente,
        actores=audiencia.actores,
        demandados=audiencia.demandados,
        sala=audiencia.sala,
        caracter=audiencia.caracter,
        causa_penal=audiencia.causa_penal,
        delitos=audiencia.delitos,
        toca=audiencia.toca,
        expediente_origen=audiencia.expediente_origen,
        imputados=audiencia.imputados,
        origen=audiencia.origen,
    )
