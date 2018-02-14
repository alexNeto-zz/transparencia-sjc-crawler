from flask import Flask
from flask_restful import Resource, Api

from headers import *

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)
