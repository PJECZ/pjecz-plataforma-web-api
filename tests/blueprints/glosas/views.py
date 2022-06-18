"""
Glosas
"""
from flask import Blueprint, render_template

glosas = Blueprint("glosas", __name__, template_folder="templates")


@glosas.route("/glosas")
def list_public():
    """Datatable de glosas"""
    return render_template("glosas/list.jinja2")
