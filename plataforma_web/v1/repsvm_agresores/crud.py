"""
REPSVM, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from ...core.repsvm_agresores.models import REPSVMAgresor
from ..distritos.crud import get_distrito


def get_repsvm_agresores(
    db: Session,
    distrito_id: int,
    nombre: str = None,
):
    """Consultar repsvm_agresores activos"""
    distrito = get_distrito(db, distrito_id)
    consulta = db.query(REPSVMAgresor).filter(REPSVMAgresor.distrito == distrito)
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(REPSVMAgresor.nombre.contains(nombre))
    return consulta.filter(REPSVMAgresor.estatus == "A").order_by(REPSVMAgresor.id.desc()).limit(400).all()


def get_repsvm_agresor(db: Session, repsvm_agresor_id: int):
    """Consultar un repsvm_agresor"""
    return db.query(REPSVMAgresor).get(repsvm_agresor_id)
