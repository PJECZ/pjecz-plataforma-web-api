"""
Autoridades
"""
import click

from cli.config import pass_config
from api.autoridades.crud import get_autoridades

from api.distritos.models import Distrito
from api.autoridades.models import Autoridad
from api.peritos.models import Perito
from api.listas_de_acuerdos.models import ListaDeAcuerdo
from api.ubicaciones_expedientes.models import UbicacionExpediente


@click.group()
@pass_config
def cli(config):
    """ Autoridades """


@cli.command()
@pass_config
def listar(config):
    """ Listado de Autoridades """
    autoridades = get_autoridades(config.db)
    for distrito, autoridad in autoridades:
        click.echo(f"{distrito.nombre}, {autoridad.descripcion}")
    click.echo(f"{len(autoridades)} autoridades consultadas.")


cli.add_command(listar)
