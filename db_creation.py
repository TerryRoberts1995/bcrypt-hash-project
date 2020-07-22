import sqlite3 

conn = sqlite3.connect('demo.db')

print("database connection successful.")

conn.execute("""CREATE TABLE EMPLOYEES
                (ID INTEGER PRIMARY KEY NOT NULL,
                USERNAME TEXT NOT NULL,
                PASSWORD TEXT NOT NULL,
                AGE INT NOT NULL); """)


print("Table Create successfully")

conn.close()

