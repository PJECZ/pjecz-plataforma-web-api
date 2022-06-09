"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from ...core.autoridades.models import Autoridad
from ...core.redams.models import Redam
from ..autoridades.crud import get_autoridad
from ..distritos.crud import get_distrito


def get_redams(
    db: Session,
    autoridad_id: int = None,
    distrito_id: int = None,
    nombre: str = None,
) -> Any:
    """Consultar los deudores activos"""
    consulta = db.query(Redam)
    if distrito_id is not None and distrito_id != 0:
        distrito = get_distrito(db, distrito_id=distrito_id)
        consulta = consulta.join(Autoridad).filter(Autoridad.distrito == distrito)
    if autoridad_id is not None and autoridad_id != 0:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Redam.autoridad == autoridad)
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(Redam.nombre.contains(nombre))
    return consulta.filter_by(estatus="A").order_by(Redam.id.desc())


def get_redam(db: Session, redam_id: int) -> Redam:
    """Consultar un deudor por su id"""
    redam = db.query(Redam).get(redam_id)
    if redam is None:
        raise IndexError("No existe ese deudor")
    if redam.estatus != "A":
        raise ValueError("No es activo ese deudor, está eliminado")
    return redam
