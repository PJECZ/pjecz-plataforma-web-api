"""
Glosas v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.glosas.models import Glosa
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_glosas(
    db: Session,
    autoridad_id: int = None,
    ano: int = None,
) -> Any:
    """Consultar las Glosas activas"""
    consulta = db.query(Glosa)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Glosa.autoridad == autoridad)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            consulta = consulta.filter(Glosa.fecha >= date(ano, 1, 1)).filter(Glosa.fecha <= date(ano, 12, 31))
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
