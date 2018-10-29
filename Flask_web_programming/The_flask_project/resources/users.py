''' This module contains the users resources '''

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.user import UserModel

''' Class for registering users into the DB '''
class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Cant be left blank!')
    parser.add_argument('password', type=str, required=True, help='Cant be left blank!')

    def post(self):
        req_data = UserRegistration.parser.parse_args()

        if UserModel.find_by_username(req_data['username']):
            return {'Response':'User already exists'}, 400

        new_user = UserModel(**req_data) #kwargs
        new_user.save_user()

        return {'Response':'User created'}, 201

''' Class for checking registered users '''
class UserCheck(Resource):

    @jwt_required()
    def get(self, name):
        if UserModel.find_by_username(name):
            return {'Response':'User {} is registered'.format(name)}, 200
        return {'Response':'User {} does not exist'.format(name)}, 404
