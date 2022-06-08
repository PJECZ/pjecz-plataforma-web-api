"""
REPSVM Delitos Genericos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from ...core.repsvm_delitos_genericos.models import REPSVMDelitoGenerico


def get_repsvm_delitos_genericos(db: Session) -> Any:
    """Consultar los Delitos Genericos activos"""
    return db.query(REPSVMDelitoGenerico).filter_by(estatus="A").order_by(REPSVMDelitoGenerico.id.desc())


def get_repsvm_delito_generico(db: Session, repsvm_delito_generico_id: int) -> REPSVMDelitoGenerico:
    """Consultar un Delito Generico por su id"""
    repsvm_delito_generico = db.query(REPSVMDelitoGenerico).get(repsvm_delito_generico_id)
    if repsvm_delito_generico is None:
        raise IndexError("No existe ese Delito Generico")
    if repsvm_delito_generico.estatus != "A":
        raise ValueError("No es activo ese Delito Generico, está eliminado")
    return repsvm_delito_generico
