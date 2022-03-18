"""
Listas de Acuerdos, modelos
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ListaDeAcuerdo(Base, UniversalMixin):
    """ListaDeAcuerdo"""

    # Nombre de la tabla
    __tablename__ = "listas_de_acuerdos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="listas_de_acuerdos")

    # Columnas
    fecha = Column(Date, index=True, nullable=False)
    descripcion = Column(String(256), nullable=False)
    archivo = Column(String(256))
    url = Column(String(512))

    # Hijos
    listas_de_acuerdos_acuerdos = relationship("ListaDeAcuerdoAcuerdo", back_populates="lista_de_acuerdo")

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
        return f"<ListaDeAcuerdo {self.id}>"
