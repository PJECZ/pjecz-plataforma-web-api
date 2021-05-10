"""
Sentencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.sentencias.models import Sentencia
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_sentencias(db: Session, autoridad_id: int = None, fecha: date = None):
    """Consultar sentencias"""
    sentencias = db.query(Sentencia, Autoridad, Distrito).select_from(Sentencia).join(Autoridad).join(Distrito)
    if autoridad_id:
        sentencias = sentencias.filter(Sentencia.autoridad_id == autoridad_id).order_by(Sentencia.fecha.desc())
    if fecha:
        sentencias = sentencias.filter(Sentencia.fecha == fecha).order_by(Autoridad.clave)
    return sentencias.filter(Sentencia.estatus == "A").limit(100).all()


def get_sentencia(db: Session, sentencia_id: int):
    """Consultar una sentencia"""
    return db.query(Sentencia).get(sentencia_id)
