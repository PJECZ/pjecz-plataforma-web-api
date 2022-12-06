"""
REPSVM Agresores-Delitos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from plataforma_web.core.repsvm_agresores_delitos.models import REPSVMAgresorDelito


def get_repsvm_agresores_delitos(
    db: Session,
    filtro_id: int = None,
    filtro_descripcion: str = None,
    filtro_boleano: bool = False,
) -> Any:
    """Consultar los agresores-delitos activos"""
    consulta = db.query(REPSVMAgresorDelito)
    if filtro_id:
        consulta = consulta.filter_by(filtro_id=filtro_id)
    filtro_descripcion = safe_string(filtro_descripcion)
    if filtro_descripcion:
        consulta = consulta.filter_by(filtro_descripcion=filtro_descripcion)
    if filtro_boleano is True:
        consulta = consulta.filter_by(filtro_boleano=True)
    return consulta.filter_by(estatus="A").order_by(REPSVMAgresorDelito.id.desc())


def get_repsvm_agresor_delito(db: Session, repsvm_agresor_delito_id: int) -> REPSVMAgresorDelito:
    """Consultar un agresor-delito por su id"""
    repsvm_agresor_delito = db.query(REPSVMAgresorDelito).get(repsvm_agresor_delito_id)
    if repsvm_agresor_delito is None:
        raise IndexError("No existe ese agresor-delito")
    if repsvm_agresor_delito.estatus != "A":
        raise ValueError("No es activo ese agresor-delito, está eliminado")
    return repsvm_agresor_delito
