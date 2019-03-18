from flask_restful import Resource
from app.extensions import swagger


@swagger.model
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
