"""
Ubicaciones de Expedientes, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_expediente

from api.autoridades.models import Autoridad
from api.distritos.models import Distrito
from api.ubicaciones_expedientes.models import UbicacionExpediente


def get_ubicaciones_expedientes(db: Session, autoridad_id: int = None, expediente: str = None):
    """ Consultar ubicaciones de expedientes """
    consulta = db.query(UbicacionExpediente, Autoridad, Distrito).select_from(UbicacionExpediente).join(Autoridad).join(Distrito)
    if autoridad_id:
        consulta = consulta.filter(UbicacionExpediente.autoridad_id == autoridad_id)
    try:
        expediente = safe_expediente(expediente)
        consulta = consulta.filter(UbicacionExpediente.expediente == expediente)
    except (IndexError, ValueError):
        pass
    return consulta.filter(UbicacionExpediente.estatus == "A").order_by(Autoridad.descripcion, UbicacionExpediente.expediente).limit(100).all()


def get_ubicacion_expediente(db: Session, ubicacion_expediente_id: int):
    """ Consultar una ubicacion de expediente """
    return db.query(UbicacionExpediente).get(ubicacion_expediente_id)
