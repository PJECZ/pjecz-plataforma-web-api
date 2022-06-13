"""
REDAMs
"""
from flask import Blueprint, render_template

redams = Blueprint("redams", __name__, template_folder="templates")


@redams.route("/redams")
def list_public():
    """Datatable de deudores"""
    return render_template("redams/list.jinja2")
