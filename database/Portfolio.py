class Portfolio:
    def __init__(self, name, id, userID, funds, stocks, commodities, properties):
    
        self.name = name #TEXT
        self.id = id #INTEGER
        self.userID = userID #INTEGER
        self.funds = funds #INTEGER

        self.stocks = stocks
        self.commodities = commodities
        self.properties = properties



    def get_name(self):
        return self.name 

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_userID(self):
        return self.userID

    def set_userID(self, userID):
        self.userID = userID

    def get_funds(self):
        return self.funds

    def set_funds(self, funds):
        self.funds = funds

    def add_stock(self, stock):
        self.stocks.append(stock)

    def add_commodity(self, commodity):
        self.commodities.append(commodity)
    
    def add_property(self, property):
        self.properties.append(property)

    def remove_stock(self, stock):
        self.stocks.remove(stock)

    def remove_commodity(self, commodity):
        self.commodities.remove(commodity)
    
    def remove_property(self, property):
        self.properties.remove(property)