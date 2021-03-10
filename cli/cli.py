"""
Plataforma Web API, comandos click
"""
import os
import click

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class Config(object):
    """ Configuración a pasar a comandos """

    def __init__(self):
        """ Inicializar la conexión a la base de datos """
        try:
            from instance.settings import SQLALCHEMY_DATABASE_URI
        except ImportError:
            from config.settings import SQLALCHEMY_DATABASE_URI
        engine = create_engine(SQLALCHEMY_DATABASE_URI)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.db = SessionLocal()


# Decorador para pasar la configuración
pass_config = click.make_pass_decorator(Config, ensure=True)

# Múltiples comandos en el directorio commands que empiezan con un prefijo
plugin_folder = os.path.join(os.path.dirname(__file__), "commands")
CMD_PREFIX = "cmd_"


class MyCLI(click.MultiCommand):
    """ Click de comandos múltiples """

    def list_commands(self, ctx):
        """ Cargar archivos py que empiezen por CMD_PREFIX """
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename.startswith(CMD_PREFIX):
                rv.append(filename[len(CMD_PREFIX) : -3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """ Obtener las instrucciones acumuladas en cli dentro de cada archivo """
        ns = {}
        fn = os.path.join(plugin_folder, CMD_PREFIX + name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


cli = MyCLI(help="Comandos para consola de Plataforma Web API")
