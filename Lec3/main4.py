import sqlite3 

"""
CRUD - Create/Read/Update/Delete
"""

conn = sqlite3.connect("data.db")
cur = conn.cursor()


create_query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)"
cur.execute(create_query)


####USER CREATION
users = [
    ("Bob", "78192312"),
    ("Alice", "kjasgdh71dy"),
    ("Derek", "uiy1e1g2hed1i"),
]
insert_query = "INSERT INTO userse VALUES(NULL, ?, ?)"
for user in users:
    cur.execute(insert_query, user)
conn.commit()

conn.close()
