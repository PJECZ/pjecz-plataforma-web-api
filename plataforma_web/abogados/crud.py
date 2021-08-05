"""
Abogados, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import datetime
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from plataforma_web.abogados.models import Abogado


def get_abogados(db: Session, nombre: str, ano_desde: int = None, ano_hasta: int = None):
    """Consultar abogados"""
    consulta = db.query(Abogado)
    if ano_desde and ano_desde > 1925:
        consulta = consulta.filter(Abogado.fecha >= datetime.strptime(f"{ano_desde}-01-01", "%Y-%m-%d"))
    if ano_hasta and ano_hasta < datetime.now().year:
        consulta = consulta.filter(Abogado.fecha <= datetime.strptime(f"{ano_hasta}-12-31", "%Y-%m-%d"))
    nombre = safe_string(nombre)
    if nombre != "":
        consulta = consulta.filter(Abogado.nombre.like(f"%{nombre}%"))
    return consulta.filter(Abogado.estatus == "A").order_by(Abogado.nombre).limit(100).all()


def get_abogado(db: Session, abogado_id: int):
    """Consultar un abogado"""
    return db.query(Abogado).get(abogado_id)
