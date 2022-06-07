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
    ubicacion = Column(
        Enum(*UBICACIONES, name="ubicaciones_opciones", native_enum=False),
        index=True,
        nullable=False,
    )

    @property
    def distrito_id(self):
        """ID del distrito"""
        return self.autoridad.distrito_id

    @property
    def distrito_nombre(self):
        """Nombre del distrito"""
        return self.autoridad.distrito.nombre

    @property
    def distrito_nombre_corto(self):
        """Nombre corto del distrito"""
        return self.autoridad.distrito.nombre_corto

    @property
    def autoridad_clave(self):
        """Nombre de la autoridad"""
        return self.autoridad.clave

    @property
    def autoridad_descripcion(self):
        """Descripcion de la autoridad"""
        return self.autoridad.descripcion

    @property
    def autoridad_descripcion_corta(self):
        """Descripcion corta de la autoridad"""
        return self.autoridad.descripcion_corta

    def __repr__(self):
        """Representación"""
        return f"<UbicacionExpediente {self.id}>"
