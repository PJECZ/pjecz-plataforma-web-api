"""
Edictos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from ..autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad
from ..distritos.models import Distrito
from .models import Edicto


def get_edictos(
    db: Session,
    autoridad_id: int = None,
    ano: int = None,
):
    """Consultar edictos"""
    edictos = db.query(Edicto, Autoridad, Distrito).select_from(Edicto).join(Autoridad).join(Distrito)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        edictos = edictos.filter(Edicto.autoridad == autoridad)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            edictos = edictos.filter(Edicto.fecha >= date(ano, 1, 1)).filter(Edicto.fecha <= date(ano, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return edictos.filter(Edicto.estatus == "A").order_by(Edicto.fecha.desc()).limit(500).all()


def get_edicto(db: Session, edicto_id: int):
    """Consulta un edicto"""
    edicto = db.query(Edicto).get(edicto_id)
    if edicto is None:
        raise IndexError
    if edicto.estatus != "A":
        raise ValueError("No es activo el edicto, está eliminado")
    return edicto
