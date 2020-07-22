import bcrypt
import sqlite3


user_name = input("Please enter a name: ")
user_password = input("Please enter a password: ")
age = int(input("Please enter your age: "))

hashed_password = bcrypt.hashpw(user_password.encode('utf8'), bcrypt.gensalt())

conn = sqlite3.connect('demo.db')

print("Opened DB connection ")

conn.execute("INSERT INTO EMPLOYEES (ID, USERNAME, PASSWORD, AGE ) \
              VALUES  (NULL,?,?,?)", (user_name, hashed_password, age))


conn.commit()


print("Record entered")


conn.close()