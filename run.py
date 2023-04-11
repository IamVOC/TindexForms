from flask import Flask, request, json
from flask_restful import Api, Resource, marshal_with
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from pymongo import MongoClient
from app.repository import MongoCollectionRepository
from app.schemas import FormObject, GetObject

app = Flask(__name__)
api = Api(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['test']
rep = MongoCollectionRepository(db, 'forms')

class MyAPI(MethodResource, Resource):

    @marshal_with(GetObject)
    def get(self):
        form = json.loads(request.data)
        note_id = form['note_id']
        col = rep.get(note_id)
        response = app.response_class(
            response=json.dumps(col),
            status=200,
            mimetype='application/json'
        )
        return response

    @marshal_with(FormObject)
    def post(self):
        form = json.loads(request.data)
        rep.add(form)
        return 'OK', 200 

api.add_resource(MyAPI, '/api/v1.0/')

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Awesome Project',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_UI_URL': '/api/v1.0/swagger'
})

docs = FlaskApiSpec(app)

docs.register(MyAPI)

if __name__ == '__main__':
    app.run(debug=True)
