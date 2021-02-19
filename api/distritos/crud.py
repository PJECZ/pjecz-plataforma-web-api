"""
Distritos, CRUD: the four basic operations (create, read, update, and delete) of data storage, regarded collectively
"""
from sqlalchemy.orm import Session
from api.distritos.models import Distrito


def get_distrito(db: Session, distrito_id: int):
    """ Consultar un distrito """
    return db.query(Distrito).get(distrito_id)


def get_distritos(db: Session):
    """ Consultar distritos """
    return db.query(Distrito).filter(Distrito.estatus == "A").order_by(Distrito.nombre).all()
