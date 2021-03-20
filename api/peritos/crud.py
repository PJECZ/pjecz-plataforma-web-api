"""
Peritos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from unidecode import unidecode

from api.peritos.models import Perito
from api.distritos.models import Distrito


def get_peritos(db: Session, distrito_id: int, nombre: str = None):
    """ Consultar peritos """
    consulta = db.query(Perito, Distrito).join(Distrito)
    if distrito_id:
        consulta = consulta.filter(Perito.distrito_id == distrito_id)
    if nombre:
        nombre = unidecode(nombre.strip()).upper()
        consulta = consulta.filter(Perito.nombre.like(f"%{nombre}%"))
    return consulta.filter(Perito.estatus == "A").order_by(Distrito.nombre, Perito.nombre).limit(200).all()


def get_perito(db: Session, perito_id: int):
    """ Consultar un perito """
    return db.query(Perito).get(perito_id)
