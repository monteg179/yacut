from datetime import datetime
import re

from sqlalchemy.orm import validates

from yacut import db
from yacut.utils import random_custom_id


class URLMap(db.Model):

    SHORT_REGEX = r'^[a-zA-Z0-9]*$'
    SHORT_MAX_LENGTH = 16

    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(
        db.String(SHORT_MAX_LENGTH),
        nullable=False,
        unique=True,
        index=True,
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @validates('short')
    def validate_short(self, key, value):
        if not value:
            return type(self).random_short()
        if re.match(URLMap.SHORT_REGEX, value) is None:
            message = ('Идентификатор может состоять только '
                       'из латинских букв и цифр.')
            raise ValueError(message)
        return value

    @classmethod
    def short_exist(cls, value: str) -> bool:
        return cls.query.filter_by(short=value).count() > 0

    @classmethod
    def random_short(cls) -> str:
        while True:
            value = random_custom_id()
            if not cls.short_exist(value):
                break
        return value
