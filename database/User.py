import sqlite3
import json
class User:
    def __init__(self, id, username, password, email, dateofbirth, genderID, userPortfolios):
        self.id = id #INTEGER PRIMARY KEY
        self.username = username #TEXT
        self.password = password #TEXT
        self.email = email #TEXT
        self.dateofbirth = dateofbirth #INTEGER
        self.genderID = genderID #TEXT
        self.userPortfolios = userPortfolios #INTEGER in id
        
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()
#        self.notifications = #INTEGER in id
#        self.predictions = #INTEGER in id


    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):
        self.password = password

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email

    def get_dateofbirth(self):
        return self.dateofbirth

    def set_dateofbirth(self, dateofbirth):
        self.dateofbirth = dateofbirth

    def get_genderID(self):
        return self.genderID

    def set_genderID(self, genderID):
        self.genderID = genderID
    
    def get_userPortfolios(self):
        return self.userPortfolios
    
    def add_portfolio(self, portfolio):
        self.userPortfolios.append(portfolio.get_id())
        self.update_portfolios()
    
    def remove_portfolio(self, portfolio):
        self.userPortfolios.remove(portfolio.get_id())
        self.update_portfolios()

    def change_username(self, username, id):        
         self.cur.execute("UPDATE 'User' SET username=? WHERE id=?", (username,id,))
         self.connect.commit()
    
    def change_password(self, password, id):
         self.cur.execute("UPDATE 'User' SET password=? WHERE id=?", (password,id,))
         self.connect.commit()
    
    def update_portfolios(self):
        self.cur.execute("UPDATE 'User' SET userPortfolios=? WHERE id=?", (json.dumps(self.userPortfolios), self.id,))
        self.connect.commit()
    

    #def get_notifications(self):
    #    return self.notifications

    #def get_predictions(self):
    #    return self.predictions
