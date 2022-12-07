"""
REPSVM Delitos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from ...core.repsvm_delitos.models import REPSVMDelito


def get_repsvm_delitos(db: Session) -> Any:
    """Consultar los Delitos activos"""
    consulta = db.query(REPSVMDelito)
    return consulta.filter_by(estatus="A").order_by(REPSVMDelito.nombre)


def get_repsvm_delito(db: Session, repsvm_delito_id: int) -> REPSVMDelito:
    """Consultar un Delito por su id"""
    repsvm_delito = db.query(REPSVMDelito).get(repsvm_delito_id)
    if repsvm_delito is None:
        raise IndexError("No existe ese Delito")
    if repsvm_delito.estatus != "A":
        raise ValueError("No es activo ese Delito, está eliminado")
    return repsvm_delito
