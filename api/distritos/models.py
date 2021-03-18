"""
Distritos, modelos
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Distrito(Base, UniversalMixin):
    """ Distrito """

    # Nombre de la tabla
    __tablename__ = "distritos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Columnas
    nombre = Column(String(256), unique=True, nullable=False)

    # Hijos
    autoridades = relationship("Autoridad", backref="distrito")
    peritos = relationship("Perito", backref="distrito", lazy="dynamic")
