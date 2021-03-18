"""
Abogados, click group
"""
import click
from tabulate import tabulate

from cli.cli import pass_config
from api.abogados.crud import get_abogados


@click.group()
def cli():
    """ Abogados """


@click.command()
@click.argument("nombre")
@pass_config
def listar(config, nombre):
    """ Listado de Abogados """
    consulta = get_abogados(config.db, nombre=nombre)
    tabla = []
    for abogado in consulta:
        tabla.append([abogado.id, abogado.fecha, abogado.libro, abogado.numero, abogado.nombre])
    click.echo(tabulate(tabla, headers=["id", "fecha", "libro", "numero", "abogado"]))
    click.echo(f"{len(consulta)} abogados encontrados con {nombre}.")


cli.add_command(listar)
