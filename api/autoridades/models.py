"""
Autoridades, modelos
"""
import sqlalchemy as db
from lib.sqlalchemy import ModelBase
from lib.universal_mixin import UniversalMixin


class Autoridad(ModelBase, UniversalMixin):
    """ Autoridad """

    # Nombre de la tabla
    __tablename__ = "autoridades"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Clave foránea
    distrito_id = db.Column("distrito", db.Integer, db.ForeignKey("distritos.id"), index=True, nullable=False)

    # Columnas
    descripcion = db.Column(db.String(256), nullable=False)
    email = db.Column(db.String(256))
