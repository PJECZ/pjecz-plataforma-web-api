"""
Sentencias, modelos
"""
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Sentencia(Base, UniversalMixin):
    """Sentencia"""

    # Nombre de la tabla
    __tablename__ = "sentencias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="sentencias")
    materia_tipo_juicio_id = Column(Integer, ForeignKey("materias_tipos_juicios.id"), index=True, nullable=False)
    materia_tipo_juicio = relationship("MateriaTipoJuicio", back_populates="sentencias")

    # Columnas
    sentencia = Column(String(16), nullable=False)
    sentencia_fecha = Column(Date, index=True, nullable=True)
    expediente = Column(String(16), nullable=False)
    fecha = Column(Date, index=True, nullable=False)
    descripcion = Column(String(1024), nullable=False)
    es_perspectiva_genero = Column(Boolean, nullable=False, default=False)
    archivo = Column(String(256), nullable=False)
    url = Column(String(512), nullable=False)
