"""
Autoridades, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session

from api.autoridades.models import Autoridad
from api.distritos.models import Distrito
from api.materias.models import Materia


def get_autoridades(db: Session, distrito_id: int = None, con_notarias: bool = False, organo_jurisdiccional: str = None, materia_id: int = None):
    """Consultar autoridades"""
    consulta = db.query(Autoridad, Distrito, Materia).select_from(Autoridad).join(Distrito).join(Materia)
    if distrito_id:
        consulta = consulta.filter(Autoridad.distrito_id == distrito_id)
    if con_notarias is False:
        consulta = consulta.filter(Autoridad.es_notaria == False)
    if organo_jurisdiccional in Autoridad.ORGANOS_JURISDICCIONALES:
        consulta = consulta.filter(Autoridad.organo_jurisdiccional == organo_jurisdiccional)
    if materia_id:
        consulta = consulta.filter(Autoridad.materia_id == materia_id)
    return consulta.filter(Autoridad.es_jurisdiccional == True).filter(Autoridad.estatus == "A").order_by(Distrito.nombre, Autoridad.clave).all()


def get_autoridad(db: Session, autoridad_id: int):
    """Consultar una autoridad"""
    return db.query(Autoridad).get(autoridad_id)
