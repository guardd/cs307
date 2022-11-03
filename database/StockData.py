import yfinance as yf
import Portfolio
import Stock
import csv
import json
import sqlite3
import nasdaqscrape
##class StockData:
   ## def __init__(self, nameABV, userID, portfolioID, stockID):
    
        ##self.nameABV = nameABV
        ##self.userID = userID
        ##self.portfolioID = portfolioID
        ##self.stockID = stockID

       ## self.ticker = yf.Ticker(self.nameABV)
     ##   self.stockInfo = self.ticker.info
def get_price(nameABV):

   ticker = yf.Ticker(nameABV)

   return ticker.info['ask']
    
def get_company_name(nameABV):
   ticker = yf.Ticker(nameABV)
   return ticker.info['shortName']
   
def store_stock_info():
        connect = sqlite3.connect("mydb.db") ##connects to database
        cur = connect.cursor()
        with open('Stocks.csv', newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in spamreader:
                cur.execute("INSERT INTO 'StockData' VALUES(?,?,?,?,?,?,?,?,?,?,?)", (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10]))
                        
            connect.commit()    

def update_stock_info():
        connect = sqlite3.connect("mydb.db") ##connects to database
        cur = connect.cursor()
        nasdaqscrape.scrape_nasdaq()
        with open('Stocks.csv', newline='') as csvfile:

           spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
           
           for row in spamreader:
            if row[0] == "Symbol":
               pass
            else:   
                    print(row[0])
                    cur.execute("UPDATE 'StockData' SET LastSale=?, NetChange=?, PercentChange=?, MarketCap=?, Volume=? WHERE Symbol=?", (row[2],row[3],row[4],row[5],row[9],row[0]))
           connect.commit()          
               