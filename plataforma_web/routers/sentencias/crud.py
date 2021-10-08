"""
Sentencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from ..autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad
from ..distritos.models import Distrito
from ..materias_tipos_juicios.models import MateriaTipoJuicio
from .models import Sentencia


def get_sentencias(
    db: Session,
    autoridad_id: int = None,
    ano: int = None,
):
    """Consultar sentencias"""
    sentencias = db.query(Sentencia, Autoridad, Distrito, MateriaTipoJuicio).select_from(Sentencia).join(Autoridad).join(Distrito).join(MateriaTipoJuicio)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        sentencias = sentencias.filter(Sentencia.autoridad == autoridad)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            sentencias = sentencias.filter(Sentencia.fecha >= date(ano, 1, 1)).filter(Sentencia.fecha <= date(ano, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return sentencias.filter(Sentencia.estatus == "A").order_by(Sentencia.fecha.desc()).limit(500).all()


def get_sentencia(db: Session, sentencia_id: int):
    """Consultar una sentencia"""
    sentencia = db.query(Sentencia).get(sentencia_id)
    if sentencia is None:
        raise IndexError
    if sentencia.estatus != "A":
        raise ValueError("No es activa la sentencia, está eliminada")
    return sentencia
