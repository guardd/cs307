from Transmission import Transmission
import Stock
from StockData import StockData
import Portfolio
import Property
import Commodity
import User
from IDCreation import IDCreation
class Trade:
    def __init__(self, id):
        self.user = Transmission.search_user_by_id(id)
        

        
    
    
    
    
    
    
    
    
    def buy_stock(self, nameABV, portfolioID, shares):

     stock =Transmission.search_stock_by_nameABV(nameABV, portfolioID)
     price = shares * StockData.get_price()
     if self.user.get_funds < price:
         return "User cannot afford this many shares"
     elif stock==-1:
            stock = Stock(StockData.get_company_name(), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(), shares)
            Transmission.insert_stock(stock)
            self.user.add_Stock(stock.get_id())
     elif stock.get_portfolioID != portfolioID:
            
      stock = Stock(StockData.get_company_name(), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(), shares)
      Transmission.insert_stock(stock)
      self.user.add_Stock(stock.get_id())

     else:
            Transmission.remove_stock(stock.get_id()) ##remove stock from database
            currentShares = stock.get_shares()
            stock.set_shares(currentShares + shares)
            newAvgSharePrice = ((currentShares * stock.get_avgSharePrice) + (shares * StockData.get_price()))/(shares+currentShares)
            stock.set_avgSharePrice(newAvgSharePrice)
            Transmission.insert_stock(stock)
    
    def sell_stock(self,stockID,shares):
        stock = Transmission.search_stock_by_id(stockID)
        if stock ==-1:
            return -1 ## this will indicate no stock by that ID found
        elif stock.get_userID!=self.user.get_id():
            return 1 ## this will indicate stock does not belong to user
        else:
            if shares >= stock.get_shares():
             self.user.set_funds(self.user.get_funds()+(stock.get_shares()*StockData.get_price()))
             Transmission.remove_stock(stockID)
             portfolio = Transmission.search_portfolio_by_id(stock.get_portfolioID())
             Transmission.remove_portfolio(stock.get_portfolioID())
             portfolio.remove_stock(stockID)
             Transmission.insert_porfolio(portfolio)

            else:
                self.user.set_funds(self.user.get_funds()+(stock.get_shares()*StockData.get_price()))
                stock.set_shares(stock.get_shares()-shares)
                Transmission.remove_stock(stockID)
                Transmission.insert_stock(stock)
            
          

        




    

