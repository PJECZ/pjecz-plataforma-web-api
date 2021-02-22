"""
Peritos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from unidecode import unidecode
from api.peritos import models


def get_peritos(db: Session, distrito_id: int, nombre: str = None):
    """ Consultar peritos """
    consulta = db.query(models.Perito).filter(models.Perito.distrito_id == distrito_id)
    if nombre:
        nombre = unidecode(nombre.strip()).upper()
        consulta = consulta.filter(models.Perito.nombre.like(f"%{nombre}%"))
    return consulta.order_by(models.Perito.nombre).limit(100).all()


def get_perito(db: Session, perito_id: int):
    """ Consultar un perito """
    return db.query(Perito).get(perito_id)
