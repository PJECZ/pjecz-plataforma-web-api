"""
Edictos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from api.edictos.models import Edicto
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_edictos(db: Session, autoridad_id: int = None):
    """Consultar edictos"""
    edictos = db.query(Edicto, Autoridad, Distrito).select_from(Edicto).join(Autoridad).join(Distrito)
    if autoridad_id:
        edictos = edictos.filter(Edicto.autoridad_id == autoridad_id).order_by(Edicto.fecha.desc())
    return edictos.filter(Edicto.estatus == "A").limit(500).all()


def get_edicto(db: Session, edicto_id: int):
    """Consulta un edicto"""
    return db.query(Edicto).get(edicto_id)
