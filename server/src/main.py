from flask import Flask
from flask_cors import CORS

from . import routes


def main() -> Flask:
    app = Flask(__name__)
    app.register_blueprint(routes.blueprint)
    CORS(app)
    return app
