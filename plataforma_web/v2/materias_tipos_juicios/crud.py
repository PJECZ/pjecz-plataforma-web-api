"""
Materias Tipos de Juicios v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from .models import MateriaTipoJuicio
from ..materias.crud import get_materia


def get_materias_tipos_juicios(db: Session, materia_id: int = None) -> Any:
    """Consultar los tipos de juicios activos"""
    consulta = db.query(MateriaTipoJuicio)
    if materia_id is not None:
        materia = get_materia(db, materia_id)
        consulta = consulta.filter(MateriaTipoJuicio.materia == materia)
    return consulta.filter(MateriaTipoJuicio.estatus == "A").order_by(MateriaTipoJuicio.id)


def get_materia_tipo_juicio(db: Session, materia_tipo_juicio_id: int) -> MateriaTipoJuicio:
    """Consultar un tipo de juicio por su id"""
    materia_tipo_juicio = db.query(MateriaTipoJuicio).get(materia_tipo_juicio_id)
    if materia_tipo_juicio is None:
        raise IndexError("No existe ese tipo de juicio")
    if materia_tipo_juicio.estatus != "A":
        raise ValueError("No es activo ese tipo de juicio, está eliminado")
    return materia_tipo_juicio
