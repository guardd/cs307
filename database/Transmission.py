from User import User
import sqlite3

class Transmission:

    def __init__(self):
        self.connect = sqlite3.connect("mydb.db")
        self.cur = self.connect.cursor()

    def search_by_id(self, id):
        self.cur.execute("SELECT * FROM 'User' WHERE id=?", (id,))
        user = self.cur.fetchone()
        
        userobject = User(user[0], user[1], user[2], user[3], user[4], user[5])
        return userobject

    def search_by_username(self, username):
        self.cur.execute("SELECT * FROM 'User' WHERE username=?", (username,))
        user = self.cur.fetchone()
        a, b, c, d, e, f = user
        userobject = User(a, b, c, d, e, f)
        return userobject

    def search_by_password(self, password):
        self.cur.execute("SELECT * FROM 'User' WHERE password=?", (password,))
        user = self.cur.fetchone()
        a, b, c, d, e, f = user
        userobject = User(a, b, c, d, e, f)
        return userobject

    def add_user_to_database(self, user):
        self.cur.execute("INSERT INTO User VALUES(1000, 'example_username', 'example_password', 'example_email@email.com', '20010428', 'M')", )

    def save():
        connect.commit()

    def close():
        connect.close()
