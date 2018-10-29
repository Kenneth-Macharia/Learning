''' This module contains helper model for finding & retrieving user '''

import sqlite3
from sqlalchemy import db  #import the sqlalchemy object

class UserModel(db.Model):  #Extend the sqlalchemy object
    #Tell sqlalchemy where the models will be stored i.e. table & columns
    __tablename__ =  'users_table'

    id = db.Colunm(db.Integer, primary_key=True)
    username = db.Column(db.String(80))  #Character length
    password = db.Column(db.String(80))  #These must match the model item in __init__

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
