from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from yacut.settings import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
Migrate(app, db)

from yacut import (
    api_views,
    cli_commands,
    error_handlers,
    models,
    views
)
