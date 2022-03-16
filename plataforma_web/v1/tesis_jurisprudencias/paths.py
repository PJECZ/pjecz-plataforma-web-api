"""
Tesis Jurisprudencias, rutas
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from lib.database import get_db
from .crud import get_tesis_jurisprudencia, get_tesis_jurisprudencias
from .schemas import TesisJurisprudenciaOut

router = APIRouter()


@router.get("", response_model=List[TesisJurisprudenciaOut])
async def listar_tesis_jurisprudencias(
    autoridad_id: int = None,
    epoca_id: int = None,
    materia_id: int = None,
    clase: str = None,
    titulo: str = None,
    texto: str = None,
    aprobacion_anio: int = None,
    db: Session = Depends(get_db),
):
    """Lista de tesis_jurisprudencias"""
    resultados = []
    try:
        for tesis_jurisprudencia, autoridad, distrito in get_tesis_jurisprudencias(
            db,
            autoridad_id=autoridad_id,
            epoca_id=epoca_id,
            materia_id=materia_id,
            clase=clase,
            titulo=titulo,
            texto=texto,
            aprobacion_anio=aprobacion_anio,
        ):
            resultados.append(
                TesisJurisprudenciaOut(
                    id=tesis_jurisprudencia.id,
                    distrito_id=distrito.id,
                    distrito=distrito.nombre,
                    autoridad_id=autoridad.id,
                    autoridad=autoridad.descripcion,
                    epoca_id=tesis_jurisprudencia.epoca_id,
                    epoca=tesis_jurisprudencia.epoca.nombre,
                    materia_id=tesis_jurisprudencia.materia_id,
                    materia=tesis_jurisprudencia.materia.nombre,
                    titulo=tesis_jurisprudencia.titulo,
                    subtitulo=tesis_jurisprudencia.subtitulo,
                    tipo=tesis_jurisprudencia.tipo,
                    estado=tesis_jurisprudencia.estado,
                    clave_control=tesis_jurisprudencia.clave_control,
                    clase=tesis_jurisprudencia.clase,
                    rubro=tesis_jurisprudencia.rubro,
                    texto=tesis_jurisprudencia.texto,
                    precedentes=tesis_jurisprudencia.precedentes,
                    votacion=tesis_jurisprudencia.votacion,
                    votos_particulares=tesis_jurisprudencia.votos_particulares,
                    aprobacion_fecha=tesis_jurisprudencia.aprobacion_fecha,
                    publicacion_tiempo=tesis_jurisprudencia.publicacion_tiempo,
                    aplicacion_tiempo=tesis_jurisprudencia.aplicacion_tiempo,
                )
            )
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return resultados


@router.get("/{tesis_jurisprudencia_id}", response_model=TesisJurisprudenciaOut)
async def consultar_un_tesis_jurisprudencia(tesis_jurisprudencia_id: int, db: Session = Depends(get_db)):
    """Consultar un tesis_jurisprudencia"""
    try:
        tesis_jurisprudencia = get_tesis_jurisprudencia(db, tesis_jurisprudencia_id=tesis_jurisprudencia_id)
    except IndexError as error:
        raise HTTPException(status_code=404, detail=f"Not found: {str(error)}") from error
    except ValueError as error:
        raise HTTPException(status_code=406, detail=f"Not acceptable: {str(error)}") from error
    return TesisJurisprudenciaOut(
        id=tesis_jurisprudencia.id,
        distrito_id=tesis_jurisprudencia.autoridad.distrito_id,
        distrito=tesis_jurisprudencia.autoridad.distrito.nombre,
        autoridad_id=tesis_jurisprudencia.autoridad_id,
        autoridad=tesis_jurisprudencia.autoridad.descripcion,
        epoca_id=tesis_jurisprudencia.epoca_id,
        epoca=tesis_jurisprudencia.epoca.nombre,
        materia_id=tesis_jurisprudencia.materia_id,
        materia=tesis_jurisprudencia.materia.nombre,
        titulo=tesis_jurisprudencia.titulo,
        subtitulo=tesis_jurisprudencia.subtitulo,
        tipo=tesis_jurisprudencia.tipo,
        estado=tesis_jurisprudencia.estado,
        clave_control=tesis_jurisprudencia.clave_control,
        clase=tesis_jurisprudencia.clase,
        rubro=tesis_jurisprudencia.rubro,
        texto=tesis_jurisprudencia.texto,
        precedentes=tesis_jurisprudencia.precedentes,
        votacion=tesis_jurisprudencia.votacion,
        votos_particulares=tesis_jurisprudencia.votos_particulares,
        aprobacion_fecha=tesis_jurisprudencia.aprobacion_fecha,
        publicacion_tiempo=tesis_jurisprudencia.publicacion_tiempo,
        aplicacion_tiempo=tesis_jurisprudencia.aplicacion_tiempo,
    )
