"""
Distritos, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Distrito(Base, UniversalMixin):
    """ Distrito """

    __tablename__ = "distritos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(256), unique=True, nullable=False)
    autoridades = relationship("Autoridad", backref="distrito")
