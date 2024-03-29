"""
Edictos v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from ...core.edictos.models import Edicto
from ..autoridades.crud import get_autoridad


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    anio: int = None,
) -> Any:
    """Consultar los Edictos activos"""
    consulta = db.query(Edicto)
    if autoridad_id is not None and autoridad_id != 0:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Edicto.autoridad == autoridad)
    if anio is not None:
        if 2000 <= anio <= date.today().year:
            consulta = consulta.filter(Edicto.fecha >= date(anio, 1, 1)).filter(Edicto.fecha <= date(anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(Edicto.id.desc())


def get_edicto(db: Session, edicto_id: int) -> Edicto:
    """Consultar un Edicto por su id"""
    edicto = db.query(Edicto).get(edicto_id)
    if edicto is None:
        raise IndexError("No existe ese Edicto")
    if edicto.estatus != "A":
        raise ValueError("No es activo ese Edicto, está eliminado")
    return edicto
