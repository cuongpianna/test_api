"""
Extensions setup
================
Extensions provide access to common resources of the application.
Please, put new extension instantiations and initializations here.
"""

from flask_restful_swagger import swagger
from flask_restful import Api
api = swagger.docs(Api())

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


def init_app(app):
    """
    Application extensions initialization.
    :param app:
    """
    for extension in (
            api,
            db
    ):
        extension.init_app(app)
