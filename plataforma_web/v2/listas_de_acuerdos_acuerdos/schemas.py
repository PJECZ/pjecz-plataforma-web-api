"""
Listas de Acuerdos Acuerdos v2, esquemas de pydantic
"""
from datetime import date
from pydantic import BaseModel


class ListaDeAcuerdoAcuerdoOut(BaseModel):
    """Esquema para entregar acuerdos de una lista de acuerdos"""

    id: int
    fecha: date
    folio: str
    expediente: str
    actor: str
    demandado: str
    tipo_acuerdo: str
    tipo_juicio: str

    class Config:
        """SQLAlchemy config"""

        orm_mode = True
