"""
Autoridades, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from sqlalchemy.orm import Session
from api.autoridades.models import Autoridad
from api.distritos.models import Distrito


def get_autoridades(db: Session, distrito_id: int = None):
    """ Consultar autoridades """
    consulta = db.query(Autoridad, Distrito).filter(Autoridad.distrito_id == Distrito.id).all()
    return consulta
    #
    # consulta = db.query(Autoridad).join(Autoridad.distrito).all()
    # return consulta
    #
    # consulta = db.query(Autoridad.id, Autoridad.distrito_id, Distrito.nombre, Autoridad.descripcion).join(Distrito)
    # consulta = consulta.with_entities()
    # consulta = consulta.filter(Autoridad.distrito_id == Distrito.id)
    # if distrito_id:
    #     consulta = consulta.filter(Autoridad.distrito_id == distrito_id)
    # return consulta.filter(Autoridad.estatus == "A").order_by(Distrito.nombre, Autoridad.descripcion).all()


def get_autoridad(db: Session, autoridad_id: int):
    """ Consultar una autoridad """
    return db.query(Autoridad).get(autoridad_id)


def get_autoridad_with_email(db: Session, email: str):
    """ Consultar una autoridad con su e-mail """
    return db.query(Autoridad).filter(Autoridad.email == email).first()
