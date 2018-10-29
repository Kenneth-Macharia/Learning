''' This module contains the users resources '''

import sqlite3
from flask_restful import Resource, reqparse
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

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        add_user_query = "INSERT INTO users_table VALUES (NULL, ?, ?)"
        cursor.execute(add_user_query, (req_data['username'], req_data['password']))

        connection.commit()
        connection.close()

        return {'Response':'User created'}, 201
