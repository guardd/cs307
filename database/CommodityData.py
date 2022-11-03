import json
from pickle import FALSE
import sqlite3
import requests
import csv
class CommodityData:
    def __init__(self):
        self.access_key = 'zlksliz38pfu59i5qiapo815taa1g783gxu0dh6e083wevv80860yg2j13gw'
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()

    def get_commodityPrice(self, endpoint, base_currency, symbol):
      #endpoint = 'latest'
      #base_currency = 'USD'
      #symbol = 'XAU' 
      #endpoint = 'latest'
   

      resp = requests.get(
        'https://commodities-api.com/api/'+endpoint+'?access_key='+self.access_key+'&base='+base_currency+'&symbols='+symbol)
      print(resp.json())
      if resp.status_code != 200:
        # This means something went wrong.
       return -1
      else:
          return 1/resp['rates'][symbol]
    def get_CommoditySymbols(self):
        resp = requests.get('https://commodities-api.com/api/symbols''?access_key='+self.access_key)
        print (resp.json())
        for x in resp.json():
         self.cur.execute("INSERT INTO 'CommodityData' VALUES(?,?)", (x, resp.json()[x]))
         self.connect.commit()
        return resp
    def get_commodity_name(self,symbol):
        self.cur.execute("SELECT 'Name' FROM 'CommodityData' WHERE Symbols=?", (symbol,))
        companyname = self.cur.fetchone()
        if companyname==None:
            return -1
        else:
            return companyname
    def get_commodity_exchange_rate(self, symbol1, symbol2,base, amount):
       if int(amount) <= 0 or int(amount)> 1000000000:
           return 2
       else:
        base_currency = str(base).upper()
        endpoint = 'latest'
        symbol1 = str(symbol1).upper()
        symbol2 = str(symbol2).upper()
        
        self.cur.execute("SELECT 'Symbols' FROM 'CommodityData' WHERE Name=?", (symbol1,))
        commodity1Name = self.cur.fetchone()
        print(commodity1Name)
        self.cur.execute("SELECT 'Symbols' FROM 'CommodityData' WHERE Name=?", (symbol2,))
        commodity2Name = self.cur.fetchone()
        print(commodity2Name)
        self.cur.execute("SELECT 'Symbols' FROM 'CommodityData' WHERE Name=?", (base_currency,))
        baseName = self.cur.fetchone()
        print(baseName)
        if baseName==None or  commodity1Name == None or commodity2Name == None:
            print('bad symbols')
            return 0
        else:
            
            resp = requests.get('https://commodities-api.com/api/'+endpoint+'?access_key='+self.access_key+'&base='+base_currency+'&symbols='+symbol1+","+symbol2)
            if resp.status_code != 200:
             # This means something went wrong.
                return -1
            else:
                response = resp.json()
                #print(response)
                #print(response['data']['rates']['USD'])
                #print(response['data']['rates'][symbol2])
                #print(response['data']['rates'][symbol1])
                exchangeRate = response['data']['rates'][symbol2]/response['data']['rates'][symbol1]
                exchangeAmount = exchangeRate * float(amount)
                exchangeAmount = f'{exchangeAmount:.2f} {symbol2} for {amount} {symbol1}'
                exchangeRate = f'{exchangeRate:.2f} {symbol2} per {symbol1}'
                exchangeData = {}
                exchangeData['exchangeAmount'] = exchangeAmount
                exchangeData['exchangeRate'] = exchangeRate
                print(exchangeData)
                return exchangeData
    def get_top_ten(self, symbols):
        endpoint = 'latest'
        base_currency = 'usd'
        symbols = ",".join(symbols)
        print(symbols)
        resp = requests.get('https://commodities-api.com/api/'+endpoint+'?access_key='+self.access_key+'&base='+base_currency+'&symbols='+symbols)
        if resp.status_code != 200:
         # This means something went wrong.
           return -1
        else:
            response = resp.json()
            for key, value in response['data']['rates'].items():
               newValue = 1/value
               response['data']['rates'][key] = f'${newValue:.2f}'
            print(response['data']['rates'])
            return response['data']['rates']