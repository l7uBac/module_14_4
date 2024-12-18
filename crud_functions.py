import sqlite3


connect = sqlite3.connect("products.db")
cursor = connect.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
        )
        ''')
    connect.commit()

def get_all_products():
    initiate_db()
    cursor.execute('SELECT * FROM Products')
    all_products = cursor.fetchall()
    connect.commit()
    return all_products



