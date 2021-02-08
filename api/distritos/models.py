"""
Distritos, modelos
"""
import sqlalchemy as db
from sqlalchemy.orm import relationship
from lib.sqlalchemy import ModelBase
from lib.universal_mixin import UniversalMixin


class Distrito(ModelBase, UniversalMixin):
    """ Distrito """

    # Nombre de la tabla
    __tablename__ = "distritos"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Columnas
    nombre = db.Column(db.String(256), unique=True, nullable=False)

    # Hijos
    autoridades = relationship("Autoridad", backref="distrito")
