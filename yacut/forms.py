from flask_wtf import FlaskForm
from wtforms.fields import StringField
from wtforms.validators import (
    URL,
    DataRequired,
    Length,
    Regexp,
)
from yacut.models import URLMap


class URLMapForm(FlaskForm):

    original_link = StringField(
        label="Адрес URL",
        description='Длинная ссылка',
        validators=(
            DataRequired(message="Обязательное поле."),
            URL(message="Некорректный адрес URL."),
        ),
    )
    custom_id = StringField(
        label="Идентификатор ссылки",
        description='Ваш вариант короткой ссылки',
        validators=(
            Length(
                max=URLMap.SHORT_MAX_LENGTH,
                message="Длина поля не должна превышать 16 символов.",
            ),
            Regexp(
                regex=URLMap.SHORT_REGEX,
                message=(
                    "Идентификатор может состоять только "
                    "из латинских букв и цифр."
                ),
            ),
        ),
    )
