"""
Distritos, modelos
"""
from sqlalchemy import Column, Integer, String, Boolean
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
    es_distrito_judicial = Column(Boolean(), nullable=False, default=False)

    # Hijos
    autoridades = relationship("Autoridad", backref="distrito")
    peritos = relationship("Perito", backref="distrito", lazy="dynamic")
