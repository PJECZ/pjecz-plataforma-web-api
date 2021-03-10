"""
Autoridades
"""
import click
from tabulate import tabulate

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
    """
        'descripcion', 'directorio_listas_de_acuerdos', 'directorio_sentencias', 'distrito', 'distrito_id', 'email', 'estatus', 'id', 'listas_de_acuerdos', 'metadata', 'ubicaciones_expedientes'
    """
    tabla = []
    for row in consulta:
        tabla.append([row.id, row.distrito.nombre, row.descripcion])
    click.echo(tabulate(tabla, headers=["id", "distrito", "autoridad"]))
    click.echo(f"{len(consulta)} autoridades consultadas.")


cli.add_command(listar)
