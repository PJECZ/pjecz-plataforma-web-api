"""
Tests v2 app.py
"""
from flask import Flask

from tests.blueprints.abogados.views import abogados
from tests.blueprints.audiencias.views import audiencias
from tests.blueprints.redams.views import redams
from tests.blueprints.sistemas.views import sistemas


def create_app():
    """Crear app"""
    app = Flask(__name__)
    app.register_blueprint(abogados)
    app.register_blueprint(audiencias)
    app.register_blueprint(redams)
    app.register_blueprint(sistemas)
    return app
