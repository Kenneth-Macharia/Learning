''' This module contains sample table creation and hard-coded data '''
import sqlite3

#create a connection & a cursor obj
connection = sqlite3.connect('test.db')
cursor = connection.cursor()

#create a table
create_table = "CREATE TABLE users_table (id int, username text, password text)"
cursor.execute(create_table)

#Insert a row
one_user = (1, 'Ken', 'asdfg')
insert_query = "INSERT INTO users_table VALUES (?, ?, ?)"
cursor.execute(insert_query, one_user)

#Insert mulitple rows
many_users = [
    (2, 'Rolf', 'ghjhk'),
    (3, 'Anna', 'uiopp')
]
cursor.executemany(insert_query, many_users)

#Retrieve data from database
select_query = "SELECT * FROM users_table"
for row in (cursor.execute(select_query)):
    print row

#Save changes to database & close connection
connection.commit()
connection.close()
