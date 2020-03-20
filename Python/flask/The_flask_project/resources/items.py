''' This module contains the items resources '''

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price', type=float, required=True, help='Price field required for all items!')
    parser.add_argument('store_id', type=int, required=True, help='Store ID required for all items!')

    @jwt_required()
    def get(self, name):
        if ItemModel.find_item_by_name(name):
            return ItemModel.find_item_by_name(name).get_json_item()
        return {'Response':'Item {} does not exist'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if ItemModel.find_item_by_name(name):
            return {'Response':'Item {} already exists'.format(name)}, 400

        response_data = Item.parser.parse_args()
        print (response_data['price'])
        print (response_data['store_id'])
        item_to_add = ItemModel(name, **response_data)  #kwargs {price & store_id}

        item_to_add.save_item()
        return {'Response':'Item {} created'.format(name)}, 201

    @jwt_required()
    def delete(self, name):
        if ItemModel.find_item_by_name(name) is None:
            return {'Response':'Item {} does not exist'.format(name)}, 400

        ItemModel.find_item_by_name(name).delete_item()
        return {'Response':'Item {} deleted'.format(name)}, 200

    @jwt_required()
    def put(self, name):
        response_data = Item.parser.parse_args()

        if ItemModel.find_item_by_name(name):
            if response_data['price']:
                ItemModel.find_item_by_name(name).price = response_data['price']
                ItemModel.find_item_by_name(name).save_item()
                return {'Response':'Price for item {} updated'.format(name)}, 200

            ItemModel.find_item_by_name(name).store_id = response_data['store_id']
            ItemModel.find_item_by_name(name).save_item()
            return {'Response':'Item {} store has been changed'.format(name)}, 200

        item_to_add = ItemModel(name, **response_data)  #kwargs {price & store_id}
        item_to_add.save_item()
        return {'Response':'Item {} created'.format(name)}, 201


class Items(Resource):
    @jwt_required()
    def get(self):
        ''' List comprehension option'''
        return {'All items':[item.get_json_item() for item in \
                ItemModel.query.all()]}, 200 if ItemModel.query.all() else 404

        ''' Lambda function option '''
        #return {'All database items':list(map(lambda x: x.get_json_item(), ItemModel.query.all()}, 200
