"""
Abogados, modelos
"""
import sqlalchemy as db
from lib.universal_mixin import BaseModel, UniversalMixin


class Abogado(BaseModel, UniversalMixin):
    """ Abogado """

    # Nombre de la tabla
    __tablename__ = "abogados"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Columnas
    fecha = db.Column(db.Date, nullable=False, index=True)
    numero = db.Column(db.String(16), nullable=False)  # Hay datos como 000-Bis
    nombre = db.Column(db.String(256), nullable=False)
    libro = db.Column(db.String(256), nullable=False)
