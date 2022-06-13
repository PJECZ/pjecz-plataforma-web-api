"""
Abogados
"""
from flask import Blueprint, render_template

abogados = Blueprint("abogados", __name__, template_folder="templates")


@abogados.route("/abogados")
def list_public():
    """Datatable de abogados"""
    return render_template("abogados/list.jinja2")
