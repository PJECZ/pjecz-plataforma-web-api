"""
REPSVM Agresores, modelos
"""
from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class REPSVMAgresor(Base, UniversalMixin):
    """REPSVMAgresor"""

    # Nombre de la tabla
    __tablename__ = 'repsvm_agresores'

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Claves foráneas
    distrito_id = Column(Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    distrito = relationship("Distrito", back_populates="repsvm_agresores")
    materia_tipo_juzgado_id = Column(Integer, ForeignKey("materias_tipos_juzgados.id"), index=True, nullable=False)
    materia_tipo_juzgado = relationship("MateriaTipoJuzgado", back_populates="repsvm_agresores")
    repsvm_delito_especifico_id = Column(Integer, ForeignKey("repsvm_delitos_especificos.id"), index=True, nullable=False)
    repsvm_delito_especifico = relationship("REPSVMDelitoEspecifico", back_populates="repsvm_agresores")
    repsvm_tipo_sentencia_id = Column(Integer, ForeignKey("repsvm_tipos_sentencias.id"), index=True, nullable=False)
    repsvm_tipo_sentencia = relationship("REPSVMTipoSentencia", back_populates="repsvm_agresores")

    # Columnas
    nombre = Column(String(256), nullable=False)
    numero_causa = Column(String(256), nullable=False)
    pena_impuesta = Column(String(256), nullable=False)
    observaciones = Column(Text(), nullable=True)
    sentencia_url = Column(String(512), nullable=False)
