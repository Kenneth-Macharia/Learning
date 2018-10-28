''' This is the main module that runs the api resources & models '''
''' Its an improvement of REST_api_with_DB.py '''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import UserRegistration
from resources.items import Item, Items

app = Flask(__name__)
app.secret_key = 'myveryfirstjwtsecuredapiwihadb'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegistration, '/user_reg')

if __name__ == '__main__':
    app.run(debug=True)
