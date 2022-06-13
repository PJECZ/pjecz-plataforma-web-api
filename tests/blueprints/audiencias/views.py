"""
Audiencias
"""
from flask import Blueprint, render_template

audiencias = Blueprint("audiencias", __name__, template_folder="templates")


@audiencias.route("/audiencias")
def list_public():
    """Datatable de audiencias"""
    return render_template("audiencias/list.jinja2")
