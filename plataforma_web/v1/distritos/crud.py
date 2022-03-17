"""
Distritos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from ...models.distritos.models import Distrito


def get_distritos(db: Session, solo_distritos: bool = False):
    """Consultar distritos judiciales activos"""
    consulta = db.query(Distrito).filter_by(es_distrito_judicial=True)
    if solo_distritos:
        consulta = consulta.filter(Distrito.nombre.like("Distrito%"))
    return consulta.filter_by(estatus="A").order_by(Distrito.nombre).all()


def get_distrito(db: Session, distrito_id: int):
    """Consultar un distrito judicial"""
    distrito = db.query(Distrito).get(distrito_id)
    if distrito is None:
        raise IndexError("No existe ese distrito")
    if distrito.es_distrito_judicial is False:
        raise ValueError("No es un distrito judicial")
    if distrito.estatus != "A":
        raise ValueError("No es activo el distrito, está eliminado")
    return distrito
