''' This module contains code & tutorial notes for the creation of a CRUD RESTful_api
    i.e Create, Read, Update, Delete '''

''' Run different python versions i.e. 2.7 > python or python2.7 or 3.5 > python3.5 '''
''' Use pip the same way, pip for python 2.7 or pip3.5 for python3.5 '''
''' Install desired python version in virtual env > virtualenv <env> --python=python<version> '''
''' Using virtual environments you can run python version & other package versions desired '''
''' Run atom and open desired folder: $atom <folder>/ '''

''' Run sample_sqlite_db.py to set up the databse for this api '''

from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required #a decorator to decorate endpoints requiring authentication
from users import authenticate, identity

''' Resources are things the api is concerned with e.g, items, students etc '''

app = Flask(__name__)
app.secret_key = 'myveryfirstjwtsecuredapi'
api = Api(app)  #Allows us to add resources to our app in the form of classes


#First Flask_Restful app
class Student(Resource):
    def get(self, name):
        return {'student':name}

api.add_resource(Student, '/student/<string:name>')


''' Test-first design - involves thinking about what you want to achieve and set up a blueprint before implementing
    the solution '''
''' In postman (Section 4 collection), the various endpoint have been defined, to aid coding their implemtations below '''
''' Flask_Restful jsonify's dicts for us, so no need to use the class Jsonify '''
''' Return the approriate status code for each operation '''

#Online RESTful api with auth & arguments parsing.
items = []

jwt = JWT(app, authenticate, identity)

''' JWT creates a new endpoint '/auth'. We collect a username & password via the endpoint
    and pass it to our authenticate method to establish if the user exists. if a user matches
    they become the identity and is returned. The '/auth then returns a JW token fr the user
    returned. The token is then used henceforth by every request done. For each of these
    requests, JWT then requires we send the token generated for the user then uses the identity
    function to get the userid and the correct user for the userid represnted by the token '''

''' Using authentication for the endoipoints:
        1. Generate a token for a user using the '/auth endpoint
        2. Supply a username & password in the auth POST request body & copy returned token, without quotes.
        3. In the request, create an 'authorization' header, in the value enter: 'JWT <the_token>
        4. Send the request '''


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help='This field cant be left blank!')

    @jwt_required()
    def get(self, name):
        #item = next(filter(lambda item: item['name'] == name, items))  #another option
        item_retrieved = list(filter(lambda item: item['name'] == name, items))
        if item_retrieved:
            return {'Response':item_retrieved}, 200
        return {'Response':'Item {} does not exist'.format(name)}, 400  # not found

    @jwt_required()
    def post(self, name):
        if list(filter(lambda item: item['name'] == name, items)):
            return {'Response':'Item {} already exists'.format(name)}, 400  # bad request

        data = Item.parser.parse_args()
        item = {'name':name, 'price':data['price']}
        items.append(item)
        return {'Item created':item}, 201  #resource created

    @jwt_required()
    def delete(self, name):
        global items
        if not list(filter(lambda item: item['name'] == name, items)):
            return {'Response':'Item {} does not exist'.format(name)}, 400

        items = list(filter(lambda x: x['name'] != name, items))
        return {'Response':'Item deleted'}, 200

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = list(filter(lambda x: x['name'] == name, items))
        if item:
            item[0]['price'] = data['price']
            return {'Item updated':item[0]}, 200

        item = {'name':name, 'price':data['price']}
        items.append(item)
        return {'Item created':item}, 201


class Items(Resource):

    @jwt_required()
    def get(self):
        if not items:
            return {'Response':'No items to return'}, 404
        return {'Response':items}, 200


api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')

#Run the app
app.run(debug=True)
