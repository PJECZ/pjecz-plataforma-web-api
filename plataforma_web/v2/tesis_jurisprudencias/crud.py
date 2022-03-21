"""
Tesis Jurisprudencias v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from plataforma_web.core.tesis_jurisprudencias.models import TesisJurisprudencia
from plataforma_web.v2.autoridades.crud import get_autoridad
from plataforma_web.v2.epocas.crud import get_epoca
from plataforma_web.v2.materias.crud import get_materia


def get_tesis_jurisprudencias(
    db: Session,
    autoridad_id: int = None,
    epoca_id: int = None,
    materia_id: int = None,
    clase: str = None,
    titulo: str = None,
    texto: str = None,
    aprobacion_anio: int = None,
) -> Any:
    """Consultar los Tesis Jurisprudencias activos"""
    consulta = db.query(TesisJurisprudencia)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(TesisJurisprudencia.autoridad == autoridad)
    if epoca_id is not None:
        epoca = get_epoca(db, epoca_id=epoca_id)
        consulta = consulta.filter(TesisJurisprudencia.epoca == epoca)
    if materia_id is not None:
        materia = get_materia(db, materia_id=materia_id)
        consulta = consulta.filter(TesisJurisprudencia.materia == materia)
    if clase is not None:
        clase = safe_string(clase)
        if clase in TesisJurisprudencia.CLASES:
            tesis_jurisprudencias = tesis_jurisprudencias.filter_by(clase=clase)
    if titulo is not None:
        titulo = safe_string(titulo)
        if titulo != "":
            tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.titulo.contains(titulo))
    if texto is not None:
        texto = safe_string(texto)
        if texto != "":
            tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.texto.contains(texto))
    if aprobacion_anio is not None:
        if 2000 <= aprobacion_anio <= date.today().year:
            tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.fecha >= date(aprobacion_anio, 1, 1)).filter(TesisJurisprudencia.fecha <= date(aprobacion_anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(TesisJurisprudencia.id.desc())


def get_tesis_jurisprudencia(db: Session, tesis_jurisprudencia_id: int) -> TesisJurisprudencia:
    """Consultar un Tesis Jurisprudencia por su id"""
    tesis_jurisprudencia = db.query(TesisJurisprudencia).get(tesis_jurisprudencia_id)
    if tesis_jurisprudencia is None:
        raise IndexError("No existe ese Tesis Jurisprudencia")
    if tesis_jurisprudencia.estatus != "A":
        raise ValueError("No es activo ese Tesis Jurisprudencia, está eliminado")
    return tesis_jurisprudencia
