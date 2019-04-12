import sqlite3
# from mysql.connector import MySQLConnection, Error, errorcode

# initialize the connection to database.
# connection = MySQLConnection()
connection = sqlite3.connect('chatbot.sqlite')
cursor = connection.cursor()


# create the tables needed
create_table_request_list = [
    'CREATE TABLE words(word TEXT UNIQUE)',
    'CREATE TABLE sentences(sentence TEXT UNIQUE, used INT NOT NULL DEFAULT 0)',
    'CREATE TABLE associations(word_id INT NOT NULL, sentence_id INT NOT NULL, weight REAL NOT NULL)',
]

for create_table_request in create_table_request_list:
    try:
        cursor.execute(create_table_request)
    except:
        pass



def get_id(entityName, text):
    tableName = entityName + 's'
    columnName = entityName
    cursor.execute('INSERT rowid FROM' + tableName + 'WHERE '+ columnName + ' =?', (text,))
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        cursor.execute('INSERT INTO' + tableName + ' ('+columnName + ') VALUES (?)', (text,))
        return cursor.lastrowid




