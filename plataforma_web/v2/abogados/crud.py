"""
Abogados v2, CRUD (create, read, update, and delete)
"""
from datetime import datetime
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_string

from plataforma_web.core.abogados.models import Abogado


def get_abogados(
    db: Session,
    nombre: str,
    ano_desde: int = None,
    ano_hasta: int = None,
) -> Any:
    """Consultar los Abogados activos"""
    consulta = db.query(Abogado)
    if ano_desde is not None:
        if 1925 <= ano_desde <= datetime.now().year:
            consulta = consulta.filter(Abogado.fecha >= datetime.strptime(f"{ano_desde}-01-01", "%Y-%m-%d"))
        else:
            raise ValueError("Año fuera de rango.")
    if ano_hasta is not None:
        if 1925 <= ano_hasta <= datetime.now().year:
            consulta = consulta.filter(Abogado.fecha <= datetime.strptime(f"{ano_hasta}-12-31", "%Y-%m-%d"))
        else:
            raise ValueError("Año fuera de rango.")
    nombre = safe_string(nombre)
    if nombre != "":
        consulta = consulta.filter(Abogado.nombre.contains(nombre))
    return consulta.filter_by(estatus="A").order_by(Abogado.id)


def get_abogado(db: Session, abogado_id: int) -> Abogado:
    """Consultar un Abogado por su id"""
    abogado = db.query(Abogado).get(abogado_id)
    if abogado is None:
        raise IndexError("No existe ese Abogado")
    if abogado.estatus != "A":
        raise ValueError("No es activo ese Abogado, está eliminado")
    return abogado
