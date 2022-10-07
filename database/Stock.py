class Stock:
    def __init__(self, name, nameABV, url, id, portfolioID, userID, avgSharePrice, shares):
    
        self.name = name #TEXT
        self.nameABV = nameABV #TEXT
        self.url = url #TEXT
        self.id = id #INTEGER
        self.portfolioID = portfolioID #INTEGER
        self.userID = userID #INTEGER
        self.avgSharePrice = avgSharePrice #INTEGER
        self.shares = shares #INTEGER





    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name
    
    def get_nameABV(self):
        return self.nameABV 

    def set_nameABV(self, nameABV):
        self.nameABV = nameABV
    
    def get_url(self):
        return self.url

    def set_url(self, url):
        self.id = url

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id
    
    def get_protfolioID(self):
        return self.portfolioID

    def set_porfolioID(self, portfolioID):
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