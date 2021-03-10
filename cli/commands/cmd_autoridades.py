"""
Autoridades, click group
"""
import click
from tabulate import tabulate

from cli.cli import pass_config
from api.autoridades.crud import get_autoridades


@click.group()
def cli():
    """ Autoridades """


@click.command()
@pass_config
def listar(config):
    """ Listado de Autoridades """
    consulta = get_autoridades(config.db)
    tabla = []
    for autoridad, distrito in consulta:
        tabla.append([autoridad.id, distrito.nombre, autoridad.descripcion])
    click.echo(tabulate(tabla, headers=["id", "distrito", "autoridad"]))
    click.echo(f"{len(consulta)} autoridades consultadas.")


cli.add_command(listar)
