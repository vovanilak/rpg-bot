import sqlite3

connection = sqlite3.connect('game.db')
cursor = connection.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
chatid INTEGER PRIMARY KEY,
userid INTEGER NOT NULL,
username TEXT
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Lives (
userid INTEGER PRIMARY KEY,
live INTEGER,
hp REAL,
dmg REAL,
lvl INTEGER,
xp INTEGER)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Hero (
userid INTEGER PRIMARY KEY,
name TEXT,
hp REAL,
dmg REAL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Fight (
id INTEGER PRIMARY KEY,
userid INTEGER,
evilid INTEGER,
winner INTEGER
)
''')

connection.commit()
connection.close()