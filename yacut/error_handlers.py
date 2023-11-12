from http import HTTPStatus

from flask import Response, jsonify, render_template
from werkzeug.exceptions import HTTPException

from yacut import app, db
from yacut.exceptions import APIError


@app.errorhandler(APIError)
def invalid_api_usage(error: APIError) -> tuple[Response, int]:
    return jsonify(error.to_dict()), error.status.value


@app.errorhandler(404)
def page_not_found(error: HTTPException) -> tuple[str, int]:
    status = HTTPStatus.NOT_FOUND
    response = render_template('error.html', status=status)
    return response, status.value


@app.errorhandler(500)
def internal_error(error: HTTPException) -> tuple[str, int]:
    db.session.rollback()
    status = HTTPStatus.INTERNAL_SERVER_ERROR
    response = render_template('error.html', status=status)
    return response, status.value
