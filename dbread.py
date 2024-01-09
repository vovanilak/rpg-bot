import sqlite3

connection = sqlite3.connect('game.db')
cursor = connection.cursor()

cursor.execute('''
SELECT *
FROM Evil
''')
print(cursor.fetchall())
connection.commit()
connection.close()