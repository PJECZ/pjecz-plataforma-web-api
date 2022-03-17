"""
Materias v2, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Materia(Base, UniversalMixin):
    """Materia"""

    # Nombre de la tabla
    __tablename__ = "materias"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(64), unique=True, nullable=False)

    # Hijos
    autoridades = relationship("Autoridad", back_populates="materia", lazy="noload")
    materias_tipos_juicios = relationship("MateriaTipoJuicio", back_populates="materia", lazy="noload")
    materias_tipos_juzgados = relationship('MateriaTipoJuzgado', back_populates='materia', lazy="noload")
    #tesis_jurisprudencias = relationship("TesisJurisprudencia", back_populates="materia", lazy="noload")

    def __repr__(self):
        """Representación"""
        return f"<Materia {self.nombre}>"
