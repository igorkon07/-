import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS not_telegram(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON not_telegram (email)")

cursor.execute("DELETE FROM not_telegram")

for i in range(1,11):
    cursor.execute("INSERT INTO not_telegram (username,email,age,balance) VALUES (?,?,?,?)", (f"newuser{i}", f"example{i}@gmail.com", i*10, 1000))

for i in range(1,11):
    if ((i+1)%2) == 0:
        cursor.execute("UPDATE not_telegram SET balance = ? WHERE id = ?", (500, i))

for i in range(1,11):
    if ((i+2)%3) == 0:
        cursor.execute(f"DELETE FROM not_telegram WHERE id = {i}")

cursor.execute("SELECT * FROM not_telegram WHERE age != 60")
result = cursor.fetchall()
for i in result:
    print(f'Имя: {i[1]} | Почта: {i[2]}  | Возраст: {i[3]}  | Баланс: {i[4]}' )


connection.commit()
connection.close()