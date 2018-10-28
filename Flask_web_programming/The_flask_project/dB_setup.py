''' This module sets up the sqlite database used for storage by the api '''

import sqlite3

connection = sqlite3.Connection('test.db')
cursor = connection.cursor()

#Create tables with auto incrementing IDs - specify INTEGER & PRIMARY KEY
create_table = "CREATE TABLE IF NOT EXISTS users_table (id INTEGER PRIMARY KEY, \
                username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items_table (name text, price real)"  #real is a decimal value
cursor.execute(create_table)

connection.commit()
connection.close()
