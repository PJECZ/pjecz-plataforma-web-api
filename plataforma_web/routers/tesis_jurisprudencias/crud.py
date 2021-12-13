"""
Tesis Jurisprudencias, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from plataforma_web.routers.tesis_jurisprudencias.models import TesisJurisprudencia
from plataforma_web.routers.autoridades.models import Autoridad
from plataforma_web.routers.distritos.models import Distrito


def get_tesis_jurisprudencias(db: Session, autoridad_id: int = None):
    """ Consultar tesis_jurisprudencias """
    tesis_jurisprudencias = db.query(TesisJurisprudencia, Autoridad, Distrito).select_from(TesisJurisprudencia).join(Autoridad).join(Distrito)
    if autoridad_id:
        tesis_jurisprudencias = tesis_jurisprudencias.filter(TesisJurisprudencia.autoridad_id == autoridad_id).order_by(TesisJurisprudencia.id.desc())
    return tesis_jurisprudencias.filter(TesisJurisprudencia.estatus == 'A').limit(500).all()


def get_tesis_jurisprudencia(db: Session, tesis_jurisprudencia_id: int):
    """ Consultar un tesis_jurisprudencia """
    return db.query(TesisJurisprudencia).get(tesis_jurisprudencia_id)
