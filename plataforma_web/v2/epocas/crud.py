"""
Epocas v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.epocas.models import Epoca


def get_epocas(db: Session) -> Any:
    """Consultar las Epocas activas"""
    return db.query(Epoca).filter_by(estatus="A").order_by(Epoca.id.desc())


def get_epoca(db: Session, epoca_id: int) -> Epoca:
    """Consultar una Epoca por su id"""
    epoca = db.query(Epoca).get(epoca_id)
    if epoca is None:
        raise IndexError("No existe ese Epoca")
    if epoca.estatus != "A":
        raise ValueError("No es activo ese Epoca, está eliminado")
    return epoca
