"""
Glosas, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from ..autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad
from ..distritos.models import Distrito
from .models import Glosa


def get_glosas(db: Session, autoridad_id: int = None, ano: int = None):
    """Consultar glosas"""
    glosas = db.query(Glosa, Autoridad, Distrito).select_from(Glosa).join(Autoridad).join(Distrito)
    if autoridad_id:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        glosas = glosas.filter(Glosa.autoridad == autoridad)
    if ano is not None and 2000 <= ano <= date.today().year:
        glosas = glosas.filter(Glosa.fecha >= date(ano, 1, 1)).filter(Glosa.fecha <= date(ano, 12, 31))
    return glosas.filter_by(estatus="A").order_by(Glosa.fecha.desc()).limit(100).all()


def get_glosa(db: Session, glosa_id: int):
    """Consultar un glosa"""
    glosa = db.query(Glosa).get(glosa_id)
    if glosa is None:
        raise IndexError
    if glosa.estatus != "A":
        raise ValueError("No es activa la glosa, está eliminada")
    return glosa
