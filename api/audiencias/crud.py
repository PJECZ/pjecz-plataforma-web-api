"""
Audiencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.audiencias.models import Audiencia
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_audiencias(db: Session, autoridad_id: int = None, fecha: date = None):
    """Consultar audiencias"""
    audiencias = db.query(Audiencia, Autoridad, Distrito).select_from(Audiencia).join(Autoridad).join(Distrito)
    if autoridad_id:
        audiencias = audiencias.filter(Audiencia.autoridad_id == autoridad_id).order_by(Audiencia.fecha.desc())
    if fecha:
        audiencias = audiencias.filter(Audiencia.fecha == fecha).order_by(Autoridad.clave)
    return audiencias.filter(Audiencia.estatus == "A").limit(100).all()


def get_audiencia(db: Session, audiencia_id: int):
    """Consultar un audiencia"""
    return db.query(Audiencia).get(audiencia_id)
