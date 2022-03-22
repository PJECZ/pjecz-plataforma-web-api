"""
Sentencias v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.sentencias.models import Sentencia
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_sentencias(
    db: Session,
    autoridad_id: int = None,
    anio: int = None,
) -> Any:
    """Consultar los Sentencias activos"""
    consulta = db.query(Sentencia)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Sentencia.autoridad == autoridad)
    if anio is not None:
        if 2000 <= anio <= date.today().year:
            consulta = consulta.filter(Sentencia.fecha >= date(anio, 1, 1)).filter(Sentencia.fecha <= date(anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(Sentencia.id.desc())


def get_sentencia(db: Session, sentencia_id: int) -> Sentencia:
    """Consultar un Sentencia por su id"""
    sentencia = db.query(Sentencia).get(sentencia_id)
    if sentencia is None:
        raise IndexError("No existe ese Sentencia")
    if sentencia.estatus != "A":
        raise ValueError("No es activo ese Sentencia, está eliminado")
    return sentencia
