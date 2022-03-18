"""
REPSVM Agresores v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from plataforma_web.core.repsvm_agresores.models import REPSVMAgresor


def get_repsvm_agresores(
    db: Session,
    filtro_id: int = None,
    filtro_descripcion: str = None,
    filtro_boleano: bool = False,
) -> Any:
    """ Consultar los Agresores activos """
    consulta = db.query(REPSVMAgresor)
    if filtro_id:
        consulta = consulta.filter_by(filtro_id=filtro_id)
    filtro_descripcion = safe_string(filtro_descripcion)
    if filtro_descripcion:
        consulta = consulta.filter_by(filtro_descripcion=filtro_descripcion)
    if filtro_boleano is True:
        consulta = consulta.filter_by(filtro_boleano=True)
    return consulta.filter_by(estatus="A").order_by(REPSVMAgresor.id.desc())


def get_agresor(db: Session, agresor_id: int) -> REPSVMAgresor:
    """ Consultar un Agresor por su id """
    agresor = db.query(REPSVMAgresor).get(agresor_id)
    if agresor is None:
        raise IndexError("No existe ese Agresor")
    if agresor.estatus != "A":
        raise ValueError("No es activo ese Agresor, está eliminado")
    return agresor
