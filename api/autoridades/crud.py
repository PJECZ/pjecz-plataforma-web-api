"""
Autoridades, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from api.autoridades.models import Autoridad


def get_autoridades(db: Session, distrito_id: int = None):
    """ Consultar autoridades """
    autoridades = db.query(Autoridad)
    if distrito_id:
        autoridades = autoridades.filter(Autoridad.distrito_id == distrito_id)
    return autoridades.filter(Autoridad.estatus == "A").order_by(Autoridad.descripcion).all()


def get_autoridad(db: Session, autoridad_id: int):
    """ Consultar una autoridad """
    return db.query(Autoridad).get(autoridad_id)
