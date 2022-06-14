"""
Listas de Acuerdos
"""
from flask import Blueprint, render_template

listas_de_acuerdos = Blueprint("listas_de_acuerdos", __name__, template_folder="templates")


@listas_de_acuerdos.route("/listas_de_acuerdos")
def list_public():
    """Datatable de listas de acuerdos"""
    return render_template("listas_de_acuerdos/list.jinja2")
