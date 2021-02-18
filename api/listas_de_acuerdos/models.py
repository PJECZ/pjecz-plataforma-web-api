"""
Listas de Acuerdos, modelos
"""
import sqlalchemy as db
from lib.universal_mixin import BaseModel, UniversalMixin


class ListaDeAcuerdo(BaseModel, UniversalMixin):
    """ Lista de Acuerdo """

    # Nombre de la tabla
    __tablename__ = "listas_de_acuerdos"

    # Clave primaria
    id = db.Column(db.Integer, primary_key=True)

    # Clave foránea
    autoridad_id = db.Column("autoridad", db.Integer, db.ForeignKey("autoridades.id"), index=True, nullable=False)

    # Columnas
    fecha = db.Column(db.Date, index=True, nullable=False)
    archivo = db.Column(db.String(256))
    descripcion = db.Column(db.String(256))
    url = db.Column(db.String(512))
