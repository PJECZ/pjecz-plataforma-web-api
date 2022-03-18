"""
Abogados v1, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import datetime
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from plataforma_web.core.abogados.models import Abogado


def get_abogados(
    db: Session,
    nombre: str,
    ano_desde: int = None,
    ano_hasta: int = None,
):
    """Consultar abogados"""
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
        consulta = consulta.filter(Abogado.nombre.like(f"%{nombre}%"))
    return consulta.filter_by(estatus="A").order_by(Abogado.nombre).limit(500).all()


def get_abogado(db: Session, abogado_id: int):
    """Consultar un abogado"""
    abogado = db.query(Abogado).get(abogado_id)
    if abogado is None:
        raise IndexError("No existe ese abogado registrado")
    if abogado.estatus != "A":
        raise ValueError("No es activo el abogado, está eliminado")
    return abogado
