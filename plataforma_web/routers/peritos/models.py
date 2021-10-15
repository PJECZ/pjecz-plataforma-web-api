"""
Peritos, modelos
"""
from collections import OrderedDict
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Perito(Base, UniversalMixin):
    """Perito"""

    TIPOS = OrderedDict(
        [
            ("ACCIDENTES DE TRABAJO", "Accidentes de Trabajo"),
            ("ALBACEA", "Albacea"),
            ("AMBIENTAL", "Ambiental"),
            ("ARBITRO", "Árbitro"),
            ("AREA DE RECONOCIMIENTO DE VOZ Y CONTROL DE RUIDO", "Área de reconocimiento de voz y control de ruido"),
            ("ARQUITECTURA", "Arquitectura"),
            ("AUDITORIA INTERNA", "Auditoría Interna"),
            ("BALISTICA", "Balística"),
            ("CALIGRAFIA", "Caligrafía"),
            ("CATASTRO", "Catastro"),
            ("CONTABILIDAD", "Contabilidad"),
            ("CONSTRUCCION", "Construcción"),
            ("CRIMINALISTICA", "Criminalística"),
            ("DACTILOSCOPIA", "Dactiloscopía"),
            ("DEPOSITARIO", "Depositario"),
            ("DOCUMENTOSCOPIA", "Documentoscopía"),
            ("FOTOGRAFIA", "Fotografía"),
            ("FOTOGRAFIA FORENSE", "Fotografía Forence"),
            ("GASTROENTEROLOGIA", "Gastroenterología"),
            ("GENETICA", "Genética"),
            ("GRAFOLOGIA", "Grafología"),
            ("GRAFOSCOPIA", "Grafoscopía"),
            ("INCENDIOS Y EXPLOSIVOS", "Incendios y Explosivos"),
            ("INGENIERIA CIVIL", "Ingeniería Civil"),
            ("INFORMATICA", "Informática"),
            ("INTERPRETE EN LENGUA DE SEÑAS MEXICANAS", "Intérprete en Lengua de Señas Mexicanas"),
            ("INTERVENTORES", "Interventores"),
            ("MEDICINA", "Medicina"),
            ("MEDICINA FORENSE", "Medicina Forense"),
            ("MEDIO AMBIENTE LABORAL", "Medio Ambiente Laboral"),
            ("ODONTOLOGIA LEGAL Y FORENSE", "Odontología Legal y Forense"),
            ("PARTIDOR", "Partidor"),
            ("POLIGRAFIA", "Poligrafía"),
            ("PSICOLOGIA", "Psicología"),
            ("PSICOANALISIS", "Psicoanálisis"),
            ("PSICOTERAPIA FAMILIAR", "Psicoterapia Familiar"),
            ("QUIMICA", "Química"),
            ("TOPOGRAFIA", "Topografía"),
            ("TRADUCCION", "Traducción"),
            ("TRANSITO Y VIALIDAD TERRESTRE", "Tránsito y Vialidad Terrestre"),
            ("TUTORES", "Tutores"),
            ("VALUACION", "Valuación"),
            ("VALUACION INMOBILIARIA", "Valuación Inmobiliaria"),
            ("VALUACION VEHICULOS DAÑADOS", "Valuación de Vehículos Dañados"),
            ("VALUACION AGROPECUARIA MAQUINARIA AGRICOLA Y EQUIPO INDUSTRIAL", "Valuación agropecuaria maquinaria agrícola y equipo industrial"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "peritos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column(Integer, ForeignKey("distritos.id"), index=True, nullable=False)
    distrito = relationship("Distrito", back_populates="peritos")

    # Columnas
    tipo = Column(
        Enum(*TIPOS, name="tipos_peritos", native_enum=False),
        index=True,
        nullable=False,
    )
    nombre = Column(String(256), nullable=False)
    domicilio = Column(String(256), nullable=False)
    telefono_fijo = Column(String(64))
    telefono_celular = Column(String(64))
    email = Column(String(256))
    notas = Column(String(256))
