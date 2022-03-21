"""
Peritos Tipos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from plataforma_web.core.peritos_tipos.models import PeritoTipo


def get_peritos_tipos(db: Session):
    """ Consultar peritos_tipos activos """
    return db.query(PeritoTipo).filter(PeritoTipo.estatus == 'A').order_by(PeritoTipo.nombre).limit(400).all()


def get_perito_tipo(db: Session, perito_tipo_id: int):
    """ Consultar un perito_tipo """
    perito_tipo = db.query(PeritoTipo).get(perito_tipo_id)
    if perito_tipo is None:
        raise IndexError("No existe ese tipo de perito")
    if perito_tipo.estatus != "A":
        raise ValueError("No es activo el tipo de perito, está eliminado")
    return perito_tipo
