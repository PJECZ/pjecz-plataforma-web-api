"""
REPSVM Tipos Sentencias, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class REPSVMTipoSentencia(Base, UniversalMixin):
    """REPSVMTipoSentencia"""

    # Nombre de la tabla
    __tablename__ = "repsvm_tipos_sentencias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(256), unique=True, nullable=False)

    # Hijos
    repsvm_agresores = relationship("REPSVMAgresor", back_populates="repsvm_tipo_sentencia", lazy="noload")

    def __repr__(self):
        """Representación"""
        return f"<REPSVMTipoSentencia {self.nombre}>"
