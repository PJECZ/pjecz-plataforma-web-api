"""
REPSVM Delitos Genericos, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class REPSVMDelitoGenerico(Base, UniversalMixin):
    """REPSVMDelitoGenerico"""

    # Nombre de la tabla
    __tablename__ = 'repsvm_delitos_genericos'

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(256), unique=True, nullable=False)

    # Hijos
    repsvm_delitos_especificos = relationship("REPSVMDelitoEspecifico", back_populates="repsvm_delito_generico", lazy="noload")
