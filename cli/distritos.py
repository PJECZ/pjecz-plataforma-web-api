"""
Distritos
"""
import click

from cli.config import pass_config
from api.distritos.crud import get_distritos


@click.group()
@pass_config
def cli(config):
    """ Distritos """


@cli.command()
@pass_config
def listar(config):
    """ Listado de Distritos """
    consulta = get_distritos(config.db)
    for distrito in consulta:
        click.echo(distrito.nombre)
    click.echo(f"{len(consulta)} distritos consultados.")


cli.add_command(listar)
