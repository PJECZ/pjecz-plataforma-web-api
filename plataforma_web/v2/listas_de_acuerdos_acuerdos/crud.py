"""
Listas de Acuerdos Acuerdos v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.listas_de_acuerdos_acuerdos.models import ListaDeAcuerdoAcuerdo
from plataforma_web.v2.listas_de_acuerdos.crud import get_lista_de_acuerdo


def get_listas_de_acuerdos_acuerdos(
    db: Session,
    lista_de_acuerdo_id: int,
) -> Any:
    """Consultar los Acuerdos activos"""
    consulta = db.query(ListaDeAcuerdoAcuerdo)
    lista_de_acuerdo = get_lista_de_acuerdo(db, lista_de_acuerdo_id)
    consulta = consulta.filter(ListaDeAcuerdoAcuerdo.lista_de_acuerdo == lista_de_acuerdo)
    return consulta.filter_by(estatus="A").order_by(ListaDeAcuerdoAcuerdo.id.desc())


def get_lista_de_acuerdo_acuerdo(db: Session, lista_de_acuerdo_acuerdo_id: int) -> ListaDeAcuerdoAcuerdo:
    """Consultar un Acuerdo por su id"""
    lista_de_acuerdo_acuerdo = db.query(ListaDeAcuerdoAcuerdo).get(lista_de_acuerdo_acuerdo_id)
    if lista_de_acuerdo_acuerdo is None:
        raise IndexError("No existe ese Acuerdo")
    if lista_de_acuerdo_acuerdo.estatus != "A":
        raise ValueError("No es activo ese Acuerdo, está eliminado")
    return lista_de_acuerdo_acuerdo
