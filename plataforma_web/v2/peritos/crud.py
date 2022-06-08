"""
Peritos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from ...core.peritos.models import Perito
from ..distritos.crud import get_distrito


def get_peritos(db: Session, distrito_id: int = None, nombre: str = None) -> Any:
    """Consultar los Peritos activos"""
    consulta = db.query(Perito)
    if distrito_id is not None:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter(Perito.distrito == distrito)
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(Perito.nombre.contains(nombre))
    return consulta.filter_by(estatus="A").order_by(Perito.nombre)


def get_perito(db: Session, perito_id: int) -> Perito:
    """Consultar un Perito por su id"""
    perito = db.query(Perito).get(perito_id)
    if perito is None:
        raise IndexError("No existe ese Perito")
    if perito.estatus != "A":
        raise ValueError("No es activo ese Perito, está eliminado")
    return perito
