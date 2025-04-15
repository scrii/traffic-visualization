from http import HTTPStatus

from flask import Blueprint, Response

from . import package, packages

blueprint = Blueprint("/", __name__)
blueprint.register_blueprint(package.blueprint, url_prefix="/package")
blueprint.register_blueprint(packages.blueprint, url_prefix="/packages")


@blueprint.get("/health/")
def get_health() -> Response:
    return Response(status=HTTPStatus.OK)
