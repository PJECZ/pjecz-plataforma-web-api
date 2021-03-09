"""
Distritos
"""
import click

from cli.config import pass_config
from api.distritos.crud import get_distritos

from api.distritos.models import Distrito
from api.autoridades.models import Autoridad
from api.peritos.models import Perito
from api.listas_de_acuerdos.models import ListaDeAcuerdo
from api.ubicaciones_expedientes.models import UbicacionExpediente


@click.group()
@pass_config
def cli(config):
    """ Distritos """


@cli.command()
@pass_config
def listar(config):
    """ Listado de Distritos """
    distritos = get_distritos(config.db)
    for distrito in distritos:
        click.echo(distrito.nombre)
    click.echo(f"{len(distritos)} distritos consultados.")


cli.add_command(listar)


if __name__ == "__main__":
    listar()
