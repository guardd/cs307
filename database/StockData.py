import yfinance as yf
import Portfolio
import Stock
import csv
import json
import sqlite3
import nasdaqscrape
import re
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
def get_price_nasdaq(nameABV):
    connect = sqlite3.connect("mydb.db") ##connects to database
    cur = connect.cursor()
    price = cur.execute("SELECT LastSale FROM 'StockData' WHERE Symbol=?", (nameABV,))
    return price
def get_company_name(nameABV):
   ticker = yf.Ticker(nameABV)
   return ticker.info['shortName']

def get_news(userID):
    connect = sqlite3.connect("mydb.db") ##connects to database
    cur = connect.cursor()
    print(userID)

    cur.execute("SELECT nameABV FROM 'Stock' WHERE userID=?", (userID,))
    nameABV = cur.fetchall()
    if nameABV == None:
        return -1
    
    names = []
    for x in range(nameABV.__len__()):
        if x == 3:
            break
        names.append(str(nameABV[x]))
    tickers = ' '.join(names)    
    regex = re.compile('[^a-zA-Z ]')
    #First parameter is the replacement, second parameter is your input string
    tickers = regex.sub('', tickers)
    ticker = yf.Tickers(tickers)

    newsPackage = []
    newsPackage.append(ticker.symbols)
    news = ticker.news()
    for x in ticker.symbols:
     
     newsPackage.append(news[x][0])
    print(newsPackage)
    return newsPackage
def store_stock_info():
        connect = sqlite3.connect("mydb.db") ##connects to database
        cur = connect.cursor()
        with open('Stocks.csv', newline='') as csvfile:

            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            for row in spamreader:
                if row[10] == '':
                    row[10] = "no industry"
                if row[9] == '':
                    row[9] = "no sector"
                if row[8] == '':
                    row[8] =0
                if row[7] == '':
                    row[7] = "n/a"
                if row[6] == '':
                    row[6] = "n/a"
                if row[5] == '':
                    row[5] = 0
                if row[4] == '':
                    row[4] = "0%"
                if row[3] == '':
                    row[3] = 0
                if row[2] == '':
                    row[2] = "$0"
                if row[1] == '':
                    row[1] = 0
                if row[0] == '':
                    row[0] = "n/a"

                cur.execute("INSERT INTO 'StockData' VALUES(?,?,?,?,?,?,?,?,?,?,?)", (row[0],row[1],row[2][1:],row[3],row[4][:-1],row[5],row[6],row[7],row[8],row[9],row[10]))
                        
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
                if row[10] == '':
                    row[10] = "no industry"
                if row[9] == '':
                    row[9] = "no sector"
                if row[8] == '':
                    row[8] = 0
                if row[7] == '':
                    row[7] = "n/a"
                if row[6] == '':
                    row[6] = "n/a"
                if row[5] == '':
                    row[5] = 0
                if row[4] == '':
                    row[4] = "0%"
                if row[3] == '':
                    row[3] = 0
                if row[2] == '':
                    row[2] = "$0"
                if row[1] == '':
                    row[1] = 0
                if row[0] == '':
                    row[0] = "n/a"
                    print(row[0])
                    cur.execute("UPDATE 'StockData' SET LastSale=?, NetChange=?, PercentChange=?, MarketCap=?, Volume=? WHERE Symbol=?", (row[2][1:],row[3],row[4][:-1],row[5],row[8],row[0]))
           connect.commit()          
           
           
def pull_top_stocks(sortType):
    connect = sqlite3.connect("mydb.db") ##connects to database
    cur = connect.cursor()

    

    if sortType == None:
        return -1

    elif sortType == 'Volume':

        cur.execute("SELECT Symbol, Name, Volume FROM 'StockData' ORDER BY Volume DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Market Cap':
        cur.execute("SELECT Symbol, Name, MarketCap FROM 'StockData' ORDER BY 'MarketCap' DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Last Sale':
        cur.execute("SELECT Symbol, Name, LastSale FROM 'StockData' ORDER BY 'LastSale' DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Net Change':
        cur.execute("SELECT Symbol, Name, NetChange FROM 'StockData' ORDER BY 'NetChange' DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Industry':
        industries = None
        with open('Industries.txt') as f:
            industries = f.readlines()

        topInfo = []
        for industry in industries:
             cur.execute("SELECT Symbol, Name, MarketCap FROM 'StockData' WHERE Industry=? ORDER BY MarketCap DESC LIMIT 1",(industry,))
             topIndustry = cur.fetchall()
             if topIndustry == None:
                return -1
             topInfo.append(topIndustry)
        print(topInfo)
        
        return topInfo
    else:
        return 0  
