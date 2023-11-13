import os


class Config:
    SECRET_KEY = os.getenv(
        key='SECRET_KEY',
        default='drxyjcnmgf[ytnytanm.'
    )
    SQLALCHEMY_DATABASE_URI = os.getenv(
        key='DATABASE_URI',
        default='sqlite:///db.sqlite3'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_AS_ASCII = False
