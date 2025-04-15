from http import HTTPStatus

from flask import Blueprint, Response, request

from src import logic
from src.logic import PackageIn

blueprint = Blueprint("/package", __name__)


@blueprint.post("/")
def post() -> Response:
    package_in: PackageIn = request.get_json()
    logic.add_package_raw(package_in)

    return Response(status=HTTPStatus.ACCEPTED)
