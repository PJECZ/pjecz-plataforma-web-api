"""
Ubicaciones Expedientes v2, CRUD (create, read, update, and delete)
"""
from typing import Any
from sqlalchemy.orm import Session

from lib.safe_string import safe_expediente

from plataforma_web.core.ubicaciones_expedientes.models import UbicacionExpediente
from plataforma_web.v2.autoridades.crud import get_autoridad


def get_ubicaciones_expedientes(
    db: Session,
    autoridad_id: int = None,
    expediente: str = None,
) -> Any:
    """Consultar los Ubicaciones Expedientes activos"""
    consulta = db.query(UbicacionExpediente)
    if autoridad_id is not None:
        autoridad = get_autoridad(db, autoridad_id=autoridad_id)
        consulta = consulta.filter(UbicacionExpediente.autoridad == autoridad)
    if expediente is not None:
        try:
            expediente = safe_expediente(expediente)
        except (IndexError, ValueError) as error:
            raise ValueError("No correcto el expediente") from error
        consulta = consulta.filter(UbicacionExpediente.expediente == expediente)
    return consulta.filter_by(estatus="A").order_by(UbicacionExpediente.id.desc())


def get_ubicacion_expediente(db: Session, ubicacion_expediente_id: int) -> UbicacionExpediente:
    """Consultar un Ubicacion Expediente por su id"""
    ubicacion_expediente = db.query(UbicacionExpediente).get(ubicacion_expediente_id)
    if ubicacion_expediente is None:
        raise IndexError("No existe ese Ubicacion Expediente")
    if ubicacion_expediente.estatus != "A":
        raise ValueError("No es activo ese Ubicacion Expediente, está eliminado")
    return ubicacion_expediente
