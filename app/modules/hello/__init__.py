from app.extensions import api


def init_app(app, **kwargs):
    from app.modules.hello.resources import HelloWorld

    api.add_resource(HelloWorld, '/')
    api.init_app(app)
