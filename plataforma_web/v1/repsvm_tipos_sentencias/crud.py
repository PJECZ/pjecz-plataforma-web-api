"""
REPSVM Tipos de Sentencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from plataforma_web.core.repsvm_tipos_sentencias.models import REPSVMTipoSentencia


def get_repsvm_tipos_sentencias(db: Session):
    """Consultar repsvm_tipos_sentencias activos"""
    return db.query(REPSVMTipoSentencia).filter(REPSVMTipoSentencia.estatus == "A").order_by(REPSVMTipoSentencia.nombre).limit(400).all()


def get_repsvm_tipo_sentencia(db: Session, repsvm_tipo_sentencia_id: int):
    """Consultar un repsvm_tipo_sentencia"""
    return db.query(REPSVMTipoSentencia).get(repsvm_tipo_sentencia_id)
