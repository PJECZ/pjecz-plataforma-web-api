"""
Edictos, modelos
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Edicto(Base, UniversalMixin):
    """Edicto"""

    # Nombre de la tabla
    __tablename__ = "edictos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    autoridad_id = Column("autoridad", Integer, ForeignKey("autoridades.id"), index=True, nullable=False)

    # Columnas
    fecha = Column(Date, index=True, nullable=False)
    descripcion = Column(String(256), nullable=False)
    expediente = Column(String(16), index=True, nullable=False)
    numero_publicacion = Column(Integer(), nullable=False)
    archivo = Column(String(256))
    url = Column(String(512))
