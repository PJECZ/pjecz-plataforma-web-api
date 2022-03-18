"""
Peritos Tipos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.peritos_tipos.models import PeritoTipo


def get_peritos_tipos(db: Session) -> Any:
    """Consultar los Tipos de Peritos activos"""
    return db.query(PeritoTipo).filter_by(estatus="A").order_by(PeritoTipo.id.desc())


def get_perito_tipo(db: Session, perito_tipo_id: int) -> PeritoTipo:
    """Consultar un Tipo de Perito por su id"""
    perito_tipo = db.query(PeritoTipo).get(perito_tipo_id)
    if perito_tipo is None:
        raise IndexError("No existe ese Tipo de Perito")
    if perito_tipo.estatus != "A":
        raise ValueError("No es activo ese Tipo de Perito, está eliminado")
    return perito_tipo
