"""
Materias Tipos de Juzgados, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from plataforma_web.routers.materias_tipos_juzgados.models import MateriaTipoJuzgado

from plataforma_web.routers.materias.models import Materia
from plataforma_web.routers.materias.crud import get_materia


def get_materias_tipos_juzgados(db: Session, materia_id: int):
    """Consultar materias_tipos_juzgados activos"""
    materia = get_materia(db, materia_id)
    return db.query(MateriaTipoJuzgado, Materia).join(Materia).filter(MateriaTipoJuzgado.materia == materia).filter(MateriaTipoJuzgado.estatus == "A").order_by(MateriaTipoJuzgado.descripcion).all()


def get_materia_tipo_juzgado(db: Session, materia_tipo_juzgado_id: int):
    """Consultar un materia_tipo_juzgado"""
    return db.query(MateriaTipoJuzgado).get(materia_tipo_juzgado_id)
