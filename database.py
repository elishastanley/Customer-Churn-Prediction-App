import sqlite3

def get_connection(path=':memory:'):
    return sqlite3.connect(path)

def get_data(query, params=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        return cursor.fetchall()
