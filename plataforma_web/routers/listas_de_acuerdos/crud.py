"""
Listas de Acuerdos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import date
from sqlalchemy.orm import Session

from ..autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad
from ..distritos.models import Distrito
from .models import ListaDeAcuerdo


def get_listas_de_acuerdos(
    db: Session,
    autoridad_id: int = None,
    fecha: date = None,
    ano: int = None,
):
    """Consultar listas de acuerdos"""
    listas_de_acuerdos = db.query(ListaDeAcuerdo, Autoridad, Distrito).select_from(ListaDeAcuerdo).join(Autoridad).join(Distrito)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        listas_de_acuerdos = listas_de_acuerdos.filter(ListaDeAcuerdo.autoridad == autoridad)
    if fecha is not None:
        listas_de_acuerdos = listas_de_acuerdos.filter(ListaDeAcuerdo.fecha == fecha)
    if ano is not None:
        if 2000 <= ano <= date.today().year:
            listas_de_acuerdos = listas_de_acuerdos.filter(ListaDeAcuerdo.fecha >= date(ano, 1, 1)).filter(ListaDeAcuerdo.fecha <= date(ano, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return listas_de_acuerdos.filter(ListaDeAcuerdo.estatus == "A").order_by(ListaDeAcuerdo.fecha.desc()).limit(500).all()


def get_lista_de_acuerdo(db: Session, lista_de_acuerdo_id: int):
    """Consultar una lista de acuerdos"""
    lista_de_acuerdo = db.query(ListaDeAcuerdo).get(lista_de_acuerdo_id)
    if lista_de_acuerdo is None:
        raise IndexError
    if lista_de_acuerdo.estatus != "A":
        raise ValueError("No es activa la lista de acuerdos, está eliminada")
    return lista_de_acuerdo
