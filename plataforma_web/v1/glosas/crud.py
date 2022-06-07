"""
Glosas, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from ...core.autoridades.models import Autoridad
from ...core.distritos.models import Distrito
from ...core.glosas.models import Glosa
from ..autoridades.crud import get_autoridad


def get_glosas(
    db: Session,
    autoridad_id: int = None,
    ano: int = None,
):
    """Consultar glosas"""
    glosas = db.query(Glosa, Autoridad, Distrito).select_from(Glosa).join(Autoridad).join(Distrito)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        glosas = glosas.filter(Glosa.autoridad == autoridad)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            glosas = glosas.filter(Glosa.fecha >= date(ano, 1, 1)).filter(Glosa.fecha <= date(ano, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return glosas.filter(Glosa.estatus == "A").order_by(Glosa.fecha.desc()).limit(400).all()


def get_glosa(db: Session, glosa_id: int):
    """Consultar un glosa"""
    glosa = db.query(Glosa).get(glosa_id)
    if glosa is None:
        raise IndexError("No existe esa glosa")
    if glosa.estatus != "A":
        raise ValueError("No es activa la glosa, está eliminada")
    return glosa
