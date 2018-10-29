''' This is the main module that runs the api resources & models '''
''' Its an improvement of REST_api_with_DB.py '''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.users import UserRegistration, UserCheck
from resources.items import Item, Items

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False #Turns off the flask_sqlalchemy obj tracker and leaves the sqlalchemy on
app.secret_key = 'myveryfirstjwtsecuredapiwihadb'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegistration, '/user_reg')
api.add_resource(UserCheck, '/user/<string:name>')

if __name__ == '__main__':
    from sqlalchemy_init import db_obj  #Import here to avoid circular imports
    db_obj.init_app(app)
    app.run(debug=True)
