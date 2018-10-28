''' This module contains the exact code from RESTful_api.py '''
''' We will add persistent storage for this version of the app '''
''' We will use sql-lite as the RDB, which has bult in python support '''

''' Run create_test-db_tables.py first, to set up the database for this api '''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from users import authenticate, identity, UserRegistration
from items import Item, Items

app = Flask(__name__)
app.secret_key = 'myveryfirstjwtsecuredapiwihadb'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')
api.add_resource(UserRegistration, '/user_reg')

''' The file that we run i.e 'python <file>.py is always '__main__'. The current
    file is always __name__, thus we would want to run the app only if this
    file is __main__ '''
''' Thus if this file is being run but is not __main__, then it has been imported
    which means its not our intention to run the app, hence the below code '''
''' We can use control structures like these to choose want we want from a file
    on import '''

if __name__ == '__main__':
    app.run(debug=True)
