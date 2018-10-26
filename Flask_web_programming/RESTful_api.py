''' Run different python versions i.e. 2.7 > python or python2.7 or 3.5 > python3.5 '''
''' Use pip the same way, pip for python 2.7 or pip3.5 for python3.5 '''
''' install desired python version in virtual env > virtual <env> --python=python<version> '''
''' Using virtual environments you can run python version & other package versions desired '''

from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required #a decorator to decorate endpoints requiring authentication
from security import authenticate, identity

''' Resources are things the api is concerned with e.g, items, students etc '''

#First Flask_Restful app
app = Flask(__name__)
app.secret_key = 'myveryfirstjwtsecuredapi'
api = Api(app)  #Allows us to add resources to our app in the form of classes

''' JWT creates a new endpoint '/auth'. We collect a username & password via the endpoint
    and pass it to our authenticate method to establish if the user exists. if a user matches
    they become the identity and is returned. The '/auth then returns a JW token fr the user
    returned. The token is then used henceforth by every request done. For each of these
    requests, JWT then requires we send the token generated for the user then uses the identity
    function to get the userid and the correct user for the userid represnted by the token '''

jwt = JWT(app, authenticate, identity)

class Student(Resource):
    def get(self, name):
        return {'student':name}

api.add_resource(Student, '/student/<string:name>')

''' Test-first design - involves thinking about what you want to achieve and set up a blueprint before implementing
    the solution '''
''' In postman (Section 4 collection), the various endpoint have been defined, to aid coding their implemtations below '''
''' Flask_Restful jsonify's dicts for us, so no need to use the class Jsonify '''
''' Return the approriate status code for each operation '''

#Online RESTful api
items = []

class Item(Resource):
    @jwt_required()
    def get(self, name):
        ''' Using authentication for this endoipoint:
                1. Generate a token for a user using the '/auth endpoint
                2. Supply a username & password in the auth POST request body & copy returned token, without quotes.
                3. In this GEt request, create an 'authorization' header, in the value enter: 'JWT <the_token>
                4.Send the GET request. '''

        ''' implemtation options: '''
        ''' Filter will return a filter obj, based on the lambda return or
            Filter will return the list of items if the lambda function finds more than 1 matches '''

        #item = filter(lambda item: item['name'] == name, items)
        item_retrieved = list(filter(lambda item: item['name'] == name, items))
        return {'Response':item_retrieved}, 200 if item_retrieved else 404  # not found

    def post(self, name):
        if list(filter(lambda item: item['name'] == name, items)):
            return {'Response':'Item {} already exists'.format(name)}, 400  # bad request

        response = request.get_json()
        item = {'name':name, 'price':response['price']}
        items.append(item)
        return {'Item created':item}, 201  #resource created

    def delete(self, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))
        return {'Response':'Item deleted'}, 200

    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name':name, 'price':response['price']}
            items.append(item)
            return {'Item created':item}, 201
        item.update(data) #Note, if 'data' has a 'name' as well it will be changed too
        return {'Item updated':item}, 200


class Items(Resource):
    def get(self):
        if not items:
            return {'Response':'No items to return'}, 404
        return {'Response':items}, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')


#Run the app
app.run(debug=True)
