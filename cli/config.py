"""
Config
"""
import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from instance.settings import SQLALCHEMY_DATABASE_URI
except ImportError:
    from config.settings import SQLALCHEMY_DATABASE_URI


class Config(object):
    """ Config """

    def __init__(self):
        """ Inicializar """
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = SessionLocal()


pass_config = click.make_pass_decorator(Config, ensure=True)
