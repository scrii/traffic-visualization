import flask
from flask import Blueprint, Response

from src import logic

blueprint = Blueprint("/packages", __name__)


@blueprint.get("/")
def get() -> Response:
    return flask.jsonify(logic.get_packages())
