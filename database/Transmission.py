from User import User
import sqlite3

class Transmission:

    def __init__(self): #connects to db and makes a cursor
        self.connect = sqlite3.connect("mydb.db")
        self.cur = self.connect.cursor()

    def search_by_id(self, id): #searches a user by id and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE id=?", (id,))
        user = self.cur.fetchone()
        try:
            userobject = User(user[0], user[1], user[2], user[3], user[4], user[5])
            return userobject
        except TypeError:
            return -1 #couldn't find

    def insert_user(self, user): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'User' VALUES(?,?,?,?,?,?)", (user.id, user.username, user.password, user.email, user.dateofbirth, user.genderID))
        self.connect.commit()

    def search_by_username(self, username):#searches a user by username and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE username=?", (username,))
        user = self.cur.fetchone()
        try:
            userobject = User(user[0], user[1], user[2], user[3], user[4], user[5])
            return userobject
        except TypeError:
            return -1 #couldn't find

    def search_by_password(self, email):#searches a user by email and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE password=?", (email,))
        user = self.cur.fetchone()
        userobject = User(user[0], user[1], user[2], user[3], user[4], user[5])
        return userobject

    def save(self): #saves the database
        self.connect.commit()

    def close(): #closes the connection to database
        self.connect.close()

    def login_sequence(self, username, password): #returns user when correct, error code when not
        user = self.search_by_username(username)
        if user == -1:
            return -1 #user nonexistant
        else:
            if user.password == password:
                return user
            else:
                return -2 # password different
