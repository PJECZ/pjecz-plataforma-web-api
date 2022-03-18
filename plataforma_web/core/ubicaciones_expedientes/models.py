"""
Ubicaciones Expedientes, modelos
"""
from collections import OrderedDict
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class UbicacionExpediente(Base, UniversalMixin):
    """UbicacionExpediente"""

    UBICACIONES = OrderedDict(
        [
            ("ARCHIVO", "Archivo"),
            ("JUZGADO", "Juzgado"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "ubicaciones_expedientes"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="ubicaciones_expedientes")

    # Columnas
    expediente = Column(String(256), nullable=False)
    ubicacion = Column(Enum(*UBICACIONES, name="ubicaciones_opciones", native_enum=False), index=True, nullable=False)

    def __repr__(self):
        """Representación"""
        return f"<UbicacionExpediente {self.id}>"
