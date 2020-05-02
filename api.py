from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class customRouteFuntionality(Resource):
    def get(self, var):
        print(f'[GET] Recieved var {var}. Do custom stuff here!')
        return {
            'recieved': True,
        }


api.add_resource(customRouteFuntionality, '/customRoute/<string:var>')

if __name__ == '__main__':
    app.run(debug=True)
