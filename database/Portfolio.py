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
    
    def get_stocks(self):
       return self.stocks
   
    def get_properties(self):
       return self.property
   
    def get_commodities(self):
       return self.commodities

    def add_stock(self, stock):
        self.stocks.append(stock.get_id())

    def add_commodity(self, commodity):
        self.commodities.append(commodity.get_id())
    
    def add_property(self, property):
        self.properties.append(property.get_id())

    def remove_stock(self, stock):
        self.stocks.remove(stock.get_id())

    def remove_commodity(self, commodity):
        self.commodities.remove(commodity.get_id())
    
    def remove_property(self, property):
        self.properties.remove(property.get_id())