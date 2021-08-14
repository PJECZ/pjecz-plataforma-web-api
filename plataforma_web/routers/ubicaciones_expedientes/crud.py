"""
Ubicaciones de Expedientes, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_expediente

from ..autoridades.models import Autoridad
from ..autoridades.crud import get_autoridad
from ..distritos.models import Distrito
from .models import UbicacionExpediente


def get_ubicaciones_expedientes(db: Session, autoridad_id: int = None, expediente: str = None):
    """Consultar ubicaciones de expedientes"""
    consulta = db.query(UbicacionExpediente, Autoridad, Distrito).select_from(UbicacionExpediente).join(Autoridad).join(Distrito)
    if autoridad_id:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(UbicacionExpediente.autoridad == autoridad)
    try:
        expediente = safe_expediente(expediente)
        consulta = consulta.filter(UbicacionExpediente.expediente == expediente)
    except (IndexError, ValueError):
        pass
    return consulta.filter_by(estatus="A").order_by(Autoridad.descripcion, UbicacionExpediente.expediente).limit(100).all()


def get_ubicacion_expediente(db: Session, ubicacion_expediente_id: int):
    """Consultar una ubicacion de expediente"""
    ubicacion_expediente = db.query(UbicacionExpediente).get(ubicacion_expediente_id)
    if ubicacion_expediente is None:
        raise IndexError
    if ubicacion_expediente.estatus != "A":
        raise ValueError("No es activa la ubicacion de expediente, está eliminada")
    return ubicacion_expediente
