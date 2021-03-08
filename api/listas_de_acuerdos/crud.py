"""
Listas de Acuerdos, CRUD: the four basic operations (create, read, update, and delete) of data storage
"""
from datetime import datetime
from sqlalchemy.orm import Session
from api.autoridades.crud import get_autoridad_with_email
from api.listas_de_acuerdos import models, schemas


def get_listas_de_acuerdos(db: Session, autoridad_id: int = None):
    """ Consultar listas de acuerdos """
    listas_de_acuerdos = db.query(models.ListaDeAcuerdo)
    if autoridad_id:
        listas_de_acuerdos = listas_de_acuerdos.filter(models.ListaDeAcuerdo.autoridad_id == autoridad_id)
    return listas_de_acuerdos.filter(models.ListaDeAcuerdo.estatus == "A").order_by(models.ListaDeAcuerdo.fecha.desc()).limit(100).all()


def get_lista_de_acuerdo(db: Session, lista_de_acuerdo_id: int):
    """ Consultar una lista de acuerdos """
    return db.query(models.ListaDeAcuerdo).get(lista_de_acuerdo_id)


def new_lista_de_acuerdo(db: Session, recibido: schemas.ListaDeAcuerdoNew):
    """ Nueva lista de acuerdos """
    # Validar autoridad_email
    autoridad = get_autoridad_with_email(recibido.autoridad_email)
    if autoridad is False:
        return False
    # Validar fecha
    hoy = datetime.date.today()
    pasado = hoy - datetime.timedelta(days=3)
    if recibido.fecha > hoy or recibido.fecha < pasado:
        return False
    fecha = recibido.fecha
    # Validar archivo
    archivo = recibido.archivo
    # Validar descripcion
    if recibido.descripcion.strip() == "":
        descripcion = "Lista de acuerdos"
    else:
        descripcion = recibido.descripcion.strip().title()
    # Validar URL
    if recibido.url.strip() == "":
        url = "https://storage.google.com/DEPOSITO/Listas de Acuerdos/DISTRITO/AUTORIDAD/YYYY/MM/"
    else:
        url = recibido.url
    # Revisar si existe
    lista_de_acuerdo = db.query(models.ListaDeAcuerdo).filter(models.ListaDeAcuerdo.autoridad == autoridad).filter(models.ListaDeAcuerdo.fecha == fecha).first()
    if lista_de_acuerdo:
        # Actualizar
        lista_de_acuerdo.archivo = archivo
        lista_de_acuerdo.descripcion = descripcion
        lista_de_acuerdo.url = url
    else:
        # Insertar
        lista_de_acuerdo = models.ListaDeAcuerdo(
            autoridad=autoridad,
            fecha=fecha,
            descripcion=descripcion,
            url=url,
        )
    # Operar
    db.add(lista_de_acuerdo)
    db.commit()
    db.refresh(lista_de_acuerdo)
    return lista_de_acuerdo
