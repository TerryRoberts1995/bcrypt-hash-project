import bcrypt
import sqlite3

conn = sqlite3.connect('demo.db')
print("Opened db connection")

data = conn.execute("SELECT id, username, password, age FROM EMPLOYEES")


for row in data:
    print("ID= ", row[0])
    print("ID= ", row[1])
    print("password= ", row[2])
    print("age= ", row[3], "\n")

    password_hash = row[2]

    user_password = input("please verify password: ")
    valid_password = bcrypt.hashpw(user_password.encode(), password_hash) == password_hash

    print(valid_password)

print("data has returned correctly.")