"""
Distritos, click group
"""
import click
from tabulate import tabulate

from cli.cli import pass_config
from api.distritos.crud import get_distritos


@click.group()
def cli():
    """ Distritos """


@click.command()
@pass_config
def listar(config):
    """ Listado de Distritos """
    consulta = get_distritos(config.db)
    tabla = []
    for distrito in consulta:
        tabla.append([distrito.id, distrito.nombre])
    click.echo(tabulate(tabla, headers=["id", "distrito"]))
    click.echo(f"{len(consulta)} distritos consultados.")


cli.add_command(listar)
