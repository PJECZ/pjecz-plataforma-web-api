"""
Listas de Acuerdos, modelos
"""
from sqlalchemy import Column, Date, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class ListaDeAcuerdo(Base, UniversalMixin):
    """ Lista de Acuerdo """

    __tablename__ = "listas_de_acuerdos"

    id = Column(Integer, primary_key=True)
    autoridad_id = Column("autoridad", Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    fecha = Column(Date, index=True, nullable=False)
    archivo = Column(String(256), nullable=False)
    descripcion = Column(String(256))
    url = Column(String(512), nullable=False)
