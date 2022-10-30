import sqlite3
import json
class Commodity:
   def __init__(self, name, type, id, portfolioID, userID, amount, avgUnitPrice):
    
        self.name = name #TEXT
        self.type = type #TEXT
        self.id = id #INTEGER
        self.portfolioID = portfolioID #INTEGER
        self.userID = userID #INTEGER
        self.amount = amount #INTEGER
        self.avgUnitPrice = avgUnitPrice #INTEGER
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()





   def get_name(self):
        return self.name 

   def set_name(self, name):
        self.name = name
    
   def get_type(self):
        return self.type 

   def set_type(self, type):
        self.type = type

   def get_id(self):
        return self.id

   def set_id(self, id):
        self.id = id
    
   def get_protfolioID(self):
        return self.userID

   def set_porfolioID(self, portfolioID):
        self.portfolioID = portfolioID

   def get_userID(self):
        return self.userID

   def set_userID(self, userID):
        self.userID = userID
    
   def get_amount(self):
        return self.amount

   def set_amount(self, amount):
        self.amount = amount
    
   def get_avgUnitPrice(self):
        return self.avgUnitPrice

   def set_avgUnitPrice(self, avgUnitPrice):
        self.avgUnitPrice = avgUnitPrice
    
   def update_commodityAmount(self, amount, id):
        self.cur.execute("UPDATE 'Commodity' SET amount=? WHERE id=?", (amount, id,))
        self.connect.commit()
   def update_commodityAvgUnitPrice(self, avgUnitPrice, id):
        self.cur.execute("UPDATE 'Commodity' SET avgUnitPrice=? WHERE id=?", (avgUnitPrice, id,))
        self.connect.commit() 
    