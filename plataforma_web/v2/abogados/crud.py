"""
Abogados v2, CRUD (create, read, update, and delete)
"""
from datetime import datetime, date
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from ...core.abogados.models import Abogado


def get_abogados(
    db: Session,
    nombre: str = None,
    anio_desde: int = None,
    anio_hasta: int = None,
) -> Any:
    """Consultar los Abogados activos"""
    consulta = db.query(Abogado)
    if anio_desde is not None:
        if 1925 <= anio_desde <= datetime.now().year:
            consulta = consulta.filter(Abogado.fecha >= date(year=anio_desde, month=1, day=1))
        else:
            raise ValueError("Año fuera de rango.")
    if anio_hasta is not None:
        if 1925 <= anio_hasta <= datetime.now().year:
            consulta = consulta.filter(Abogado.fecha <= date(year=anio_hasta, month=12, day=31))
        else:
            raise ValueError("Año fuera de rango.")
    if nombre is not None:
        nombre = safe_string(nombre)
        if nombre != "":
            consulta = consulta.filter(Abogado.nombre.contains(nombre))
    return consulta.filter_by(estatus="A").order_by(Abogado.id.desc())


def get_abogado(db: Session, abogado_id: int) -> Abogado:
    """Consultar un Abogado por su id"""
    abogado = db.query(Abogado).get(abogado_id)
    if abogado is None:
        raise IndexError("No existe ese Abogado")
    if abogado.estatus != "A":
        raise ValueError("No es activo ese Abogado, está eliminado")
    return abogado
