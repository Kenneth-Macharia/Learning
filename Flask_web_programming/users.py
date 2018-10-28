''' This module contains code & tutorial notes for searching & authenticating
    users for our RESTful_api '''
'''It has three models for achieving the above '''

import sqlite3
from flask_restful import Resource, reqparse
from werkzeug.security import safe_str_cmp #for safely comparing string in python 2x

''' Managing users via data structures '''
# users = [
#     {
#         'id':1,
#         'username':'bob',
#         'password':'asdf'
#     }
# ]
#
#These mappings ensure that we dont have to iterate through the users list
# username_mapping = {'bob':
#     {
#         'id':1,
#         'username':'bob',
#         'password':'asdf'
#     }
# }
#
# useid_mapping = {1:
#     {
#         'id':'bob',
#         'username':'bob',
#         'password':'asdf'
#     }
# }
#
# ''' Custom methos for checking if a user exists '''
# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     if user is not None and safe_str_cmp(user.password, password):
#         return user
#
# ''' Identity method is unique to JWT '''
# def identity(payload):    # payload is the contents of the JWT token
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)


''' Managing users via OOP only '''
# class User(object):
#     def __init__(self, _id, username, password):
#         self.id = _id
#         self.username = username
#         self.password = password
#
# users = [
#     User(1, 'bob', 'asdf')
# ]
#
# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}
#
# ''' Custom methos for checking if a user exists '''
# def authenticate(username, password):
#     user = username_mapping.get(username, None)
#     if user is not None and safe_str_cmp(user.password, password):
#         return user
#
# ''' Identity method is unique to JWT '''
# def identity(payload):    # payload is the contents of the JWT token
#     user_id = payload['identity']
#     return userid_mapping.get(user_id, None)


''' Managing users via OOP and a database (test.db)'''
class User_db(object):
    def __init__(self, _id, username, password):
        ''' Since no method is using 'self, then they can all be class methods '''

        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        ''' class method for finding a user by username '''

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_user_query = "SELECT * FROM users_table WHERE username=?" #getting every row matching our req.
        query_result = cursor.execute(get_user_query, (username,)) #sql parameter must be tuple
        row = query_result.fetchone() #if no match, none will be returned, else first row is returned

        if row:
            ''' Row values represented by each of the table columns,
            and matching __init__ paramenter, created as a class object '''

            #user = cls(row[0], row[1], row[2) #Above can be shortened to:
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

def authenticate(username, password):
    user = User_db.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return User_db.find_by_id(user_id)


''' Class for registering users into the DB '''
class UserRegistration(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='Cant be left blank!')
    parser.add_argument('password', type=str, required=True, help='Cant be left blank!')

    def post(self):
        req_data = UserRegistration.parser.parse_args()

        if User_db.find_by_username(req_data['username']):
            return {'Response':'User already exists'}, 400

        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        add_user_query = "INSERT INTO users_table VALUES (NULL, ?, ?)"
        cursor.execute(add_user_query, (req_data['username'], req_data['password']))

        connection.commit()
        connection.close()

        return {'Response':'User created'}, 201
