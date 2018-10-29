''' This module contains helper model for interacting with items '''

import sqlite3
from sqlalchemy import db


class ItemModel(db.Model):
    #Tell sqlalchemy where the models will be stored i.e. table & columns
    __tablename__ =  'items_table'

    id = db.Colunm(db.Integer, primary_key=True)
    name = db.Column(db.String(80))  #Character length
    price = db.Column(db.Float(precision=2))  #Decimal number to two decimal places

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def json(self):
        return {'name':self.name, 'price':self.price}  #returns a json rep of the model i.e items

    @classmethod
    def find_item_by_name(cls, name):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        get_item_query = "SELECT * FROM items_table WHERE name=?"
        result = cursor.execute(get_item_query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            #return cls(row[0], row[1])  #return an ItemModel object representing the row returned.
            return cls(*row)  #{arg unpacking} returns the object elements in their order as per the __init__

    def insert_item(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        insert_item_query = "INSERT INTO items_table VALUES (?, ?)"
        cursor.execute(insert_item_query, (self.name, self.price))

        connection.commit()
        connection.close()

    def update_item(self):
        connection = sqlite3.connect('test.db')
        cursor = connection.cursor()

        edit_item_query = "UPDATE items_table SET price=? WHERE name=?"
        cursor.execute(edit_item_query, (self.price, self.name))

        connection.commit()
        connection.close()
