''' Run different python versions i.e. 2.7 > python or python2.7 or 3.5 > python3.5 '''
''' Use pip the same way, pip for python 2.7 or pip3.5 for python3.5 '''
''' install desired python version in virtual env > virtual <env> --python=python<version> '''
''' Using virtual environments you can run python version & other package versions desired '''

from flask import Flask, request
from flask_restful import Resource, Api

''' Resources are things the api is concerned with e.g, items, students etc '''

#First Flask_Restful app
app = Flask(__name__)
api = Api(app)  #Allows us to add resources to our app in the form of classes

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
    def get(self, name):
        ''' implemtation options: '''
        ''' Filter will return a filter obj, based on the lambda return or
            Filter will return the list of items if the lambda function finds more than 1 matches '''

        #item = filter(lambda item: item['name'] == name, items)
        item_retrieved = list(filter(lambda item: item['name'] == name, items))
        return item_retrieved, 200 if item_retrieved else 404  #staus 'OK' else status 'not found'

    def post(self, name):
        if list(filter(lambda item: item['name'] == name, items)):
            return {'message':'Item {} already exists'.format(name)}, 400  #bad reuwest

        response = request.get_json()
        item = {'name':name, 'price':response['price']}
        items.append(item)
        return item, 201  #resource created

class Items(Resource):
    def get(self):
        if not items:
            return 'No items to return', 404
        return items, 200

api.add_resource(Item, '/item/<string:name>')
api.add_resource(Items, '/items')


#Run the app
app.run(port=3000, debug=True)
