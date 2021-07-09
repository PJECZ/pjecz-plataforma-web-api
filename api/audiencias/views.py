"""
Audiencias, vistas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from api.autoridades.crud import get_autoridad
from api.audiencias import crud, schemas
from lib.database import get_db

router = APIRouter()


@router.get('', response_model=List[schemas.Audiencia])
async def listar_audiencias(autoridad_id: int, fecha: date = None, ano: int = None, db: Session = Depends(get_db)):
    """ Lista de audiencias """
    autoridad = get_autoridad(db, autoridad_id=autoridad_id)
    if autoridad is None:
        raise HTTPException(status_code=400, detail='No existe la autoridad.')
    resultados = []
    for audiencia, autoridad, distrito in crud.get_audiencias(db, autoridad_id=autoridad_id, fecha=fecha, ano=ano):
        resultados.append(
            schemas.Audiencia(
                id=audiencia.id,
                distrito_id=distrito.id,
                distrito=distrito.nombre,
                autoridad_id=autoridad.id,
                autoridad=autoridad.descripcion,
                tiempo=autoridad.tiempo,
                tipo_audiencia=autoridad.tipo_audiencia,
                expediente=autoridad.expediente,
                actores=autoridad.actores,
                demandados=autoridad.demandados,
                sala=autoridad.sala,
                caracter=autoridad.caracter,
                causa_penal=autoridad.causa_penal,
                delitos=autoridad.delitos,
                toca=autoridad.toca,
                expediente_origen=autoridad.expediente_origen,
                imputados=autoridad.imputados,
                origen=autoridad.origen,
            )
        )
    return resultados


@router.get('/{audiencia_id}', response_model=schemas.Audiencia)
async def consultar_un_audiencia(audiencia_id: int, db: Session = Depends(get_db)):
    """ Consultar un audiencia """
    audiencia = crud.get_audiencia(db, audiencia_id=audiencia_id)
    if audiencia is None:
        raise HTTPException(status_code=400, detail='No existe el audiencia.')
    return schemas.Audiencia(
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
