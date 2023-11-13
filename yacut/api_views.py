from http import HTTPStatus
import re


from flask import (
    jsonify,
    request,
    Response,
    url_for,
)

from yacut import app, db
from yacut.exceptions import APIRequestError
from yacut.models import URLMap


@app.route('/api/id/', methods=('POST',))
def create_short_url() -> tuple[Response, int]:
    instance = validation(request.json)
    db.session.add(instance)
    db.session.commit()
    url = url_for('mapping_redirect', short=instance.short, _external=True)
    response = {
        'url': instance.original,
        'short_link': url,
    }
    return jsonify(response), HTTPStatus.CREATED.value


def validation(data) -> URLMap:
    if not data:
        raise APIRequestError('Отсутствует тело запроса')
    url = data.get('url')
    if not url:
        raise APIRequestError('"url" является обязательным полем!')
    custom_id = data.get('custom_id')
    if custom_id is not None:
        if (len(custom_id) > URLMap.SHORT_MAX_LENGTH or
                re.match(URLMap.SHORT_REGEX, custom_id) is None):
            raise APIRequestError('Указано недопустимое имя для короткой ссылки')
        if URLMap.short_exist(custom_id):
            raise APIRequestError(
                'Предложенный вариант короткой ссылки уже существует.')
    return URLMap(original=url, short=custom_id)


@app.route('/api/id/<string:short>/')
def get_short_url(short: str) -> tuple[Response, int]:
    instance = URLMap.query.filter_by(short=short).first()
    if not instance:
        raise APIRequestError('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': instance.original}), HTTPStatus.OK.value
