class Commodity:
   def __init__(self, name, type, id, portfolioID, userID, amount, avgUnitPrice):
    
        self.name = name #TEXT
        self.type = type #TEXT
        self.id = id #INTEGER
        self.portfolioID = portfolioID #INTEGER
        self.userID = userID #INTEGER
        self.amount = amount #INTEGER
        self.avgUnitPrice = avgUnitPrice #INTEGER





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
        self.portfolioID = porfolioID

    def get_userID(self):
        return self.userID

    def set_userID(self, userID):
        self.userID = userID
    
    def get_amount(self):
        return self.userID

    def set_amount(self, amount):
        self.userID = userID
    
    def get_avgUnitPrice(self):
        return self.avgUnitPrice

    def set_avgUnitPrice(self, amount):
        self.avgUnitPrice = avgUnitPrice
    
    
    