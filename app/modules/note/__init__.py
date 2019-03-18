from app.extensions import api


def init_app(app, **kwargs):
    from app.modules.note.resouces import NoteListResource, NoteResource

    api.add_resource(NoteListResource, '/notes/')
    api.add_resource(NoteResource, '/notes/<string:id>/')
    # api.init_app(app)
