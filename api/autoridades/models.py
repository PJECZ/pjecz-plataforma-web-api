"""
Autoridades, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Autoridad(Base, UniversalMixin):
    """ Autoridad """

    __tablename__ = "autoridades"

    id = Column(Integer, primary_key=True)
    distrito_id = Column("distrito", Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    descripcion = Column(String(256), nullable=False)
    email = Column(String(256))
