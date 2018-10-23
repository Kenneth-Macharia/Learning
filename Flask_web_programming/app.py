from flask import Flask, jsonify

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
''' JSON is a key-value pair (of the dict form) for sending data between application of a string type
    and uses double quotes (" ") not single quotes'''
''' jsonify is a Flask method for covnerting a python objects into json strings '''


''' A online store REST API '''

#Data storage
stores = [
    {
        'name':'store1',
        'items':[
            {
                'name':'some_item',
                'price':100.00
            },
            {
                'name':'other_item',
                'price':120.00
            }
        ]
    },
    {    'name':'store2',
        'items':[
            {
                'name':'an_item',
                'price':50.00
            }
        ]
    }
]

#GET /store -  Returns all stores
@app.route('/store', methods=['GET'])
def return_all_store():
    return jsonify({'Stores':stores})

#POST /store {POST data:store name} - Adds a store
@app.route('/store', methods=['POST'])
def create_store():
    pass

#GET /store/<string:name> - Returns a specific store
@app.route('/store/<string:name>', methods=['GET'])
def return_a_store(name):
    pass

#POST /store/<string:name>/item {POST data:item name & price}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_store_item(name):
    pass

#GET /store/store/<string:name>/item - Returns all items in a store
@app.route('/store/<string:name>/item', methods=['GET'])
def return_store_items(name):
    pass



#Run the app
app.run(port=3000)
