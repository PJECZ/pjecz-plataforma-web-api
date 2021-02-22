"""
Peritos, modelos
"""
from collections import OrderedDict
from sqlalchemy import Column, Enum, ForeignKey, Integer, String
from lib.database import Base
from lib.universal_mixin import UniversalMixin


class Perito(Base, UniversalMixin):
    """ Perito """

    TIPOS = OrderedDict(
        [
            ("ALBACEA", "Albacea"),
            ("AMBIENTAL", "Ambiental"),
            ("ARBITRO", "Árbitro"),
            ("ARBITRO VOLUNTARIO", "Árbitro Voluntario"),
            ("AUDITORIA INTERNA", "Auditoría Interna"),
            ("BALISTICA", "Balística"),
            ("CALIGRAFIA", "Caligrafía"),
            ("CONTABILIDAD", "Contabilidad"),
            ("CRIMINOLOGIA", "Criminología"),
            ("CRIMINALISTICA", "Criminalística"),
            ("DACTILOSCOPIA", "Dactiloscopía"),
            ("DEPOSITARIO", "Depositario"),
            ("DOCUMENTOSCOPIA", "Documentoscopía"),
            ("FOTOGRAFIA", "Fotografía"),
            ("FOTOGRAFIA FORENSE", "Fotografía Forence"),
            ("GASTROENTEROLOGIA", "Gastroenterología"),
            ("GENETICA", "Genética"),
            ("GENETICA HUMANA", "Genética Humana"),
            ("GRAFOLOGIA", "Grafología"),
            ("GRAFOSCOPIA", "Grafoscopía"),
            ("HECHOS DE TRANSITO", "Hechos de Tránsito"),
            ("HECHOS DE TRANSITO TERRESTRE", "Hechos de Tránsito Terrestre"),
            ("INCENDIOS Y EXPLOSIVOS", "Incendios y Explosivos"),
            ("INFORMATICA", "Informática"),
            ("INTERPRETE EN LENGUA DE SEÑAS MEXICANAS", "Intérprete en Lengua de Señas Mexicanas"),
            ("INTERVENTORES", "Interventores"),
            ("MEDICINA", "Medicina"),
            ("MEDICINA FORENSE", "Medicina Forense"),
            ("ODONTOLOGIA LEGAL Y FORENSE", "Odontología Legal y Forense"),
            ("POLIGRAFIA", "Poligrafía"),
            ("PSICOLOGIA", "Psicología"),
            ("QUIMICA", "Química"),
            ("TOPOGRAFIA", "Topografía"),
            ("TRADUCCION", "Traducción"),
            ("TRANSITO Y VIALIDAD TERRESTRE", "Tránsito y Vialidad Terrestre"),
            ("TUTORES", "Tutores"),
            ("VALUACION", "Valuación"),
            ("VALUACION INMOBILIARIA", "Valuación Inmobiliaria"),
            ("VALUACION VEHICULOS DAÑADOS", "Valuación Vehículos Dañados"),
            ("VALUACION AGROPECUARIA MAQUINARIA AGRICOLA Y EQUIPO INDUSTRIAL", "Valuación agropecuaria maquinaria agrícola y equipo industrial"),
        ]
    )

    # Nombre de la tabla
    __tablename__ = "peritos"

    # Clave primaria
    id = Column(Integer, primary_key=True)

    # Clave foránea
    distrito_id = Column("distrito", Integer, ForeignKey("distritos.id"), index=True, nullable=False)

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
