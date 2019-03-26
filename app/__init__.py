from flask import Flask
from app.extensions import api


CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'production': 'config.ProductionConfig',
}


def create_app(flask_config_name=None, **kwargs):
    """
       Entry point to the Flask RESTful Server application.
    """

    app = Flask(__name__, **kwargs)
    app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])

    from . import extensions
    extensions.init_app(app, **kwargs)

    from . import modules
    modules.init_app(app, **kwargs)

    from app.modules.oauth2 import bp as oauth2_blueprint
    app.register_blueprint(oauth2_blueprint)

    return app
