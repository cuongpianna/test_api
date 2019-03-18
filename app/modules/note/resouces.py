from datetime import datetime

from flask_restful import Resource, reqparse, fields, marshal_with, abort

from app.extensions import db, swagger
from app.modules.note.models import Note


note_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'create_at': fields.String,
}

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')
parser.add_argument('create_at')


@swagger.model
class NoteResourceFields:
    resource_fields = {
        'id': fields.Integer,
        'title': fields.String,
        'description': fields.String,
        'create_at': fields.String,
    }


class NoteResource(Resource):
    @marshal_with(NoteResourceFields.resource_fields)
    def get(self, id):
        note = Note.query.get(id)
        if not note:
            abort(404, message="Note {} doesn't exist".format(id))
        return note

    def delete(self, id):
        note = Note.query.get(id)
        if not note:
            abort(404, message="Note {} doesn't exist".format(id))
        db.session.delete(note)
        db.session.commit()
        return 'delete', 204


class NoteListResource(Resource):
    @marshal_with(NoteResourceFields.resource_fields)
    def get(self):
        notes = Note.query.all()
        return notes

    @marshal_with(NoteResourceFields.resource_fields)
    def post(self):
        parses_arg = parser.parse_args()
        print(parses_arg)
        note = Note(
            title=parses_arg['title'],
            description=parses_arg['description'],
            create_at=parses_arg['create_at']
        )
        db.session.add(note)
        db.session.commit()
        return note, 201

