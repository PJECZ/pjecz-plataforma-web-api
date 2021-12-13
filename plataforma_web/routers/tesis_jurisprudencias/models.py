"""
Tesis Jurisprudencias, modelos
"""
from collections import OrderedDict

from sqlalchemy import Column, Date, DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship

from lib.database import Base
from lib.universal_mixin import UniversalMixin


class TesisJurisprudencia(Base, UniversalMixin):
    """TesisJurisprudencia"""

    TIPOS = OrderedDict(
        [
            ("POR CONTRADICCION", "Por contradicción"),
            ("REITERACION", "reiteración"),
            ("REVALIDACION", "revalidación"),
            ("DECLARACION", "declaración"),
        ]
    )

    ESTADOS = OrderedDict(
        [
            ("INTERRUMPIR", "Interrumpir"),
            ("MODIFICAR", "Modificar"),
        ]
    )

    CLASES = OrderedDict(
        [
            ("TESIS", "Tesis"),
            ("JURISPRUDENCIA", "Jurisprudencia"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = 'tesis_jurisprudencias'

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea Órgano jurisdiccional
    autoridad_id = Column(Integer, ForeignKey("autoridades.id"), index=True, nullable=False)
    autoridad = relationship("Autoridad", back_populates="tesis_jurisprudencias")

    # Clave foránea Época
    epoca_id = Column(Integer, ForeignKey("epocas.id"), index=True, nullable=False)
    epoca = relationship("Epoca", back_populates="tesis_jurisprudencias")

    # Clave foránea Materia
    materia_id = Column(Integer, ForeignKey("materias.id"), index=True, nullable=False)
    materia = relationship("Materia", back_populates="tesis_jurisprudencias")

    # Columnas
    titulo = Column(String(256), nullable=False)
    subtitulo = Column(String(256), nullable=False)
    tipo = Column(Enum(*TIPOS, name="tipos", native_enum=False), index=True, nullable=False)
    estado = Column(Enum(*ESTADOS, name="estados", native_enum=False), index=True, nullable=False)
    clave_control = Column(String(24), nullable=False)
    clase = Column(Enum(*CLASES, name="clases", native_enum=False), index=True, nullable=False)
    rubro = Column(String(256), nullable=False)
    texto = Column(Text(), nullable=False)
    precedentes = Column(Text(), nullable=False)
    votacion = Column(String(256), nullable=False)
    votos_particulares = Column(String(256), nullable=False)
    aprobacion_fecha = Column(Date(), nullable=False)
    publicacion_tiempo = Column(DateTime(), nullable=False)
    aplicacion_tiempo = Column(DateTime(), nullable=False)

    # Hijos de funcionarios
    #tesis_jurisprudencias_funcionarios = relationship('TesisJurisprudenciaFuncionario', back_populates='tesis_jurisprudencias')

    # Hijos a Sentencias
    #tesis_jurisprudencias_sentencias = relationship('TesisJurisprudenciaSentencia', back_populates='tesis_jurisprudencia')

    @property
    def numero_registro_digital(self):
        """Número de registro digital (Número único por registro)"""
        return self.id
