from tkinter.tix import INTEGER
import yfinance as yf
import Portfolio
import Stock
import csv
import json
import sqlite3
import nasdaqscrape
import re
import pandas as pd
from datetime import datetime
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
   if ticker.info['regularMarketPrice'] == None:
       return -1
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
    
    elif sortType == 'Trade Volume':
      
        cur.execute("SELECT Symbol, Name, Volume FROM 'StockData' ORDER BY Volume DESC LIMIT 10")
        topInfo = cur.fetchall()
       
        if topInfo == None:
           return -1
        print(topInfo[0][0])
        
        return topInfo
    elif sortType == 'Market Cap':
        cur.execute("SELECT Symbol, Name, MarketCap FROM 'StockData' ORDER BY MarketCap DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Last Sale':
        cur.execute("SELECT Symbol, Name, LastSale FROM 'StockData' ORDER BY LastSale DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Net Change':
        cur.execute("SELECT Symbol, Name, NetChange FROM 'StockData' ORDER BY NetChange DESC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        
        
        return topInfo
    elif sortType == 'Industry':
        industries = None
        with open('Industries.txt') as f:
            industries = f.readlines()
            

        topInfo = []
        newtopInfo = ''
        for industry in industries:
             newIndustry = industry.replace('\n','')
             cur.execute("SELECT Symbol, Name, MarketCap, Industry FROM 'StockData' WHERE Industry=? ORDER BY MarketCap DESC LIMIT 1",(newIndustry,))
             topIndustry = cur.fetchall()
             if topIndustry == None:
                return -1
             elif topIndustry == '[]':
                 pass
             else:
                 for x in range(topIndustry.__len__()):
                        
                    industryString = str(topIndustry[x])
                    industryString = industryString.replace(",","\t")
                    topInfo.append(industryString)
                 
        
        newtopInfo = "\n".join(topInfo)
        regex = re.compile('[^a-zA-Z0-9./\n\t ]')
        newtopInfo = regex.sub('',newtopInfo)
        print(topInfo)
        print(newtopInfo)
        #print(newtopInfo)
        
        return newtopInfo
    else:
        return 0
def pull_top_stocks_desc(sortType):
    connect = sqlite3.connect("mydb.db") ##connects to database
    cur = connect.cursor()

    if sortType == None:
        return -1
    
    elif sortType == 'Trade Volume':
      
        cur.execute("SELECT Symbol, Name, Volume FROM 'StockData' WHERE Volume > 200 ORDER BY Volume ASC LIMIT 10")
        topInfo = cur.fetchall()
       
        if topInfo == None:
           return -1
        print(topInfo[0][0])
        
        return topInfo
    elif sortType == 'Market Cap':
        cur.execute("SELECT Symbol, Name, MarketCap FROM 'StockData' WHERE MarketCap > 0 ORDER BY MarketCap ASC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Last Sale':
        cur.execute("SELECT Symbol, Name, LastSale FROM 'StockData' ORDER BY LastSale ASC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        print(topInfo)
        
        return topInfo
    elif sortType == 'Net Change':
        cur.execute("SELECT Symbol, Name, NetChange FROM 'StockData' ORDER BY NetChange ASC LIMIT 10")
        topInfo = cur.fetchall()
        if topInfo == None:
           return -1
        
        
        return topInfo
    elif sortType == 'Industry':
        industries = None
        with open('Industries.txt') as f:
            industries = f.readlines()
            

        topInfo = []
        newtopInfo = ''
        for industry in industries:
             newIndustry = industry.replace('\n','')
             cur.execute("SELECT Symbol, Name, MarketCap, Industry FROM 'StockData' WHERE Industry=? AND MarketCap > 0 ORDER BY MarketCap ASC LIMIT 1",(newIndustry,))
             topIndustry = cur.fetchall()
             if topIndustry == None:
                return -1
             elif topIndustry == '[]':
                 pass
             else:
                 for x in range(topIndustry.__len__()):
                        
                    industryString = str(topIndustry[x])
                    industryString = industryString.replace(",","\t")
                    topInfo.append(industryString)
                 
        
        newtopInfo = "\n".join(topInfo)
        regex = re.compile('[^a-zA-Z0-9./\n\t ]')
        newtopInfo = regex.sub('',newtopInfo)
        print(topInfo)
        print(newtopInfo)
        #print(newtopInfo)
        
        return newtopInfo
    else:
        return 0
 

def pull_company_data(nameABV, dateRange):
  try:
   ticker = yf.Ticker(nameABV)
   if ticker.info['regularMarketPrice'] == None:
       return -1
  except:
   return -1
  

  dateRange = int(dateRange)
 
  
  financials = pd.DataFrame.to_html(ticker.financials.iloc[:, :dateRange])
  balanceSheet = pd.DataFrame.to_html(ticker.balancesheet.iloc[:, :dateRange])
  earnings = pd.DataFrame.to_html(ticker.earnings.iloc[:, :dateRange])
  cashflow = pd.DataFrame.to_html(ticker.cashflow.iloc[:, :dateRange])
  connect = sqlite3.connect("mydb.db") ##connects to database
  conn = connect.cursor()
  companyName = ticker.info['shortName']
  dateTime = datetime.now()
  ticker.financials.to_sql(f'{companyName}-{dateTime}', connect, if_exists='replace', index=False)
  connect.commit()
  #pd.read_sql('select * from new_table_name', conn)
  
  companyData={ 
      'financials': financials,
      'balanceSheet':balanceSheet,
      'earnings':earnings,
      'cashflow':cashflow
                
      }
  #print(companyData)
  return companyData
def pull_financial_markers(nameABV):
  try:
   ticker = yf.Ticker(nameABV)
   
  except:
   return -1
  if ticker.info['regularMarketPrice'] == None:
       return -1
  financials = ticker.financials
  balanceSheet = ticker.balancesheet
  earnings = ticker.earnings
  cashflow = ticker.cashflow
  
  
  columnName = financials.columns[0]
  columnName2 = balanceSheet.columns[0]
  columnName3 = cashflow.columns[0]
  try:
    accountingProfit = (financials[columnName]['Total Revenue']) -  ((financials[columnName]['Total Operating Expenses']) +(financials[columnName]['Income Tax Expense']))#total revenue - (Cost of goods sold + operating expenses + taxes)
    accountingProfit = f'{accountingProfit:.2f}'
  except:
    accountingProfit = 'N/A'
  try:
    returnOnEquity = (financials[columnName]['Net Income']/balanceSheet[columnName2]['Total Stockholder Equity']) #net income/ Average Owners Equity
    returnOnEquity = f'{returnOnEquity:.2f}'
  except:
    returnOnEquity = 'N/A'
  try:
    debtToEquityRatio = balanceSheet[columnName2]['Long Term Debt']/balanceSheet[columnName2]['Total Stockholder Equity'] #debt/equity
    debtToEquityRatio = f'{debtToEquityRatio:.2f}'
  except:
      debtToEquityRatio = 'N/A'
  currentRatio = balanceSheet[columnName2]['Total Assets']/balanceSheet[columnName2]['Total Liab'] #current assets/ current liabilities
  try:
    burnRate = 1/(financials[columnName]['Total Revenue']/financials[columnName]['Total Operating Expenses'])  #total cost/toal revenue
    burnRate = f'{burnRate:.2f}'
  except:
    burnRate = 'N/A'
  try:
    ROI = (financials[columnName]['Gross Profit']/(financials[columnName]['Total Operating Expenses']))*100
    ROI = f'{ROI:.2f}%'
  except:
    ROI = 'N/A'
  
  
  data = {
      'accountingProfit':accountingProfit,
      'returnOnEquity':returnOnEquity,
      'debtToEquityRatio':debtToEquityRatio,
      'currentRatio':currentRatio,
      'burnRate':burnRate,
      'ROI':ROI
      }
  print(data)
  return data