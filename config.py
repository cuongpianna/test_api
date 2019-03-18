import os


class BaseConfig:
    SECRET_KEY = 'porn'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # POSTGRESQL
    # DB_USER = 'user'
    # DB_PASSWORD = 'password'
    # DB_NAME = 'restplusdb'
    # DB_HOST = 'localhost'
    # DB_PORT = 5432
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
    #     user=DB_USER,
    #     password=DB_PASSWORD,
    #     host=DB_HOST,
    #     port=DB_PORT,
    #     name=DB_NAME,
    # )

    DEBUG = False

    ENABLED_MODULES = (
        'note',
        'hello',
    )

    AUTHORIZATIONS = {
        'oauth2_password': {
            'type': 'oauth2',
            'flow': 'password',
            'scopes': {},
            'tokenUrl': '/auth/oauth2/token',
        },
        # TODO: implement other grant types for third-party apps
        # 'oauth2_implicit': {
        #    'type': 'oauth2',
        #    'flow': 'implicit',
        #    'scopes': {},
        #    'authorizationUrl': '/auth/oauth2/authorize',
        # },
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    CSRF_ENABLED = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % (os.path.join(PROJECT_ROOT, "example.db"))


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    SECRET_KEY = 'jklasndlasjldjal'
