"""
Glosas, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.autoridades.models import Autoridad
from api.distritos.models import Distrito
from api.glosas.models import Glosa


def get_glosas(db: Session, autoridad_id: int = None, ano: int = None):
    """Consultar glosas"""
    glosas = db.query(Glosa, Autoridad, Distrito).select_from(Glosa).join(Autoridad).join(Distrito)
    if autoridad_id:
        glosas = glosas.filter(Glosa.autoridad_id == autoridad_id)
    if 2000 <= ano <= date.today().year:
        glosas = glosas.filter(Glosa.fecha >= date(ano, 1, 1)).filter(Glosa.fecha <= date(ano, 12, 31))
    return glosas.filter(Glosa.estatus == "A").order_by(Glosa.fecha.desc()).limit(100).all()


def get_glosa(db: Session, glosa_id: int):
    """Consultar un glosa"""
    return db.query(Glosa).get(glosa_id)
