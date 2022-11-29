"""
Materias Tipos de Juzgados v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from ...core.materias_tipos_juzgados.models import MateriaTipoJuzgado
from ..materias.crud import get_materia


def get_materias_tipos_juzgados(db: Session, materia_id: int = None) -> Any:
    """Consultar los tipos de juzgados activos"""
    consulta = db.query(MateriaTipoJuzgado)
    if materia_id is not None and materia_id != 0:
        materia = get_materia(db, materia_id)
        consulta = consulta.filter(MateriaTipoJuzgado.materia == materia)
    return consulta.filter_by(estatus="A").order_by(MateriaTipoJuzgado.descripcion)


def get_materia_tipo_juzgado(db: Session, materia_tipo_juzgado_id: int) -> MateriaTipoJuzgado:
    """Consultar un tipo de juzgado por su id"""
    materia_tipo_juzgado = db.query(MateriaTipoJuzgado).get(materia_tipo_juzgado_id)
    if materia_tipo_juzgado is None:
        raise IndexError("No existe ese tipo de juzgado")
    if materia_tipo_juzgado.estatus != "A":
        raise ValueError("No es activo ese tipo de juzgado, está eliminado")
    return materia_tipo_juzgado
