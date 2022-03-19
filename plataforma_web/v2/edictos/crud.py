"""
Edictos v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.edictos.models import Edicto
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    ano: int = None,
) -> Any:
    """Consultar los Edictos activos"""
    consulta = db.query(Edicto)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Edicto.autoridad == autoridad)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            consulta = consulta.filter(Edicto.fecha >= date(ano, 1, 1)).filter(Edicto.fecha <= date(ano, 12, 31))
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
