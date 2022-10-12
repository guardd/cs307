import yfinance as yf
import Portfolio
import Stock
class StockData:
    def __init__(self, nameABV, userID, portfolioID, stockID):
    
        self.nameABV = nameABV
        self.userID = userID
        self.portfolioID = portfolioID
        self.stockID = stockID

        self.ticker = yf.Ticker(self.nameABV)
        self.stockInfo = self.ticker.info


    def get_price(self):
     return self.stockInfo['ask']
    
    def get_company_name(self):
     return self.stockInfo['shortName']

        

    
    

         