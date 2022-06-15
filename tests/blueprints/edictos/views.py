"""
Edictos
"""
from flask import Blueprint, render_template

edictos = Blueprint("edictos", __name__, template_folder="templates")


@edictos.route("/edictos")
def list_public():
    """Datatable de edictos"""
    return render_template("edictos/list.jinja2")
