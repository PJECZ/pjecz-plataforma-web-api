"""
Distritos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_clave

from ...core.distritos.models import Distrito


def get_distritos(db: Session, solo_distritos: bool = None) -> Any:
    """Consultar los Distritos judiciales activos"""
    consulta = db.query(Distrito).filter_by(es_distrito_judicial=True)
    if solo_distritos:
        consulta = consulta.filter(Distrito.nombre.like("DISTRITO%"))
    return consulta.filter_by(estatus="A").order_by(Distrito.nombre)


def get_distrito(db: Session, distrito_id: int) -> Distrito:
    """Consultar un Distrito por su id"""
    distrito = db.query(Distrito).get(distrito_id)
    if distrito is None:
        raise IndexError("No existe ese distrito")
    if distrito.es_distrito_judicial is False:
        raise ValueError("No es un distrito judicial")
    if distrito.estatus != "A":
        raise ValueError("No es activo ese distrito, está eliminado")
    return distrito


def get_distrito_from_clave(db: Session, distrito_clave: str) -> Distrito:
    """Consultar un Distrito por su clave"""
    clave = safe_clave(distrito_clave)
    if clave == "":
        raise ValueError("No es válida la clave del distrito")
    distrito = db.query(Distrito).filter_by(clave=clave).first()
    if distrito is None:
        raise IndexError("No existe ese distrito")
    if distrito.estatus != "A":
        raise ValueError("No es activo ese distrito, está eliminado")
    return distrito
