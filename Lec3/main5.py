"""
ORM -> django models
"""
import sqlite3

class User:
    __tablename__ = "users"
    def __init__(self, username:str, password:str):
        self.username = username 
        self.password = password 

    def insert(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        insert_query = "INSERT INTO {} VALUES(NULL, ?, ?)".format(self.__tablename__)
        cur.execute(insert_query, (self.username, self.password))

        conn.commit()
        conn.close()

    def delete(self):
        conn = sqlite3.connect("data.db")
        cur = conn.cursor()

        delete_query = "DELETE FROM {} WHERE username=?".format(self.__tablename__)
        cur.execute(delete_query, (self.username,))

        conn.commit()
        conn.close()
