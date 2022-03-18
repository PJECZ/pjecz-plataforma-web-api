"""
REPSVM Delitos Especificos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.repsvm_delitos_especificos.models import REPSVMDelitoEspecifico
from plataforma_web.v2.repsvm_delitos_genericos.crud import get_repsvm_delito_generico


def get_repsvm_delitos_especificos(
    db: Session,
    repsvm_delito_generico_id: int = None,
) -> Any:
    """Consultar los Delitos Especificos activos"""
    consulta = db.query(REPSVMDelitoEspecifico)
    if repsvm_delito_generico_id:
        repsvm_delito_generico = get_repsvm_delito_generico(db, repsvm_delito_generico_id)
        consulta = consulta.filter(REPSVMDelitoEspecifico.repsvm_delito_generico == repsvm_delito_generico)
    return consulta.filter_by(estatus="A").order_by(REPSVMDelitoEspecifico.id.desc())


def get_repsvm_delito_especifico(db: Session, repsvm_delito_especifico_id: int) -> REPSVMDelitoEspecifico:
    """Consultar un Delito Especifico por su id"""
    repsvm_delito_especifico = db.query(REPSVMDelitoEspecifico).get(repsvm_delito_especifico_id)
    if repsvm_delito_especifico is None:
        raise IndexError("No existe ese Delito Especifico")
    if repsvm_delito_especifico.estatus != "A":
        raise ValueError("No es activo ese Delito Especifico, está eliminado")
    return repsvm_delito_especifico
