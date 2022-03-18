"""
REPSVM Delitos Genericos, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class REPSVMDelitoGenerico(Base, UniversalMixin):
    """REPSVMDelitoGenerico"""

    # Nombre de la tabla
    __tablename__ = "repsvm_delitos_genericos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    repsvm_delito_generico_id = Column(Integer, ForeignKey("repsvm_delitos_genericos.id"), index=True, nullable=False)
    repsvm_delito_generico = relationship("REPSVMDelitoGenerico", back_populates="repsvm_delitos_especificos")

    # Columnas
    descripcion = Column(String(256), nullable=False)

    # Hijos
    repsvm_agresores = relationship("REPSVMAgresor", back_populates="repsvm_delito_especifico", lazy="noload")

    def __repr__(self):
        """Representación"""
        return f"<REPSVMDelitoGenerico {self.id}>"
