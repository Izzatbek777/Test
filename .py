import sqlite3

conn = sqlite3.connect('medicc.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS medicc(id INT, name TEXT,bdate INT, price INT)''')
