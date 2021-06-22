"""
Autoridades, modelos
"""
from collections import OrderedDict
from sqlalchemy import Column, Enum, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Autoridad(Base, UniversalMixin):
    """Autoridad"""

    ORGANOS_JURISDICCIONALES = OrderedDict(
        [
            ("NO DEFINIDO", "No Definido"),
            ("JUZGADO DE PRIMERA INSTANCIA", "Juzgado de Primera Instancia"),
            ("PLENO O SALA DEL TSJ", "Pleno o Sala del TSJ"),
            ("TRIBUNAL DISTRITAL", "Tribunal Distrital"),
            ("TRIBUNAL DE CONCILIACION Y ARBITRAJE", "Tribunal de Conciliación y Arbitraje"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "autoridades"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column(Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    distrito = relationship("Distrito", back_populates="autoridades")
    materia_id = Column(Integer, ForeignKey("materias.id"), index=True, nullable=False)
    materia = relationship("Materia", back_populates="autoridades")

    # Columnas
    descripcion = Column(String(256), nullable=False)
    descripcion_corta = Column(String(64), nullable=False, default="")
    clave = Column(String(16), nullable=False, unique=True)
    es_jurisdiccional = Column(Boolean(), nullable=False, default=False)
    es_notaria = Column(Boolean(), nullable=False, default=False)
    organo_jurisdiccional = Column(
        Enum(*ORGANOS_JURISDICCIONALES, name="tipos_organos_jurisdiccionales", native_enum=False),
        index=True,
        nullable=False,
    )

    # Hijos
    edictos = relationship("Edicto", back_populates="autoridad", lazy="noload")
    glosas = relationship("Glosa", back_populates="autoridad", lazy="noload")
    listas_de_acuerdos = relationship("ListaDeAcuerdo", back_populates="autoridad", lazy="noload")
    sentencias = relationship("Sentencia", back_populates="autoridad", lazy="noload")
    ubicaciones_expedientes = relationship("UbicacionExpediente", back_populates="autoridad", lazy="noload")
