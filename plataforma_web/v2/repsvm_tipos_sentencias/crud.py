"""
REPSVM Tipos de Sentencias v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from ...core.repsvm_tipos_sentencias.models import REPSVMTipoSentencia


def get_repsvm_tipos_sentencias(db: Session) -> Any:
    """Consultar los Tipos de Sentencias activos"""
    return db.query(REPSVMTipoSentencia).filter_by(estatus="A").order_by(REPSVMTipoSentencia.nombre)


def get_repsvm_tipo_sentencia(db: Session, repsvm_tipo_sentencia_id: int) -> REPSVMTipoSentencia:
    """Consultar un Tipo de Sentencia por su id"""
    repsvm_tipo_sentencia = db.query(REPSVMTipoSentencia).get(repsvm_tipo_sentencia_id)
    if repsvm_tipo_sentencia is None:
        raise IndexError("No existe ese Tipo de Sentencia")
    if repsvm_tipo_sentencia.estatus != "A":
        raise ValueError("No es activo ese Tipo de Sentencia, está eliminado")
    return repsvm_tipo_sentencia
