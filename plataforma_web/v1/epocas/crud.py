"""
Epocas, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from ...core.epocas.models import Epoca


def get_epocas(db: Session):
    """Consultar epocas activos"""
    return db.query(Epoca).filter(Epoca.estatus == "A").order_by(Epoca.nombre).limit(400).all()


def get_epoca(db: Session, epoca_id: int):
    """Consultar un epoca"""
    return db.query(Epoca).get(epoca_id)
