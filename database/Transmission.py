from User import User
from notifications import Notifications
from Portfolio import Portfolio
from Stock import Stock
from Property import Property
from Commodity import Commodity
import sqlite3
import json

class Transmission:

    def __init__(self): #connects to db and makes a cursor
        self.connect = sqlite3.connect("mydb.db")
        self.cur = self.connect.cursor()

    def insert_user(self, user): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'User' VALUES(?,?,?,?,?,?,?)", (user.id, user.username, user.password, user.email, user.dateofbirth, user.genderID, json.dumps((user.userPortfolios))))
        self.connect.commit()

    def insert_porfolio(self, portfolio): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'Portfolios' VALUES(?,?,?,?,?,?,?)", (portfolio.name, portfolio.id, portfolio.userID, portfolio.funds, json.dumps(portfolio.stocks),  json.dumps(portfolio.commodities), json.dumps((portfolio.properties))))
        self.connect.commit()

    def insert_stock(self, stock): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'Stock' VALUES(?,?,?,?,?,?,?,?)", (stock.name, stock.nameABV, stock.url, stock.id, stock.portfolioID, stock.userID, stock.avgSharePrice, stock.Shares))
        self.connect.commit()

    def insert_property(self, property): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'Property' VALUES(?,?,?,?,?,?,?)", (property.name, property.type, property.url, property.id, property.portfolioID, property.userID , property.unitPrice))
        self.connect.commit()

    def insert_commodity(self, commodity): #inserts a user into the database and saves database
        self.cur.execute("INSERT INTO 'Commodity' VALUES(?,?,?,?,?,?,?)", (commodity.name, commodity.type, commodity.id, commodity.portfolioID, commodity.userID, commodity.amount, commodity.avgUnitPrice))
        self.connect.commit()

    def delete_user(self, user): # deletes a user and its associated portfolio, stock, property, commodity
        try:
            user_id_to_search = user.get_id()

            self.cur.execute("DELETE from 'Portfolios' WHERE userID=?", (user_id_to_search,))
            self.cur.execute("DELETE from 'Stock' WHERE userID=?", (user_id_to_search,))
            self.cur.execute("DELETE from 'Property' WHERE userID=?", (user_id_to_search,))
            self.cur.execute("DELETE from 'Commodity' WHERE userID=?", (user_id_to_search,))
            try:
                self.cur.execute("DELETE * from 'User' WHERE userID=?", (user_id_to_search,))
            except sqlite3.Error as error:
                print("Failed to delete User object")
                return -1
        except sqlite3.Error as error:
            print("Failed to delete User portfolio info")
            return -1
        return 0

    def search_portfolio_by_id(self, id): #searches a portfolio by its unique id and returns it
        self.cur.execute("SELECT * FROM 'Portfolios' WHERE id=?", (id,))
        portfolio = self.cur.fetchone()
        try:
            portfolioobject = Portfolio(portfolio[0], portfolio[1], portfolio[2], portfolio[3], json.loads(portfolio[4]), json.loads(portfolio[5]), json.loads(portfolio[6]))
            return portfolioobject
        except TypeError:
            return -1 #couldn't find


    def search_stock_by_id(self, id): #searches a stock by its unique id and returns it
        self.cur.execute("SELECT * FROM 'Stock' WHERE id=?", (id,))
        stock = self.cur.fetchone()
        try:
            stockobject = Stock(stock[0],stock[1],stock[2],stock[3],stock[4],stock[5],stock[6],stock[7])
            return stockobject
        except TypeError:
            return -1 #couldn't find

    def search_property_by_id(self, id): #searches a property by its unique id and returns it
        self.cur.execute("SELECT * FROM 'Property' WHERE id=?", (id,))
        property = self.cur.fetchone()
        try:
            propertyobject = Property(property[0],property[1],property[2],property[3],property[4],property[5],property[6])
            return propertyobject
        except TypeError:
            return -1 #couldn't find
    def search_commodity_by_id(self, id): #searches a commodity by its unique id and returns it
        self.cur.execute("SELECT * FROM 'Commodity' WHERE id=?", (id,))
        commodity = self.cur.fetchone()
        try:
            commodityobject = Commodity(commodity[0],commodity[1],commodity[2],commodity[3],commodity[4],commodity[5],commodity[6])
            return commodityobject
        except TypeError:
            return -1 #couldn't find

    def search_user_by_id(self, id): #searches a user by id and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE id=?", (id,))
        user = self.cur.fetchone()
        try:
            userobject = User(user[0], user[1], user[2], user[3], user[4], user[5], json.loads(user[6]))
            return userobject
        except TypeError:
            return -1 #couldn't find

    def search_user_by_username(self, username):#searches a user by username and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE username=?", (username,))
        user = self.cur.fetchone()
        try:
            userobject = User(user[0], user[1], user[2], user[3], user[4], user[5], json.loads(user[6]))
            return userobject
        except TypeError:
            return -1 #couldn't find

    def search_user_by_password(self, email):#searches a user by email and returns the user
        self.cur.execute("SELECT * FROM 'User' WHERE password=?", (email,))
        user = self.cur.fetchone()
        userobject = User(user[0], user[1], user[2], user[3], user[4], user[5], json.loads(user[6]))
        return userobject

    def insert_notification(self, notification):
        self.cur.execute("Insert Into 'Notifications' VALUES(?, ?, ?, ?, ?)", (notification.id, notification.userid, notification.code, notification.name, notification.text))
        self.connect.commit()

    def retrieve_notification_by_user(self, user):
        self.cur.execute("SELECT * FROM 'Notifications' WHERE userid=?", (user.id,))
        notifications = self.cur.fetchall()
        notificationlist = []
        for notification in notifications:
            notificationlist.append(Notifications(notification[0], notification[1], notification[2], notification[3], notification[4]))
        return notificationlist


    def save(self): #saves the database
        self.connect.commit()

    def close(self): #closes the connection to database
        self.connect.close()

    def login_sequence(self, username, password): #returns user when correct, error code when not
        user = self.search_by_username(username)
        if user == -1:
            return -1 #user nonexistant
        else:
            if user.password == password:
                return 1 #in current commit return user
            else:
                return -2 # password different
