"""
REPSVM Agresores v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from plataforma_web.core.repsvm_agresores.models import REPSVMAgresor
from plataforma_web.v2.distritos.crud import get_distrito


def get_repsvm_agresores(
    db: Session,
    distrito_id: int = None,
    nombre: str = None,
) -> Any:
    """Consultar los Agresores activos"""
    consulta = db.query(REPSVMAgresor)
    if distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter(REPSVMAgresor.distrito == distrito)
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(REPSVMAgresor.nombre.contains(nombre))
    return consulta.filter_by(estatus="A").order_by(REPSVMAgresor.id.desc())


def get_repsvm_agresor(db: Session, repsvm_agresor_id: int) -> REPSVMAgresor:
    """Consultar un Agresor por su id"""
    agresor = db.query(REPSVMAgresor).get(repsvm_agresor_id)
    if agresor is None:
        raise IndexError("No existe ese Agresor")
    if agresor.estatus != "A":
        raise ValueError("No es activo ese Agresor, está eliminado")
    return agresor
