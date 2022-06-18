"""
Sentencias
"""
from flask import Blueprint, render_template

sentencias = Blueprint("sentencias", __name__, template_folder="templates")


@sentencias.route("/sentencias")
def list_public():
    """Datatable de sentencias"""
    return render_template("sentencias/list.jinja2")
