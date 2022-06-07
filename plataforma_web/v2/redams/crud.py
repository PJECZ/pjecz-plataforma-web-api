"""
REDAM (Registro Estatal de Deudores Alimentarios) v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.redams.models import Redam
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_redams(
    db: Session,
    autoridad_id: int = None,
) -> Any:
    """Consultar los deudores activos"""
    consulta = db.query(Redam)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(Redam.autoridad == autoridad)
    return consulta.filter_by(estatus="A").order_by(Redam.id.desc())


def get_redam(db: Session, redam_id: int) -> Redam:
    """Consultar un deudor por su id"""
    redam = db.query(Redam).get(redam_id)
    if redam is None:
        raise IndexError("No existe ese deudor")
    if redam.estatus != "A":
        raise ValueError("No es activo ese deudor, está eliminado")
    return redam