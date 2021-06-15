"""
Materias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from api.materias.models import Materia


def get_materias(db: Session):
    """Consultar materias activas"""
    return db.query(Materia).filter(Materia.estatus == "A").order_by(Materia.nombre).all()


def get_materia(db: Session, materia_id: int):
    """Consultar un materia"""
    return db.query(Materia).get(materia_id)
