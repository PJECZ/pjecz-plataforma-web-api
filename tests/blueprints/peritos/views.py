"""
Peritos
"""
from flask import Blueprint, render_template

peritos = Blueprint("peritos", __name__, template_folder="templates")


@peritos.route("/peritos")
def list_public():
    """Datatable de peritos"""
    return render_template("peritos/list.jinja2")
