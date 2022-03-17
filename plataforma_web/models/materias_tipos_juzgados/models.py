"""
Materias Tipos de Juzgados v2, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class MateriaTipoJuzgado(Base, UniversalMixin):
    """MateriaTipoJuzgado"""

    # Nombre de la tabla
    __tablename__ = "materias_tipos_juzgados"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    materia_id = Column(Integer, ForeignKey("materias.id"), index=True, nullable=False)
    materia = relationship("Materia", back_populates="materias_tipos_juzgados")

    # Columnas
    descripcion = Column(String(256), nullable=False)

    # Hijos
    # repsvm_agresores = relationship("REPSVMAgresor", back_populates="materia_tipo_juzgado", lazy="noload")

    @property
    def materia_nombre(self):
        """Nombre de la materia"""
        return self.materia.nombre

    def __repr__(self):
        """Representación"""
        return f"<MateriaTipoJuzgado {self.descripcion}>"
