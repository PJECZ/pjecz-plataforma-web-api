"""
Autoridades, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Autoridad(Base, UniversalMixin):
    """ Autoridad """

    # Nombre de la tabla
    __tablename__ = "autoridades"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column("distrito", Integer, ForeignKey("distritos.id"), index=True, nullable=False)

    # Columnas
    descripcion = Column(String(256), nullable=False)
    es_jurisdiccional = Column(Boolean(), nullable=False, default=False)
    directorio_listas_de_acuerdos = Column(String(256))
    directorio_sentencias = Column(String(256))

    # Hijos
    listas_de_acuerdos = relationship("ListaDeAcuerdo", backref="autoridad", lazy="noload")
    ubicaciones_expedientes = relationship("UbicacionExpediente", backref="autoridad", lazy="noload")
