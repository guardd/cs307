import sqlite3
import json
from IDCreation import IDCreation
class Stock:
    def __init__(self, name, nameABV, id, portfolioID, userID, avgSharePrice, shares, color):
    
        self.name = name #TEXT
        self.nameABV = nameABV #TEXT
        self.id = id #INTEGER
        self.portfolioID = portfolioID #INTEGER
        self.userID = userID #INTEGER
        self.avgSharePrice = avgSharePrice #INTEGER
        self.shares = shares #INTEGER
        self.color = color #IDCreation.generate_color_hex()
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()
    



    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name
    
    def get_nameABV(self):
        return self.nameABV 

    def set_nameABV(self, nameABV):
        self.nameABV = nameABV

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_portfolioID(self):
        return self.portfolioID

    def set_portfolioID(self, portfolioID):
        self.portfolioID = portfolioID

    def get_userID(self):
        return self.userID

    def set_userID(self, userID):
        self.userID = userID
    
    def get_avgSharePrice(self):
        return self.avgSharePrice

    def set_avgSharePrice(self, avgSharePrice):
        self.avgSharePrice = avgSharePrice
    
    def get_shares(self):
        return self.shares

    def set_shares(self, shares):
        self.shares = shares
    def get_color(self):
        return self.color
    def update_stockShares(self, shares):
        self.cur.execute("UPDATE 'Stock' SET shares=? WHERE id=?", (shares, self.id,))
        self.connect.commit()
    def update_stockAvgSharePrice(self, avgSharePrice, id):
        self.cur.execute("UPDATE 'Stock' SET avgSharePrice=? WHERE id=?", (avgSharePrice, id,))
        self.connect.commit()