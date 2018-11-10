from flask_restful import Resource
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):
    @jwt_required()
    def get(self, name):
        if StoreModel.find_store_by_name(name):
            return StoreModel.find_store_by_name(name).get_json_store()
        return {'Response':'Item {} does not exist'.format(name)}, 404

    @jwt_required()
    def post(self, name):
        if StoreModel.find_store_by_name(name):
            return {'Response':'Store {} already exists'.format(name)}, 400

        store = StoreModel(name)
        try:
            store.save_store()
        except:
            return {'Response':'An error occured while saving the store, \
                    please try again'}, 500

        return {'Response':'Store {} created'.format(name)}, 201

    @jwt_required()
    def delete(self, name):
        if StoreModel.find_store_by_name(name) is None:
            return {'Response':'Store {} does not exist'.format(name)}, 400

        StoreModel.find_store_by_name(name).delete_item()
        return {'Response':'Store {} deleted'.format(name)}, 200



class Stores(Resource):
    @jwt_required()
    def get(self):
        return {'All stores':[store.get_json_store() for store in \
                StoreModel.query.all()]}, 200 if StoreModel.query.all() else 404
