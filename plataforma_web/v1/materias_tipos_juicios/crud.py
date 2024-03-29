"""
Materias Tipos Juicios, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from ...core.materias.models import Materia
from ...core.materias_tipos_juicios.models import MateriaTipoJuicio
from ..materias.crud import get_materia


def get_materias_tipos_juicios(db: Session, materia_id: int):
    """Consultar tipos de juicios activos"""
    materia = get_materia(db, materia_id)
    return db.query(MateriaTipoJuicio, Materia).join(Materia).filter(MateriaTipoJuicio.materia == materia).filter(MateriaTipoJuicio.estatus == "A").order_by(MateriaTipoJuicio.descripcion).limit(400).all()


def get_materia_tipo_juicio(db: Session, materia_tipo_juicio_id: int):
    """Consultar un tipo de juicio"""
    return db.query(MateriaTipoJuicio).get(materia_tipo_juicio_id)
