"""
Listas de Acuerdos v2, CRUD (create, read, update, and delete)
"""
from datetime import date
from typing import Any
from sqlalchemy.orm import Session

from plataforma_web.core.listas_de_acuerdos.models import ListaDeAcuerdo
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_listas_de_acuerdos(
    db: Session,
    autoridad_id: int = None,
    fecha: date = None,
    anio: int = None,
) -> Any:
    """Consultar los Listas de Acuerdos activos"""
    consulta = db.query(ListaDeAcuerdo)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(ListaDeAcuerdo.autoridad == autoridad)
    if fecha is not None:
        consulta = consulta.filter(ListaDeAcuerdo.fecha == fecha)
    if anio is not None:
        if 2000 <= anio <= date.today().year:
            consulta = consulta.filter(ListaDeAcuerdo.fecha >= date(anio, 1, 1)).filter(ListaDeAcuerdo.fecha <= date(anio, 12, 31))
        else:
            raise ValueError("Año fuera de rango.")
    return consulta.filter_by(estatus="A").order_by(ListaDeAcuerdo.id.desc())


def get_lista_de_acuerdo(db: Session, lista_de_acuerdo_id: int) -> ListaDeAcuerdo:
    """Consultar un Lista de Acuerdo por su id"""
    lista_de_acuerdo = db.query(ListaDeAcuerdo).get(lista_de_acuerdo_id)
    if lista_de_acuerdo is None:
        raise IndexError("No existe ese Lista de Acuerdo")
    if lista_de_acuerdo.estatus != "A":
        raise ValueError("No es activo ese Lista de Acuerdo, está eliminado")
    return lista_de_acuerdo
