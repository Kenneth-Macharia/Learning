''' This module contains code for the items models '''
''' It is responsible for saving and retireving items to and from the db '''

import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='This field cant be left blank!')

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_item_query = "SELECT * FROM items_table WHERE name=?"
        result = cursor.execute(get_item_query, (name,))
        row = result.fetchone()
        connection.close()

        return row

    @classmethod
    def insert_item(cls, item_to_insert):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        insert_item_query = "INSERT INTO items_table VALUES (?, ?)"
        cursor.execute(insert_item_query, (item_to_insert['name'], item_to_insert['price']))

        connection.commit()
        connection.close()

    @classmethod
    def update_item(cls, item_to_update):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        edit_item_query = "UPDATE items_table SET price=? WHERE name=?"
        cursor.execute(edit_item_query, (item_to_update['price'], item_to_update['name']))

        connection.commit()
        connection.close()


    @jwt_required()
    def get(self, name):
        row_returned = Item.find_item_by_name(name)
        if row_returned:
            return {'Response':{'name':row_returned[0], 'price':row_returned[1]}}, 200
        return {'Response':'Item {} does not exist'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if Item.find_item_by_name(name):
            return {'Response':'Item {} already exists'.format(name)}, 400

        response_data = Item.parser.parse_args()
        item_to_add = {'name':name, 'price':response_data['price']}

        Item.insert_item(item_to_add)
        return {'Response':'Item {} created'.format(name)}, 201

    @jwt_required()
    def delete(self, name):
        if Item.find_item_by_name(name) is None:
            return {'Response':'Item {} does not exist'.format(name)}, 400

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        delete_item_query = "DELETE FROM items_table WHERE name=?"
        cursor.execute(delete_item_query, (name,))

        connection.commit()
        connection.close()

        return {'Response':'Item {} deleted'.format(name)}, 200

    @jwt_required()
    def put(self, name):
        response_data = Item.parser.parse_args()
        item_to_add_or_update = {'name':name, 'price':response_data['price']}

        if Item.find_item_by_name(name):
            Item.update_item(item_to_add_or_update)
            return {'Response':'Item {} updated'.format(name)}, 200

        Item.insert_item(item_to_add_or_update)
        return {'Response':'Item {} created'.format(name)}, 201


class Items(Resource):
    @jwt_required()
    def get(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_all_query = "SELECT * FROM items_table"
        result = cursor.execute(get_all_query)

        items = []

        for row in result:
            items.append({'name':row[0], 'price':row[1]})

        connection.close()

        return {'All database items':items}, 200
