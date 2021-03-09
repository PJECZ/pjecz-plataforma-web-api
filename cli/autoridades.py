"""
Autoridades
"""
import click

from cli.config import pass_config
from api.autoridades.crud import get_autoridades


@click.group()
@pass_config
def cli(config):
    """ Autoridades """


@cli.command()
@pass_config
def listar(config):
    """ Listado de Autoridades """
    consulta = get_autoridades(config.db)
    for distrito, autoridad in consulta:
        click.echo(f"{distrito.nombre}, {autoridad.descripcion}")
    click.echo(f"{len(consulta)} autoridades consultadas.")


cli.add_command(listar)
