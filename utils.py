import sqlite3

def dbinsert(table, **kwargs):
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()
    columns = ', '.join(["'" + k + "'"  for k in kwargs.keys()])
    values = ', '.join(["'" + str(v) + "'" for v in kwargs.values()])
    cursor.execute(f'''
    INSERT INTO {table} ({columns}) VALUES
    ({values})
    ''')
    connection.commit()
    connection.close()

def dbselect(table, column):
    connection = sqlite3.connect('game.db')
    cursor = connection.cursor()
    cursor.execute(f'''
    SELECT {column}
    FROM {table}
    ''')
    result = cursor.fetchall()
    connection.commit()
    connection.close()
    return result


#dbinsert('Evil', id=4, name='Яга', hp=60, dmg=40)