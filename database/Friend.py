import sqlite3
import json

class Friend:
    def __init__(self, id, friendRequests, friends, messages):
        self.id = id #TEXT
        self.friendRequests = friendRequests #TEXT : friend's ID
        self.friends = friends #TEXT : friend's ID
        self.messages = messages #TEXT : format : Text, "Friend : blah blah blah"
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()
#        self.notifications = #INTEGER in id
#        self.predictions = #INTEGER in id
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    
    def get_userPortfolios(self):
        return self.userPortfolios
    
    def add_portfolio(self, portfolio):
        self.userPortfolios.append(portfolio.get_id())
    
    def remove_portfolio(self, portfolio):
        self.userPortfolios.remove(portfolio.get_id())

    def change_username(self, username, id):        
         self.cur.execute("UPDATE 'User' SET username=? WHERE id=?", (username,id,))
         self.connect.commit()
    
    def change_password(self, password, id):
         self.cur.execute("UPDATE 'User' SET password=? WHERE id=?", (password,id,))
         self.connect.commit()
    
    def update_portfolios(self):
        self.cur.execute("UPDATE 'User' SET userPortfolios=? WHERE id=?", (json.dumps(self.userPortfolios), self.id,))
        self.connect.commit()
    