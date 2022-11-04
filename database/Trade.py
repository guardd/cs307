from Transmission import Transmission
from Stock import Stock
#from StockData import StockData
import StockData
from Portfolio import Portfolio
from Property import Property
from Commodity import Commodity
from CommodityData import CommodityData
from User import User
from IDCreation import IDCreation
class Trade:
    def __init__(self):
        self.p = Transmission()

        

        
    
    
    
    def create_new_portfolio(self, uid, name, funds):
  
        portfolio = Portfolio(name, IDCreation.generate_ID(), uid, funds, [], [], [])
        p.search_user_by_id(uid).add_portfolio(portfolio)
        p = Transmission()
        p.insert_portfolio(portfolio)

        
    def delete_portfolio(self, uid, portfolioID):
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

        p.search_user_by_id(uid).remove_portfolio(portfolio)

 
    
    
    
    def buy_stock(self, uid, nameABV, portfolioID, shares):
     p = Transmission()
     stock =p.search_stock_by_nameABV(nameABV, portfolioID)
     portfolio = p.search_portfolio_by_id(portfolioID)
     try:
        price = shares * StockData.get_price(nameABV)
     except KeyError:
        return -2
     if shares <= 0:
        return -3
     if portfolio.get_funds() < price:
         return -1
     elif stock==-1:
            stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, uid, StockData.get_price(nameABV), shares, IDCreation.generate_color_hex())
            p.insert_stock(stock)
            portfolio.add_stock(stock)
            portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     elif stock.get_portfolioID() != portfolioID:
            
      stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, uid, StockData.get_price(nameABV), shares, IDCreation.generate_color_hex())
      p.insert_stock(stock)
      portfolio.add_stock(stock)
      portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
      portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     else:
            #p.remove_stock(stock.get_id()) ##remove stock from database
            #currentShares = stock.get_shares()
            #stock.set_shares(currentShares + shares)
            #newAvgSharePrice = ((currentShares * stock.get_avgSharePrice) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            #stock.set_avgSharePrice(newAvgSharePrice)
            #p.insert_stock(stock)
            #portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
            currentShares = stock.get_shares()
            stock.update_stockShares(currentShares + shares, stock.id)
            newAvgSharePrice = ((currentShares * stock.get_avgSharePrice()) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            stock.update_stockAvgSharePrice(newAvgSharePrice, stock.id)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     return 1
    
    def sell_stock(self, uid, stockID,shares):
        t = Transmission()
        stock = t.search_stock_by_id(stockID)
        portfolio = t.search_portfolio_by_id(stock.get_portfolioID())
        if stock==-1 or portfolio==-1:
            return -1 ## this will indicate no stock or portfolio by that ID found
        elif stock.get_userID()!=uid:
            print(stock.get_userID())
            print(uid)
            return 1 ## this will indicate stock does not belong to user
        else:
            if shares >= stock.get_shares():
             portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
             portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
             t.remove_stock(stockID)
             portfolio.remove_stock(stock)
             portfolio.update_stocks(portfolio.get_stocks(),portfolio.get_id())

            else:
                return -2
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
                commodity = Commodity(Commodity.get_company_name(type), type, IDCreation.generate_ID(), portfolioID, uid, amount, price)
                p.insert_commodity(commodity)
                portfolio.add_commodity(commodity)
                portfolio.update_commodities(portfolio.get_commodities(), portfolioID)
                portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
            elif commodity.get_portfolioID != portfolioID:
            
                commodity = Commodity(Commodity.get_company_name(type), type, IDCreation.generate_ID(), portfolioID, uid, amount, price)
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
    def sell_commodity(self, uid, commodityID, amount):
            t = Transmission()
            stock = t.search_stock_by_id(stockID)
            ortfolio = t.search_portfolio_by_id(stock.get_portfolioID())
            if stock==-1 or portfolio==-1:
                 return -1 ## this will indicate no stock or portfolio by that ID found
            elif stock.get_userID()==t.search_user_by_id(uid).get_id():
                print(stock.get_userID())
                print(t.search_user_by_id(uid).get_id())
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
    def share_portfolio(self,friendID, toShare):
            portfolioName = toShare.name
            user = self.p.search_user_by_id(friendID)
            portfolio = toShare
            if user == -1:
                return -1
            elif portfolio ==-1:
                return -1
            else:
             try:
                ##print("1st")
                newPortfolio = Portfolio(portfolioName,IDCreation.generate_ID(), friendID,portfolio.get_funds(),[],[],[])
                stocklist = portfolio.get_stocks()
                propertylist = portfolio.get_properties()
                commoditylist =  portfolio.get_commodities()
                ##print("1st")
                for x in stocklist:
                    oldStock = self.p.search_stock_by_id(x)
                    newStock = Stock(oldStock.get_name(),oldStock.get_nameABV(),IDCreation.generate_ID(),newPortfolio.get_id(),friendID, oldStock.avgSharePrice, oldStock.get_shares(), oldStock.get_color())
                    self.p.insert_stock(newStock)
                    newPortfolio.add_stock(newStock)
                    ##print("2st")
                for x in propertylist:
                    oldProperty = self.p.get_property_by_id(x)
                    newProperty = Property(oldProperty.get_name(),oldProperty.get_type(),oldProperty.get_URL(),IDCreation.generate_ID(),newPortfolio.get_id(),friendID, oldStock.get_unitPrice())
                    newPortfolio.add_property(newProperty)
                   ## print("3st")
        
                for x in commoditylist:
                    oldCommodity = self.p.search_commodity_by_id(x)
                    newCommodity = Commodity(oldCommodity.get_name(),oldCommodity.get_type(),IDCreation.generate_ID(),newPortfolio.get_id(),friendID, oldCommodity.get_avgUnitPrice())
                    newPortfolio.add_commodity(newCommodity)
                    ##print("4st")
                
                newPortfolio.update_commodities(newPortfolio.get_commodities(),newPortfolio.get_id())
                newPortfolio.update_stocks(newPortfolio.get_stocks(),newPortfolio.get_id())
                newPortfolio.update_properties(newPortfolio.get_properties(),newPortfolio.get_id())
                self.p.insert_portfolio(newPortfolio)
                user.add_portfolio(newPortfolio)
                user.update_portfolios()
                ##print("5st")
                return 0
             except TypeError:
               return 1
             

