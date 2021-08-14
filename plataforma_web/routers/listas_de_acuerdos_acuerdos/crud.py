"""
Listas de Acuerdos Acuerdos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from ..listas_de_acuerdos.models import ListaDeAcuerdo
from ..listas_de_acuerdos.crud import get_lista_de_acuerdo
from .models import ListaDeAcuerdoAcuerdo


def get_listas_de_acuerdos_acuerdos(db: Session, lista_de_acuerdo_id: int):
    """Consultar listas_de_acuerdos_acuerdos"""
    consulta = db.query(ListaDeAcuerdoAcuerdo, ListaDeAcuerdo).join(ListaDeAcuerdo)
    lista_de_acuerdo = get_lista_de_acuerdo(db, lista_de_acuerdo_id)
    consulta = consulta.filter(ListaDeAcuerdoAcuerdo.lista_de_acuerdo == lista_de_acuerdo)
    return consulta.filter_by(estatus="A").order_by(ListaDeAcuerdoAcuerdo.id).limit(500).all()


def get_lista_de_acuerdo_acuerdo(db: Session, lista_de_acuerdo_acuerdo_id: int):
    """Consultar un lista_de_acuerdo_acuerdo"""
    acuerdo = db.query(ListaDeAcuerdoAcuerdo).get(lista_de_acuerdo_acuerdo_id)
    if acuerdo is None:
        raise IndexError
    if acuerdo.estatus != "A":
        raise ValueError("No es activo el acuerdo, está eliminado")
    return acuerdo
