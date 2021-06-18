"""
Sentencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.sentencias.models import Sentencia
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_sentencias(db: Session, autoridad_id: int = None, ano: int = None):
    """Consultar sentencias"""
    sentencias = db.query(Sentencia, Autoridad, Distrito).select_from(Sentencia).join(Autoridad).join(Distrito)
    if autoridad_id:
        sentencias = sentencias.filter(Sentencia.autoridad_id == autoridad_id)
    if ano and ano >= 2000 and ano <= date.today().year:
        sentencias = sentencias.filter(Sentencia.fecha >= date(ano, 1, 1)).filter(Sentencia.fecha <= date(ano, 12, 31))
    return sentencias.filter(Sentencia.estatus == "A").order_by(Sentencia.fecha.desc()).limit(500).all()


def get_sentencia(db: Session, sentencia_id: int):
    """Consultar una sentencia"""
    return db.query(Sentencia).get(sentencia_id)
