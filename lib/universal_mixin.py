"""
UniversalMixin define las columnas y métodos comunes de todos los modelos
"""
import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


class UniversalMixin:
    """ Columnas y métodos comunes a todas las tablas """

    estatus = db.Column(db.String(1), server_default="A", nullable=False)
