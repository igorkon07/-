import sqlite3

def initiate_db():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    price INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER
    )
    ''')
#    for i in range(1,5):
#        cursor.execute("INSERT INTO Products (title,description,price) VALUES (?,?,?)", (f"Продукт{i}", f"Описание{i}", i*100))
    connection.commit()
    connection.close()

def get_all_products():
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    all_products = cursor.fetchall()
    connection.close()
    return all_products

def add_user(username, email, age):
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO Users (username,email,age,balance) VALUES (?,?,?,?)", (username, email, age, 1000))
    connection.commit()
    connection.close()

def is_included(name):
    bol = True
    connection = sqlite3.connect('Products.db')
    cursor = connection.cursor()
    cout_user=cursor.execute(f"SELECT COUNT(*) FROM Users WHERE username = ?", (name,)).fetchone()
    if cout_user[0] == 0:
        bol = False
    connection.close()
    return bol

