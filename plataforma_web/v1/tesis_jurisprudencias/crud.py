"""
Tesis Jurisprudencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from plataforma_web.core.autoridades.models import Autoridad
from plataforma_web.core.distritos.models import Distrito
from plataforma_web.core.tesis_jurisprudencias.models import TesisJurisprudencia
from plataforma_web.v1.autoridades.crud import get_autoridad
from plataforma_web.v1.epocas.crud import get_epoca
from plataforma_web.v1.materias.crud import get_materia


def get_tesis_jurisprudencias(
    db: Session,
    autoridad_id: int = None,
    epoca_id: int = None,
    materia_id: int = None,
    clase: str = None,
    titulo: str = None,
    texto: str = None,
    aprobacion_anio: int = None,
):
    """Consultar tesis_jurisprudencias"""
    tesis_jurisprudencias = db.query(TesisJurisprudencia, Autoridad, Distrito).select_from(TesisJurisprudencia).join(Autoridad).join(Distrito)
    if autoridad_id:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.autoridad == autoridad)
    if epoca_id:
        epoca = get_epoca(db, epoca_id=epoca_id)
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.epoca == epoca)
    if materia_id:
        materia = get_materia(db, materia_id=materia_id)
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.materia == materia)
    clase = safe_string(clase)
    if clase in TesisJurisprudencia.CLASES:
        tesis_jurisprudencias = tesis_jurisprudencias.filter_by(clase=clase)
    titulo = safe_string(titulo)
    if titulo != "":
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.titulo.like(f"%{titulo}%"))
    texto = safe_string(texto)
    if texto != "":
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.texto.like(f"%{texto}%"))
    if aprobacion_anio is not None:
        if 2000 <= aprobacion_anio <= date.today().year:
            tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.fecha >= date(aprobacion_anio, 1, 1)).filter(TesisJurisprudencia.fecha <= date(aprobacion_anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return tesis_jurisprudencias.filter(TesisJurisprudencia.estatus == "A").order_by(TesisJurisprudencia.id.desc()).limit(400).all()


def get_tesis_jurisprudencia(db: Session, tesis_jurisprudencia_id: int):
    """Consultar un tesis_jurisprudencia"""
    return db.query(TesisJurisprudencia).get(tesis_jurisprudencia_id)
