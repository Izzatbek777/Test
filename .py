import sqlite3

conn = sqlite3.connect('medicc.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS medicc(id INT, name TEXT,bdate INT, price INT)''')

conn = sqlite3.connect('medicc.db')
cursor = conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS medicc(id INT, name TEXT,bdate INT, price INT)''')
cursor.execute('''INSERT INTO medicc(id,  name, bdate, price) VALUES  (2, 'sitromon', '6 month', '12000')''')
cursor.execute('''INSERT INTO medicc(id,  name, bdate, price) VALUES  (6, 'tirmol', '2 years', '8000')''')
cursor.execute('''INSERT INTO medicc(id,  name, bdate, price) VALUES  (4, 'livomikol', '8 month', '2000')''')


conn.commit()
