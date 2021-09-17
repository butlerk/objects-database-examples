import sqlite3
connection = sqlite3.connect('store.db')
cursor = connection.cursor()

cursor.execute('CREATE TABLE fruit (id INT PRIMARY KEY, name TEXT, price_cents INT)')
cursor.execute("INSERT INTO fruit VALUES (1,'apple',100)")
connection.commit()
connection.close()


