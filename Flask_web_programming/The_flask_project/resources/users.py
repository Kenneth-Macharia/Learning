''' This module contains the users resources '''

import sqlite3
from flask_restful import Resource, reqparse


class User(object):
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        ''' class method for finding a user by username '''

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_user_query = "SELECT * FROM users_table WHERE username=?"
        query_result = cursor.execute(get_user_query, (username,))
        row = query_result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        ''' class method for finding a user by id '''

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_user_query = "SELECT * FROM users_table WHERE id=?"
        query_result = cursor.execute(get_user_query, (_id,))
        row = query_result.fetchone()

        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user


''' Class for registering users into the DB '''
class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Cant be left blank!')
    parser.add_argument('password', type=str, required=True, help='Cant be left blank!')

    def post(self):
        req_data = UserRegistration.parser.parse_args()

        if User.find_by_username(req_data['username']):
            return {'Response':'User already exists'}, 400

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        add_user_query = "INSERT INTO users_table VALUES (NULL, ?, ?)"
        cursor.execute(add_user_query, (req_data['username'], req_data['password']))

        connection.commit()
        connection.close()

        return {'Response':'User created'}, 201
