from Transmission import Transmission
import Stock
from StockData import StockData
import Portfolio
import Property
import Commodity
import User
from IDCreation import IDCreation
class Trade:
    def __init__(self, uid):
        p = Transmission()
        self.user = p.search_user_by_id(uid)
        

        
    
    
    
    def create_new_portfolio(self, name, funds):
        portfolio = Portfolio(name, IDCreation.generate_ID(), self.user.get_id(), funds, [], [], [])
        self.user.add_portfolio(portfolio)
        p = Transmission()
        p.insert_portfolio(portfolio)
    
    def delete_portfolio(self, portfolioID):
        p = Transmission()
        portfolio = Transmission.search_portfolio_by_id(portfolioID)

        stocklist = portfolio.get_stocks()
        propertylist = portfolio.get_properties()
        commoditylist =  portfolio.get_commodities()

        for x in stocklist:
            p.remove_stock(x)
        
        for x in propertylist:
            p.remove_property(x)
        
        for x in commoditylist:
            p.remove_commodity(x)
        
        p.remove_portfolio(portfolio)

        self.user.remove_portfolio(portfolio)

        self.user.update_portfolios(self.user.get_userPortfolios(), self.user.get_id())
    
    
    
    def buy_stock(self, nameABV, portfolioID, shares):
     p = Transmission()
     stock =p.search_stock_by_nameABV(nameABV, portfolioID)
     portfolio = p.search_portfolio_by_id(portfolioID)
     price = shares * StockData.get_price(nameABV)
     if portfolio.get_funds < price:
         return "User cannot afford this many shares"
     elif stock==-1:
            stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(nameABV), shares)
            p.insert_stock(stock)
            self.user.add_Stock(stock.get_id())
     elif stock.get_portfolioID != portfolioID:
            
      stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(nameABV), shares)
      p.insert_stock(stock)
      self.user.add_Stock(stock.get_id())

     else:
            p.remove_stock(stock.get_id()) ##remove stock from database
            currentShares = stock.get_shares()
            stock.set_shares(currentShares + shares)
            newAvgSharePrice = ((currentShares * stock.get_avgSharePrice) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            stock.set_avgSharePrice(newAvgSharePrice)
            p.insert_stock(stock)
    
    def sell_stock(self,stockID,shares):
        t = Transmission()
        stock = t.search_stock_by_id(stockID)
        portfolio = t.search_portfolio_by_id(stock.get_portfolioID())
        if stock==-1 or portfolio==-1:
            return -1 ## this will indicate no stock or portfolio by that ID found
        elif stock.get_userID()==self.user.get_id():
            print(stock.get_userID())
            print(self.user.get_id())
            return 1 ## this will indicate stock does not belong to user
        else:
            if shares >= stock.get_shares():
             portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
             t.remove_stock(stockID)
             portfolio = t.search_portfolio_by_id(stock.get_portfolioID())
             t.remove_portfolio(stock.get_portfolioID())
             portfolio.remove_stock(stock)
             t.insert_porfolio(portfolio)

            else:
                portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
                stock.set_shares(stock.get_shares()-shares)
                t.remove_portfolio(stock.get_portfolioID())
                t.insert_portfolio(portfolio)
                t.remove_stock(stockID)
                t.insert_stock(stock)
            
          

        




    

