"""
Materias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from plataforma_web.core.materias.models import Materia


def get_materias(db: Session):
    """Consultar materias activas (excepto el id 1 que es NO DEFINIDO)"""
    return db.query(Materia).filter_by(estatus="A").filter(Materia.id != 1).order_by(Materia.nombre).limit(400).all()


def get_materia(db: Session, materia_id: int):
    """Consultar un materia"""
    materia = db.query(Materia).get(materia_id)
    if materia is None:
        raise IndexError("No existe esa materia")
    if materia.estatus != "A":
        raise ValueError("No es activa la materia, está eliminada")
    return materia
