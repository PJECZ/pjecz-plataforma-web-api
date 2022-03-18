"""
Ubicaciones de Expedientes, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from lib.safe_string import safe_expediente

from plataforma_web.core.autoridades.models import Autoridad
from plataforma_web.core.distritos.models import Distrito
from plataforma_web.core.ubicaciones_expedientes.models import UbicacionExpediente
from plataforma_web.v1.autoridades.crud import get_autoridad


def get_ubicaciones_expedientes(
    db: Session,
    autoridad_id: int = None,
    expediente: str = None,
):
    """Consultar ubicaciones de expedientes"""
    consulta = db.query(UbicacionExpediente, Autoridad, Distrito).select_from(UbicacionExpediente).join(Autoridad).join(Distrito)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(UbicacionExpediente.autoridad == autoridad)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise ValueError("No correcto el expediente") from error
        consulta = consulta.filter(UbicacionExpediente.expediente == expediente)
    return consulta.filter(UbicacionExpediente.estatus == "A").order_by(Autoridad.descripcion, UbicacionExpediente.expediente).limit(500).all()


def get_ubicacion_expediente(db: Session, ubicacion_expediente_id: int):
    """Consultar una ubicacion de expediente"""
    ubicacion_expediente = db.query(UbicacionExpediente).get(ubicacion_expediente_id)
    if ubicacion_expediente is None:
        raise IndexError("No existe esa ubicación de expediente")
    if ubicacion_expediente.estatus != "A":
        raise ValueError("No es activa la ubicacion de expediente, está eliminada")
    return ubicacion_expediente
