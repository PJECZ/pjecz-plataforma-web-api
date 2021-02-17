"""
Ubicaciones de Expedientes, modelos
"""
from collections import OrderedDict
import sqlalchemy as db
from lib.universal_mixin import BaseModel, UniversalMixin


class UbicacionExpediente(BaseModel, UniversalMixin):
    """ Ubicacion de Expediente """

    UBICACIONES = OrderedDict(
        [
            ("ARCHIVO", "Archivo"),
            ("JUZGADO", "Juzgado"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "ubicaciones_expedientes"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Clave foránea
    autoridad_id = db.Column("autoridad", db.Integer, db.ForeignKey("autoridades.id"), index=True, nullable=False)

    # Columnas
    expediente = db.Column(db.String(256), nullable=False)
    ubicacion = db.Column(
        db.Enum(*UBICACIONES, name="ubicaciones_opciones", native_enum=False),
        index=True,
        nullable=False,
    )
