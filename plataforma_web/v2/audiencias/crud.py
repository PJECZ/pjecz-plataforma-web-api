"""
Audiencias v2, CRUD (create, read, update, and delete)
"""
from datetime import datetime, date
from typing import Any
from sqlalchemy.orm import Session

from ...core.audiencias.models import Audiencia
from ..autoridades.crud import get_autoridad


def get_audiencias(
    db: Session,
    autoridad_id: int = None,
    fecha: date = None,
    anio: int = None,
) -> Any:
    """Consultar los Audiencias activos"""
    consulta = db.query(Audiencia)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Audiencia.autoridad == autoridad)
    if fecha is not None:
        desde = datetime(
            year=fecha.year,
            month=fecha.month,
            day=fecha.day,
            hour=0,
            minute=0,
            second=0,
        )
        hasta = datetime(
            year=fecha.year,
            month=fecha.month,
            day=fecha.day,
            hour=23,
            minute=59,
            second=59,
        )
        consulta = consulta.filter(Audiencia.tiempo >= desde).filter(Audiencia.tiempo <= hasta)
    elif anio is not None:
        if 2000 <= anio <= date.today().year:
            consulta = consulta.filter(Audiencia.tiempo >= date(anio, 1, 1)).filter(Audiencia.tiempo <= date(anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(Audiencia.id.desc())


def get_audiencia(db: Session, audiencia_id: int) -> Audiencia:
    """Consultar un Audiencia por su id"""
    audiencia = db.query(Audiencia).get(audiencia_id)
    if audiencia is None:
        raise IndexError("No existe ese Audiencia")
    if audiencia.estatus != "A":
        raise ValueError("No es activo ese Audiencia, está eliminado")
    return audiencia
