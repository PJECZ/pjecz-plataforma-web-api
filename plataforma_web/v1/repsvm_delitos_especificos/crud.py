"""
REPSVM Delitos Especificos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from .models import REPSVMDelitoEspecifico


def get_repsvm_delitos_especificos(db: Session):
    """ Consultar repsvm_delitos_especificos activos """
    return db.query(REPSVMDelitoEspecifico).filter(REPSVMDelitoEspecifico.estatus == 'A').order_by(REPSVMDelitoEspecifico.descripcion).all()


def get_repsvm_delito_especifico(db: Session, repsvm_delito_especifico_id: int):
    """ Consultar un repsvm_delito_especifico """
    return db.query(REPSVMDelitoEspecifico).get(repsvm_delito_especifico_id)
