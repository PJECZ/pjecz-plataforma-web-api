"""
Autoridades, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_string

from plataforma_web.autoridades.models import Autoridad
from plataforma_web.distritos.models import Distrito
from plataforma_web.distritos.crud import get_distrito
from plataforma_web.materias.models import Materia
from plataforma_web.materias.crud import get_materia


def get_autoridades(
    db: Session,
    distrito_id: int = None,
    materia_id: int = None,
    organo_jurisdiccional: str = None,
    con_notarias: bool = False,
    para_glosas: bool = False,
):
    """Consultar autoridades"""
    consulta = db.query(Autoridad, Distrito, Materia).select_from(Autoridad).join(Distrito).join(Materia)
    if distrito_id:
        distrito = get_distrito(db, distrito_id)
        consulta = consulta.filter(Autoridad.distrito == distrito)
    if materia_id:
        materia = get_materia(db, materia_id)
        consulta = consulta.filter(Autoridad.materia == materia)
    organo_jurisdiccional = safe_string(organo_jurisdiccional)
    if organo_jurisdiccional in Autoridad.ORGANOS_JURISDICCIONALES:
        consulta = consulta.filter_by(organo_jurisdiccional=organo_jurisdiccional)
    if con_notarias is False:
        consulta = consulta.filter_by(es_notaria=False)
    if para_glosas:
        consulta = consulta.filter(Autoridad.organo_jurisdiccional.in_(["PLENO O SALA DEL TSJ", "TRIBUNAL DE CONCILIACION Y ARBITRAJE"]))
    return consulta.filter_by(es_jurisdiccional=True).filter_by(estatus="A").order_by(Distrito.nombre, Autoridad.clave).all()


def get_autoridad(db: Session, autoridad_id: int):
    """Consultar una autoridad"""
    autoridad = db.query(Autoridad).get(autoridad_id)
    if autoridad is None:
        raise IndexError
    if autoridad.estatus != "A":
        raise ValueError("No es activa la autoridad, está eliminada")
    return autoridad
