"""
Glosas v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from ...core.glosas.models import Glosa
from ..autoridades.crud import get_autoridad


def get_glosas(
    db: Session,
    autoridad_id: int = None,
    anio: int = None,
) -> Any:
    """Consultar las Glosas activas"""
    consulta = db.query(Glosa)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Glosa.autoridad == autoridad)
    if anio is not None:
        if 2000 <= anio <= date.today().year:
            consulta = consulta.filter(Glosa.fecha >= date(anio, 1, 1)).filter(Glosa.fecha <= date(anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(Glosa.id.desc())


def get_glosa(db: Session, glosa_id: int) -> Glosa:
    """Consultar una Glosa por su id"""
    glosa = db.query(Glosa).get(glosa_id)
    if glosa is None:
        raise IndexError("No existe ese Glosa")
    if glosa.estatus != "A":
        raise ValueError("No es activo ese Glosa, está eliminado")
    return glosa
