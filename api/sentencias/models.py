"""
Sentencias, modelos
"""
from sqlalchemy import Boolean, Column, Date, ForeignKey, Integer, String
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Sentencia(Base, UniversalMixin):
    """Sentencia"""

    # Nombre de la tabla
    __tablename__ = "sentencias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    autoridad_id = Column("autoridad", Integer, ForeignKey("autoridades.id"), index=True, nullable=False)

    # Columnas
    fecha = Column(Date, index=True, nullable=False)
    sentencia = Column(String(16), index=True, nullable=False)
    expediente = Column(String(16), index=True, nullable=False)
    es_paridad_genero = Column(Boolean, nullable=False, default=False)
    archivo = Column(String(256))
    url = Column(String(512))
