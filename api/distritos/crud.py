"""
Distritos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from api.distritos.models import Distrito


def get_distritos(db: Session):
    """ Consultar distritos judiciales activos """
    return (
        db.query(Distrito)
        .filter(Distrito.es_distrito_judicial == True)
        .filter(Distrito.estatus == "A")
        .order_by(Distrito.nombre)
        .all()
    )


def get_distrito(db: Session, distrito_id: int):
    """ Consultar un distrito """
    return db.query(Distrito).get(distrito_id)
