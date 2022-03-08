"""
REPSVM, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from plataforma_web.routers.repsvm_agresores.models import REPSVMAgresor


def get_repsvm_agresores(db: Session):
    """Consultar repsvm_agresores activos"""
    return db.query(REPSVMAgresor).filter(REPSVMAgresor.estatus == "A").order_by(REPSVMAgresor.id.desc()).limit(50).all()


def get_repsvm_agresor(db: Session, repsvm_agresor_id: int):
    """Consultar un repsvm_agresor"""
    return db.query(REPSVMAgresor).get(repsvm_agresor_id)
