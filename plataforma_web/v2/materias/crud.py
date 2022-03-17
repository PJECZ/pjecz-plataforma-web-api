"""
Materias v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from .models import Materia


def get_materias(db: Session) -> Any:
    """Consultar los materias activos"""
    return db.query(Materia).filter_by(estatus="A").order_by(Materia.id)


def get_materia(db: Session, materia_id: int) -> Materia:
    """Consultar un materia por su id"""
    materia = db.query(Materia).get(materia_id)
    if materia is None:
        raise IndexError("No existe ese materia")
    if materia.estatus != "A":
        raise ValueError("No es activo ese materia, está eliminado")
    return materia
