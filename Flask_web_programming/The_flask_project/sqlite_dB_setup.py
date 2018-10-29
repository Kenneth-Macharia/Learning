''' This module sets up the sqlite database used for storage by the api '''

import sqlite3

connection = sqlite3.Connection('test.db')
cursor = connection.cursor()

#Create tables with auto incrementing IDs - specify INTEGER & PRIMARY KEY
create_table_users = "CREATE TABLE IF NOT EXISTS users_table (id INTEGER PRIMARY KEY, \
                username text, password text)"
cursor.execute(create_table_users)

create_table_items = "CREATE TABLE IF NOT EXISTS items_table (id INTEGER PRIMARY KEY, \
                name text, price real)"  #real is a decimal value
cursor.execute(create_table_items)

connection.commit()
connection.close()
