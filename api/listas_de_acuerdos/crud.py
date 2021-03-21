"""
Listas de Acuerdos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from api.listas_de_acuerdos.models import ListaDeAcuerdo
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_listas_de_acuerdos(db: Session, autoridad_id: int = None, fecha: date = None):
    """ Consultar listas de acuerdos """
    listas_de_acuerdos = db.query(ListaDeAcuerdo, Autoridad, Distrito).select_from(ListaDeAcuerdo).join(Autoridad).join(Distrito)
    if autoridad_id:
        listas_de_acuerdos = listas_de_acuerdos.filter(ListaDeAcuerdo.autoridad_id == autoridad_id).order_by(ListaDeAcuerdo.fecha.desc())
    if fecha:
        listas_de_acuerdos = listas_de_acuerdos.filter(ListaDeAcuerdo.fecha == fecha).order_by(Distrito.nombre, Autoridad.descripcion)
    return listas_de_acuerdos.filter(ListaDeAcuerdo.estatus == "A").limit(100).all()


def get_lista_de_acuerdo(db: Session, lista_de_acuerdo_id: int):
    """ Consultar una lista de acuerdos """
    return db.query(ListaDeAcuerdo).get(lista_de_acuerdo_id)
