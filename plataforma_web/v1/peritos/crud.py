"""
Peritos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from ...core.distritos.models import Distrito
from ...core.peritos_tipos.models import PeritoTipo
from ...core.peritos.models import Perito
from ..distritos.crud import get_distrito


def get_peritos(
    db: Session,
    distrito_id: int,
    nombre: str = None,
):
    """Consultar peritos"""
    distrito = get_distrito(db, distrito_id)
    consulta = db.query(Perito, PeritoTipo, Distrito).select_from(Perito).join(PeritoTipo).join(Distrito).filter(Perito.distrito == distrito)
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(Perito.nombre.like(f"%{nombre}%"))
    return consulta.filter(Perito.estatus == "A").order_by(Distrito.nombre, Perito.nombre).limit(400).all()


def get_perito(db: Session, perito_id: int):
    """Consultar un perito"""
    perito = db.query(Perito).get(perito_id)
    if perito is None:
        raise IndexError("No existe ese perito")
    if perito.estatus != "A":
        raise ValueError("No es activo el perito, está eliminado")
    return perito
