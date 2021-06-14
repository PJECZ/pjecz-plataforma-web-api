"""
Autoridades, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Autoridad(Base, UniversalMixin):
    """Autoridad"""

    # Nombre de la tabla
    __tablename__ = "autoridades"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column(Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    distrito = relationship("Distrito", back_populates="autoridades")

    # Columnas
    descripcion = Column(String(256), nullable=False)
    clave = Column(String(16), nullable=False, unique=True)
    es_jurisdiccional = Column(Boolean(), nullable=False, default=False)
    es_notaria = Column(Boolean(), nullable=False, default=False)
    directorio_edictos = Column(String(256))
    directorio_glosas = Column(String(256))
    directorio_listas_de_acuerdos = Column(String(256))
    directorio_sentencias = Column(String(256))

    # Hijos
    edictos = relationship("Edicto", back_populates="autoridad")
    listas_de_acuerdos = relationship("ListaDeAcuerdo", back_populates="autoridad")
    sentencias = relationship("Sentencia", back_populates="autoridad")
    ubicaciones_expedientes = relationship("UbicacionExpediente", back_populates="autoridad")
