class Property:
    def __init__(self, name, type, url, id, portfolioID, userID, unitPrice):
    
        self.name = name #TEXT
        self.type = type #TEXT
        self.url = url #TEXT
        self.id = id #INTEGER
        self.portfolioID = portfolioID #INTEGER
        self.userID = userID #INTEGER
        self.unitPrice = unitPrice #INTEGER





    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name
    
    def get_type(self):
        return self.type 

    def set_type(self, type):
        self.type = type
    
    def get_url(self):
        return self.url

    def set_url(self, url):
        self.id = url

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
    
    def get_unitPrice(self):
        return self.unitPrice

    def set_unitPrice(self, unitPrice):
        self.unitPrice = unitPrice