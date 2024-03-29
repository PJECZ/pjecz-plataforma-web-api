"""
Distritos, modelos
"""
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Distrito(Base, UniversalMixin):
    """Distrito"""

    # Nombre de la tabla
    __tablename__ = "distritos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    clave = Column(String(16), nullable=False, unique=True)
    nombre = Column(String(256), unique=True, nullable=False)
    nombre_corto = Column(String(64), nullable=False, default="")
    es_distrito_judicial = Column(Boolean(), nullable=False, default=False)

    # Hijos
    autoridades = relationship("Autoridad", back_populates="distrito", lazy="noload")
    peritos = relationship("Perito", back_populates="distrito", lazy="noload")
    repsvm_agresores = relationship("REPSVMAgresor", back_populates="distrito", lazy="noload")

    def __repr__(self):
        """Representación"""
        return f"<Distrito {self.nombre}>"
