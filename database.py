import sqlite3

def create_tables():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    cursor.execute('''
         CREATE TABLE IF NOT EXISTS Meals (
             id TEXT PRIMARY KEY,      
             name TEXTE,
             price INTEGER)''')
    
    cursor.execute('''
         CREATE TABLE IF NOT EXISTS Drinks (
             id TEXT PRIMARY KEY,      
             name TEXTE,
             price INTEGER)''')
    conn.commit()
    conn.close()

def insert_products():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    meals_data = [
        ('M1' , 'Cheese Burger' , 10),
        ('M2' , 'Machrom Burger' , 8),
        ('M3' , 'Smach Burger(Single)' , 15),
        ('M4' , 'Smach Burger(Double)' , 25),
        ('M5' , 'Smach Burger(Trible)' , 35),
        ('M6' , 'Chiken Burger' , 12),
        ('M7' , 'Frensh Fries' , 5)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Meals (id , name , price) VALUES (? , ? , ?)',meals_data)

    drinks_data = [
        ('D1' , 'Cola' , 3),
        ('D2' , 'Sprite' , 3),
        ('D3' , 'Ice Coffee' , 10),
        ('D4' , 'Blue Berry' , 10),
        ('D5' , 'Latte' , 8),
        ('D6' , 'Lemon' , 10),
        ('D7' , 'Orange' , 10)
    ]

    cursor.executemany('INSERT OR IGNORE INTO Drinks (id , name , price) VALUES (? , ? , ?)',drinks_data)

    conn.commit()
    conn.close()

def get_product_prices():
    conn = sqlite3.connect('Products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT price FROM Meals')
    meal_prices = [row[0] for row in cursor.fetchall()]

    cursor.execute('SELECT price FROM Drinks')
    drink_prices = [row[0] for row in cursor.fetchall()]

    conn.close()

    return meal_prices , drink_prices

create_tables()
insert_products()
