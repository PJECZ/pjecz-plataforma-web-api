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
@click.option("--distrito-id", type=int, default=None, help="Distrito ID")
@pass_config
def listar(config, distrito_id):
    """ Listar Autoridades """
    consulta = get_autoridades(config.db, distrito_id=distrito_id)
    tabla = []
    for autoridad, distrito in consulta:
        tabla.append([autoridad.id, distrito.nombre, autoridad.descripcion])
    click.echo(tabulate(tabla, headers=["id", "distrito", "autoridad"]))
    click.echo(f"{len(consulta)} autoridades consultadas.")


cli.add_command(listar)
