from Transmission import Transmission
from Stock import Stock
from StockData import StockData
from Portfolio import Portfolio
from Property import Property
from Commodity import Commodity
from CommodityData import CommodityData
from User import User
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
        self.user.update_portfolios(self.user.get_userPortfolios(), self.user.get_id())
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
     if portfolio.get_funds() < price:
         return "User cannot afford this many shares"
     elif stock==-1:
            stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(nameABV), shares)
            p.insert_stock(stock)
            portfolio.add_stock(stock)
            portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     elif stock.get_portfolioID != portfolioID:
            
      stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, self.user.get_id(), StockData.get_price(nameABV), shares)
      p.insert_stock(stock)
      portfolio.add_stock(stock)
      portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
      portfolio.update_funds(portfolio.get_funds()-price)
     else:
            #p.remove_stock(stock.get_id()) ##remove stock from database
            #currentShares = stock.get_shares()
            #stock.set_shares(currentShares + shares)
            #newAvgSharePrice = ((currentShares * stock.get_avgSharePrice) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            #stock.set_avgSharePrice(newAvgSharePrice)
            #p.insert_stock(stock)
            #portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
            currentShares = stock.get_shares()
            stock.update_stockShares(currentShares + shares)
            newAvgSharePrice = ((currentShares * stock.get_avgSharePrice()) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            stock.update_stockAvgSharePrice(newAvgSharePrice)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)

    
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
             portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
             t.remove_stock(stockID)
             portfolio.remove_stock(stock)
             portfolio.update_stocks(portfolio.get_stocks(),portfolio.get_id())

            else:
                portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
                portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
                stock.set_shares(stock.get_shares()-shares)
                stock.update_stockShares(stock.get_shares())
               
            
        def buy_commodity(self, type, portfolioID, amount):
            p = Transmission()
            commodity =p.search_commodity_by_type(type,portfolioID)
            portfolio = p.search_portfolio_by_type(portfolioID)
            price = amount * CommodityData.get_commodityPrice("latest","USD",type)
            if portfolio.get_funds() < price:
                return "User cannot afford this many shares"
            elif commodity==-1:
                commodity = Commodity(Commodity.get_company_name(type), type, IDCreation.generate_ID(), portfolioID, self.user.get_id(), amount, price)
                p.insert_commodity(commodity)
                portfolio.add_commodity(commodity)
                portfolio.update_commodities(portfolio.get_commodities(), portfolioID)
                portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
            elif commodity.get_portfolioID != portfolioID:
            
                commodity = Commodity(Commodity.get_company_name(type), type, IDCreation.generate_ID(), portfolioID, self.user.get_id(), amount, price)
                p.insert_commodity(commodity)
                portfolio.add_commodity(commodity)
                portfolio.update_commodities(portfolio.get_commodities(), portfolioID)
                portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
            else:
                #p.remove_stock(stock.get_id()) ##remove stock from database
            #currentShares = stock.get_shares()
            #stock.set_shares(currentShares + shares)
            #newAvgSharePrice = ((currentShares * stock.get_avgSharePrice) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            #stock.set_avgSharePrice(newAvgSharePrice)
            #p.insert_stock(stock)
            #portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
                currentAmount = commodity.get_amount()
                commodity.update_amount(currentAmount + amount)
                newAvgUnitPrice = ((currentAmount * commodity.get_avgUnitPrice()) + (amount * price))/(amount+currentAmount)
                commodity.update_commodityAvgUnitPrice(newAvgUnitPrice)
                portfolio.update_funds(portfolio.get_funds()-price, portfolioID)

            return 0
        def sell_commodity(self, commodityID, amount):
            t = Transmission()
            stock = t.search_stock_by_id(stockID)
            ortfolio = t.search_portfolio_by_id(stock.get_portfolioID())
            if stock==-1 or portfolio==-1:
                 return -1 ## this will indicate no stock or portfolio by that ID found
            elif stock.get_userID()==self.user.get_id():
                print(stock.get_userID())
                print(self.user.get_id())
                return 1 ## this will indicate stock does not belong to user
            else:
                if shares >= stock.get_shares():
                    portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
                    portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
                    t.remove_stock(stockID)
                    portfolio.remove_stock(stock)
                    portfolio.update_stocks(portfolio.get_stocks(),portfolio.get_id())

                else:
                    portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
                    portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
                    stock.set_shares(stock.get_shares()-shares)
                    stock.update_stockShares(stock.get_shares())   
        def buy_property():
            return 0
        def sell_property():
            return 0
        




    

