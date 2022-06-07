"""
REPSVM Delitos Genericos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from ...core.repsvm_delitos_genericos.models import REPSVMDelitoGenerico


def get_repsvm_delitos_genericos(db: Session):
    """Consultar repsvm_delitos_genericos activos"""
    return db.query(REPSVMDelitoGenerico).filter(REPSVMDelitoGenerico.estatus == "A").order_by(REPSVMDelitoGenerico.nombre).limit(400).all()


def get_repsvm_delito_generico(db: Session, repsvm_delito_generico_id: int):
    """Consultar un repsvm_delito_generico"""
    return db.query(REPSVMDelitoGenerico).get(repsvm_delito_generico_id)
