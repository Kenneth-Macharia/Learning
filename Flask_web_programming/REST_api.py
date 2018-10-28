''' This module contains code & tutorial notes for the creation of a REST_api '''
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

''' First flask app '''

# @app.route('/')
# def home():
#     return 'Hello world'


''' Web server is software designed to accept web requests '''
''' REST means a mindest of dealing with resources available on a web server e.g. /item, /items_lists '''
''' It also means that REST is stateles, i.e. requests are independent of each other and the web server does
    does not associate one with the other '''
''' In http://wwww.google.com/maps/:
    '/maps' is an endpoint that is supposed to do something e.g retrieve and respond back with a map page
    http://www.google.com is the host '''
''' Browsers do GET requests by default thus a route must specifiy what HTTP verb to use, and will default
    to GET if none is specified '''
''' JSON is a key-value pair (of the dict form) for sending data between application of string type
    and uses double quotes (" ") not single quotes'''
''' jsonify is a Flask method for converting a python objects into json strings '''


''' A online store REST API '''

#Data storage
stores = [
    {
        'name':'store1',
        'items':[
            {
                'name':'some_item',
                'price':100.00
            }
        ]
    }
]

#Home page endpoint that will be called via javascript in index.html
@app.route('/')
def home_page():
    return render_template('index.html')

#GET /store -  Returns all stores
@app.route('/store')
def return_all_store():
    return jsonify({'Response':stores})

#POST /store {POST data:store name} - Adds a store
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name':request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'Response':new_store})

#GET /store/<string:name> - Returns a specific store
@app.route('/store/<string:name>', methods=['GET'])
def return_a_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'Response':store})
    return jsonify({'Response':'Store not found'})

#POST /store/<string:name>/item {POST data:item name & price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_store_item = {
                'name':request_data['name'],
                'price':request_data['price']
            }
            store['items'].append(new_store_item)
            return jsonify({'Response':new_store_item})
        return jsonify({'Response':'Store not found'})

#GET /store/store/<string:name>/item - Returns all items in a store
@app.route('/store/<string:name>/item')
def return_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'Response':store['items']})
    return jsonify({'Response':'Store not found'})

#Run the app
''' Activate fenv in windows : fenv\Scripts\activate '''
''' Export the env variables manually in Windows:
        set FLASK_ENV='development'
        set FLASK_DEBUG=1 '''

app.run(port=3000)

''' Good json response format:
{
    'Description':'User friendly msg of what went wrong'
    'Error':'Name of error'
    'Status_code':401
} '''

''' Calling api endpoints from javascript important for flask web applications,
 not so important for api'''
''' Differences between web app and web api? '''
