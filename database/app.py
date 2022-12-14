from Transmission import Transmission
from User import User
from Portfolio import Portfolio
from Property import Property
from Stock import Stock
import tax
from flask import Flask, request, jsonify
from Email import Email
from notifications import Notifications
from Commodity import Commodity
from IDCreation import IDCreation
import StockData
from Friend import Friend
from CommodityData import CommodityData
from Trade import Trade
import json
import uuid
import prediction
from twisted.internet import task, reactor
import sched, time
import stockChangeList

app = Flask(__name__)
print("Flask running")
db = Transmission()
#hostEmail = Email()
userSignupDict = {}
userDaytradeDict = {}
userDaytradeCountDict = {}
s = sched.scheduler(time.time, time.sleep)  
#code = hostEmail.send_email_verify_email(email)
#userSignupDict.update({code: [username, password, email]})
secs_in_day = 86400
secs_in_week = 604800.0

def reset_dayTrade():
    userDaytradeDict = {}
    s.enter(secs_in_day , 1, reset_dayTrade, ())

s.enter(secs_in_day , 1, reset_dayTrade, ())
#userDaytradeDict format: 
#{stock: [portid, buy / sell]}
#if different buy sell add count to id remove stock
#userDaytradeCountDict format:
#{id: [counts, [remove_dates]]}
#l = task.LoopingCall(reset_dayTrade)
#l.start(secs_in_day)

#userDaytradeCountDict format:
#{id: count}
#schedule a -1 1 week later whenever a +1 happens
#format
#s = sched.scheduler(time.time, time.sleep)  
def reduce_dayTrade(portid):
    if portid in userDaytradeCountDict:
        userDaytradeCountDict[portid] = userDaytradeCountDict[portid] - 1

#s = sched.scheduler(time.time, time.sleep)
#reactor.run()
#return values:
#1 = is day trade
#2 = not Daytrade
#3 = daytrade and rejected
#4 = daytrade and over 25000
def dayTradeCheck(portid, stock, buySell):
    print(userDaytradeCountDict)
    print(userDaytradeDict)
    if stock in userDaytradeDict:
        if userDaytradeDict[stock][1] != buySell:
            #is a daytrade
            if portid in userDaytradeCountDict:
                if userDaytradeCountDict[portid] == 4:
                    #need to intervene
                    port = db.search_portfolio_by_id(portid)
                    if port.funds > 25000:
                        userDaytradeCountDict.update({portid: userDaytradeCountDict[portid] + 1})
                        s.enter(secs_in_week, 1, reduce_dayTrade, (portid))
                        del userDaytradeDict[stock]
                        return 4
                    else:
                        return 3
                else:
                    userDaytradeCountDict.update({portid: userDaytradeCountDict[portid] + 1})
                    s.enter(secs_in_week, 1, reduce_dayTrade, (portid))
                    del userDaytradeDict[stock]
                    return 1
            else:
                userDaytradeCountDict.update({portid: 1})
                s.enter(secs_in_week, 1, reduce_dayTrade, (portid))
                del userDaytradeDict[stock]
                return 1
        else:    
            return 2
    else:
        userDaytradeDict.update({stock: [portid, buySell]})
        return 2
@app.route('/getCompanyData', methods=['POST'])
def get_company_data():
  requestJson = request.get_json()
  stockABV = requestJson['stockABV']
  dateRange = requestJson['dateRange']
  
  print(stockABV)
  print(dateRange)
  
  companyData=StockData.pull_company_data(stockABV, dateRange)
  companyName = StockData.get_company_name(stockABV)
  financialMarkers = StockData.pull_financial_markers(stockABV)
  if companyData == -1 or financialMarkers == -1:
        data={"returncode": "-1" }
 
  else:
    


    data = {
         "returncode": "0",
     
         "companyName": companyName,
         "companyData": companyData,
         "financialMarkers": financialMarkers

    }
    print(data)
  return data
@app.route('/getSortStock', methods=['POST'])
def get_sort_stock():
  requestJson = request.get_json()
  sortType = requestJson['sortType']
  ascdesc = requestJson['ascdesc']
  
  print(sortType)
  print(ascdesc)
  StockData.update_stock_info()
  if ascdesc == 'asc':
    sortedStocks = StockData.pull_top_stocks(sortType)
  elif ascdesc == 'desc':
    sortedStocks = StockData.pull_top_stocks_desc(sortType)
  else:
      return -1
  if sortedStocks == -1:
        data={"returncode": "-1" }
  elif sortedStocks == 0:
      data={"returncode": "0"}
  elif str(sortType) == 'Industry':
      data={"returncode": "1",
            "topIndustryTable": sortedStocks
            }
  else:
    stockABV = []
    stockName = []
    stockSortedBy = []

    for x in range(sortedStocks.__len__()):
        

            stockABV.append(str(sortedStocks[x][0]))
            stockName.append(str(sortedStocks[x][1]))
            stockSortedBy.append(str(sortedStocks[x][2]))
 


    data = {
         "returncode": "2",
     
         "stockABV": stockABV,
         "stockName": stockName,
         "stockSortedBy": stockSortedBy

    }
    print(data)
  return data
@app.route('/getNews', methods=['POST'])
def get_news():
  requestJson = request.get_json()
  userID = requestJson['uid']
  print(userID)
  newsPackage = StockData.get_news(userID)
  if newsPackage == -1:
        data={"returncode": "-1" }
  else:
    newstitles = []
    newspublishers = []
    newsurls = []

    for x in range(newsPackage[0].__len__()):
        newstitles.append(newsPackage[x+1]['title'])
        newspublishers.append(newsPackage[x+1]['publisher'])
        newsurls.append(newsPackage[x+1]['link'])
 


    data = {
         "retruncode": "0",
         "number": newsPackage[0].__len__(),
         "stocks": newsPackage[0],
         "newstitles": newstitles,
         "newspublishers": newspublishers,
         "newsurls": newsurls

    }
    print(data)
  return data
@app.route('/exchangeRate', methods=['POST'])
def get_exchange_rate():
    requestJson = request.get_json()
    symbol1 = requestJson['symbol1']
    symbol2 = requestJson['symbol2']
    base = requestJson['base']
    amount = requestJson['amount']
    CD = CommodityData()
    exchangeData = CD.get_commodity_exchange_rate(symbol1, symbol2, base, amount)
    if exchangeData ==-1:
        data = {
            "returncode": "-1"
        }
    elif exchangeData == 0:
        data = {
            "returncode": "0"
        }
    elif exchangeData == 2:
        data = {
            "returncode": "2"
        }
    else:
        data = {
            "returncode": "1",
            "exchangeRate": exchangeData['exchangeRate'],
            "exchangeAmount": exchangeData['exchangeAmount']
        }

    return data
@app.route('/topTenRefresh', methods=['POST'])
def get_top_ten():
    requestJson = request.get_json()
    symbols = []
    
    for x in range(10):
        
        iterator = f'symbol{x+1}'
        symbols.append(requestJson[iterator])
        
    CD = CommodityData()

    topTenRefreshData = CD.get_top_ten(symbols)

    if topTenRefreshData ==-1:
        data = {
            "returncode": "-1"
        }
    else:
        data = {
            "returncode": "1",
             "rates":topTenRefreshData
        }
        print(data)
    return data
@app.route('/loginMethod', methods=['POST'])
def get_login_test():
    print(request.is_json)
    requestJson = request.get_json()
    print(json.dumps(requestJson))
    username = requestJson['username']
    password = requestJson['password']
    user = db.login_sequence(username, password)
    try:
        data = {
            "returncode": "1",
            "id": user.get_id()
        }
    except AttributeError:
        data = {
            "returncode": "-1"
        }
    return data

@app.route('/userSignup', methods=['POST'])
def user_signup_check():
    #todo : check username, then send email
    #code : -1 = duplicate username
    requestJson = request.get_json()
    username = requestJson['username']
    email = requestJson['email']
    password = requestJson['password']
    if (db.search_user_by_username(username) != -1):
        data = {
            "returncode": -1
        }
        return data
    if (db.search_user_by_email(email) != -1):
        data = {
            "returncode": -2
        }
        return data    
    code = hostEmail.send_email_verify_email(email)
    userSignupDict.update({code: [username, password, email]})
    data = {
        "returncode": 1
    }
    return data

@app.route('/emailVerification', methods=['POST'])
def user_signup_complete():
    requestJson = request.get_json()
    print(userSignupDict)
    code = requestJson['code']
    if code in userSignupDict:
        #sign up user
        user = User(str(uuid.uuid4()), userSignupDict[code][0], userSignupDict[code][1], userSignupDict[code][2], 1, "TODO", [])
        friend = Friend(user.id, [], [], [])
        db.insert_user(user)
        db.insert_friend(friend)
        data = {
            "returncode": 1
        }
        del userSignupDict[code]
    else:
        data = {
            "returncode": -1
        }
    db.save() 
    return data


@app.route('/userDataRequest', methods=['POST'])
def user_data_request():
    requestJson = request.get_json()
    id = requestJson['id']
    if (db.search_user_by_id(id) != -1):
        user = db.search_user_by_id(id)
        data = {
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "dateofbirth": user.dateofbirth,
            "genderID": user.genderID,
            "returncode": 1
        }
    else:
        data = {
            "returncode": -1
        }
    return data
@app.route('/deleteProfile', methods=['POST'])
def user_delete():
    requestJson = request.get_json()
    id = requestJson['id']
    if (db.remove_user(id) != -1):
        data = {
            "returncode": 1
        }
    else:
        data = {
            "returncode": 0
        }
    return data
    
@app.route('/passwordRecovery', methods=['POST'])
def password_recovery():
    requestJson = request.get_json()
    email = requestJson['email']
    if (db.search_user_by_email(email) != -1):
        hostEmail.send_password_recovery_email(db.search_user_by_email(email))
        data = {
            "returncode": 0
        }
    else:
        data = {
            "returncode": -1
        }
    return data    

@app.route('/usernameChange', methods=['POST'])
def username_change():
    requestJson = request.get_json()
    id = requestJson['id']
    changeUsername = requestJson['changeUsername']
    if (db.search_user_by_username(changeUsername) == -1):
        user = db.search_user_by_id(id)
        user.change_username(changeUsername, id)
        data = {
            "returncode": "0"
        }
    else:
        data = {
            "returncode": "-1"
        }
    return data


@app.route('/passwordChange', methods=['POST'])
def password_change():
    requestJson = request.get_json()
    id = requestJson['id']
    changePassword = requestJson['changePassword']
    user = db.search_user_by_id(id)
    user.change_password(changePassword, id)
    data = {
        "returncode": "0"
    }
    return data

@app.route('/bugReport', methods=['POST'])
def bug_report():
    requestJson = request.get_json()
    name = requestJson['name']
    email = requestJson['email']
    problem = requestJson['problem']
    db.insert_bug_report(name, email, problem)
    data = {
        "returncode": 0
    }
    return data

@app.route('/getUserPortfolios', methods=['POST'])
def userPortfolios():
    requestJson = request.get_json()
    id = requestJson['id']
    userports = db.search_portfolio_by_userId(id)
    howmany = len(userports)
    portnames = []
    portids = []
    data = {}
    data['size'] = howmany
    for port in userports:
        portnames.append(port.name)
        portids.append(port.id)
    data["portnames"] = portnames
    data["portids"] = portids
    return data

@app.route('/getComPrediction', methods=['POST'])
def getComPrediction():
    requestJson = request.get_json()
    symbol = requestJson['symbol']
    stockdata = prediction.get_commodity(symbol)
    data = {}
    i = 1
    for point in stockdata:
        obj = {"date": point[0], "price": point[1]}
        data[i] = obj
        i = i + 1
    print(data)
    data[0] = i-1
    return data

@app.route('/getPredictions', methods=['POST'])
def getPredictions():
    requestJson = request.get_json()
    projectABV = requestJson['projectABV']
    days = requestJson['days']
    stockdata = prediction.pullStockData(projectABV, days)
    data = {}
    i = 1
    for point in stockdata:
        
        
        obj = {"date": point[0], "close": point[1]}
        data[i] = obj
       
        i = i + 1
    print(data)
    data[0] = i-1
    return data

@app.route('/getPredictionsFinal', methods=['POST'])
def getPredictionsFinal():
    requestJson = request.get_json()
    projectABV = requestJson['projectABV']
    stockdata = prediction.find_prediction(projectABV)
    data = {}
    i = 0
    for point in stockdata:      
        obj = {"date": point[0], "close": point[1]}
        data[i] = obj      
        i = i + 1
    return data

@app.route('/getComPredictionFinal', methods=['POST'])
def getComPredictionsFinal():
    requestJson = request.get_json()
    symbol = requestJson['symbol']
    stockdata = prediction.commodity_prediction(symbol)
    data = {}
    i = 0
    for point in stockdata:      
        obj = {"date": point[0], "price": point[1]}
        data[i] = obj      
        i = i + 1
    return data

@app.route('/getReccomendations', methods=['POST'])
def getReccomendations():
    requestJson = request.get_json()
    db = requestJson['projectABV']
    data = prediction.generate_risk(db)
    obj = {"risk_score": data[0], "recomendation": data[1]}
    return obj

@app.route('/makeNewPortfolio', methods=['POST'])
def makeNewPortfolio():
    requestJson = request.get_json()
    name = requestJson['name']
    id = requestJson['id']
    funds = requestJson['funds']
    user = db.search_user_by_id(id)
    names = []
    for single in user.userPortfolios:
        names.append(db.search_portfolio_by_id(single).name)
    if name in names:
        data = {
        "returncode": "-1"
        }
        return data
    port = Portfolio(name, str(uuid.uuid4()), id, funds, [], [], [])
    db.insert_portfolio(port)

    user.add_portfolio(port)
    user.update_portfolios()
    db.save() 
    data = {
        "returncode": "0"
    }
    return data

@app.route('/getPortfolioData', methods=['POST'])
def getPortfolioData():
    #sd = StockData()
    requestJson = request.get_json()
    id = requestJson['id']
    port = db.search_portfolio_by_id(id)
    stocks = port.stocks
    data = {}
    i = 1
    total = port.funds
    for stockid in stocks:
        stock = db.search_stock_by_id(stockid)
        weight = StockData.get_price(stock.nameABV) * stock.shares
        total = total + weight
        obj = {"stockABVs": stock.nameABV,
        "stockids": stock.id,
          "stockAmount": stock.shares,
          "stockColor": stock.color,
           "stockPrices": StockData.get_price(stock.nameABV),
            "stockWeight": weight}
        #print(StockData.get_price(stock.nameABV) * stock.shares)
        data[i] = obj 
        i = i + 1
    data[0] = {"size": i, "funds": port.funds, "total": total}
    return data

@app.route('/buyStock', methods=['POST'])
def buyStock():
    requestJson = request.get_json()
    uid = requestJson['uid']
    print(uid)
    id = requestJson['id']
    nameABV = requestJson['nameABV']
    shares = requestJson['shares']
    port = db.search_portfolio_by_id(id)
    #daycheck = dayTradeCheck(id, )
    #trade = Trade()
    ret = buy_stock_trade(uid, nameABV, id, int(shares))
    stockid = db.search_stock_by_nameABV_and_userId(nameABV, uid)
    
    data = {
        "returncode": str(ret)
    }
    return data

@app.route('/sellStock', methods=['POST'])
def sellStock():
    requestJson = request.get_json()
    uid = requestJson['uid']
    id = requestJson['id']
    
    nameABV = requestJson['nameABV']
    shares = requestJson['shares']
    print(nameABV)
    print(uid)
    #port = db.search_portfolio_by_id(id)
    stock = db.search_stock_by_nameABV_and_userId(nameABV, uid)
    if stock == -1:
        return {
            "returncode": "-4"
        }
    sid = stock.id
    #for each in port.stocks:
    #    if db.search_stock_by_id(each).nameABV == nameABV:
    #        sid = each

    #trade = Trade()
    ret = sell_stock_trade(uid,sid, int(shares), id)
    data = {
        "returncode": str(ret)
    }
    return data

@app.route('/sharePortfolio', methods=['POST'])
def sharePort():
    requestJson = request.get_json()
    friendId = requestJson['friendId']
    portfolioName = requestJson['portfolioName']
    uid = requestJson['uid']
    toShare = db.search_portfolio_by_name_and_id(portfolioName, uid)
    trade = Trade()
    if toShare == -1:
        return {
            'returncode': -2
        }
    data = {
        'returncode': trade.share_portfolio(friendId, toShare)
    }
    return data



@app.route('/deleteFriend', methods=['POST'])
def deleteFriend():
    requestJson = request.get_json()
    friendId = requestJson['friendId']
    uid = requestJson['uid']
    userFriend = db.search_friend_by_id(uid)
    otherFriend = db.search_friend_by_id(friendId)
    userFriend.remove_friend(friendId)
    otherFriend.remove_friend(uid)
    userFriend.update_friends()
    otherFriend.update_friends()
    data = {
        "returncode": 1
    }
    return data
# How ADDING Friends should work
# Add friend by username
# case : username doesn't exist / fail return code -1
# case : already sent request / fail return code -2
# then, case : push in friend request in other user return code 1
# Other user can see this, can accept BY : SAME CALL, JUST THE USERNAME WILL BE THE OPPOSITE
# that way we can avoid the case where both user sends to each other and not being added
# therefore :
# case : the other user that we are about to send a request to is already in my friendrequest / GET THEM BOTH IN FRIEND CATEGORY return code 2
@app.route('/addFriend', methods=['POST'])
def addFriend():
    requestJson = request.get_json()
    #what json should have : id (of the user), username (of the person the user is adding)
    userId = requestJson['userId']
    userFriend = db.search_friend_by_id(userId)
    otherUsername = requestJson['otherUsername']
    otherUserId = db.search_user_by_username(otherUsername)
    if (otherUserId == -1):
        data = {
            "returncode": -1
        }
        return data
    otherFriend = db.search_friend_by_id(otherUserId.get_id())
    try:
        otherFriend.friendRequests.index(userId)
        data = {
            "returncode": -2
        }
        return data
    except ValueError:
        print("addFriend No error!")
    try:
        print(otherUserId.get_id())
        index = userFriend.friendRequests.index(otherUserId.get_id())

        ## make them friends
        userFriend.remove_friend_request(otherUserId.get_id())

        userFriend.add_friend(otherUserId.get_id())

        otherFriend.add_friend(userId)

        userFriend.update_friend_requests()

        userFriend.update_friends()

        otherFriend.update_friends()

        data = {
            "returncode": 2
        }
        return data
    except ValueError:
        ##send request
        if userId in otherFriend.get_friends():
            data = {
            "returncode": -2
            }
            return data
        otherFriend.add_friend_request(userId)
        otherFriend.update_friend_requests()
        data = {
            "returncode": 1
        }
        return data
    
@app.route('/getFriends', methods=['POST'])
def userFriends():
    requestJson = request.get_json()
    id = requestJson['id']
    friend = db.search_friend_by_id(id)
    
    
    friendRequests = []
    friendRequestNames = []
    friendNames = []
    friendIds = []
    data = {}
    friendRequestSize = 0
    friendSize = 0
    for friendRequest in friend.friendRequests:
        if (db.search_user_by_id(friendRequest) == -1):
            friend.remove_friend_request(friendRequest)
            print("user gone, removed friend request")
            friend.update_friend_requests()
        else:
            friendRequests.append(friendRequest)
            friendRequestNames.append(db.search_user_by_id(friendRequest).get_username())
            friendRequestSize = friendRequestSize + 1
    for indfriend in friend.friends:
        if (db.search_user_by_id(indfriend) == -1):
            friend.remove_friend(indfriend)
            print("user gone, removed friend")
            friend.update_friends()
        else:    
            friendIds.append(indfriend)
            friendNames.append(db.search_user_by_id(indfriend).get_username())
            friendSize = friendSize + 1
    data["friendRequests"] = friendRequests
    data["friendRequestNames"] = friendRequestNames
    data["friendNames"] = friendNames
    data["friendIds"] = friendIds
    data["friendRequestSize"] = friendRequestSize
    data["friendSize"] = friendSize
    return data
    
@app.route('/textFriend', methods=['POST'])
def textFriend():
    requestJson = request.get_json()
    id = requestJson['id']
    friendId = requestJson['friendId']
    msg = requestJson['msg']
    friend = db.search_friend_by_id(id)
    try:
        index = friend.friends.index(friendId)
        otherfriend = db.search_friend_by_id(friendId)
        if (otherfriend == -1):
            #friend nonexistant
            data = {
            "returncode": -2
            }
            return data
        toSend = db.search_user_by_id(id).get_username() + ":" + msg
        #toSend.append(":")
        #toSend.append(msg)
        otherfriend.add_message(toSend)
        otherfriend.update_messages()
        #message sent!
        data = {
            "returncode": 1
        }
        return data
    except ValueError:
        #not friend
        data = {
            "returncode": -1
        }
        return data

@app.route('/textGet', methods=['POST'])
def textGet():
    requestJson = request.get_json()
    print(requestJson)
    id = requestJson['id']
    friend = db.search_friend_by_id(id)

    returnArray = friend.pop_messages()

    returnString = ""
    for each in returnArray:
        returnString = returnString + each + "\n"
        #returnString.append("\n")
    data = {
        "msgs": returnString
    }
    return data

def buy_stock_trade(uid, nameABV, portfolioID, shares):
     p = db
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
            print(uid)
            stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, uid, StockData.get_price(nameABV), shares, IDCreation.generate_color_hex())
            daytrade = dayTradeCheck(portfolioID, stock.id, 1)
            if daytrade == 3:
                 return -4
            print(stock.userID)
            p.insert_stock(stock)
            portfolio.add_stock(stock)
            portfolio.update_stocks(portfolio.get_stocks(), portfolioID)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     elif stock.get_portfolioID() != portfolioID:
            
      stock = Stock(StockData.get_company_name(nameABV), nameABV, IDCreation.generate_ID(), portfolioID, uid, StockData.get_price(nameABV), shares, IDCreation.generate_color_hex())
      daytrade = dayTradeCheck(portfolioID, stock.id, 1)
      if daytrade == 3:
        return -4
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
            daytrade = dayTradeCheck(portfolioID, stock.id, 1)
            if daytrade == 3:
                 return -4
            currentShares = stock.get_shares()
            stock.update_stockShares(currentShares + shares)
            newAvgSharePrice = ((currentShares * stock.get_avgSharePrice()) + (shares * StockData.get_price(nameABV)))/(shares+currentShares)
            stock.update_stockAvgSharePrice(newAvgSharePrice, stock.id)
            portfolio.update_funds(portfolio.get_funds()-price, portfolioID)
     return 1

def sell_stock_trade(uid, stockID,shares, portID):
        t = db
        stock = t.search_stock_by_id(stockID)
        portfolio = t.search_portfolio_by_id(stock.get_portfolioID())
        if stock==-1 or portfolio==-1:
            return -1 ## this will indicate no stock or portfolio by that ID found
        elif stock.get_userID()!=uid:
            print(stock.get_userID())
            print(uid)
            return -4 ## this will indicate stock does not belong to user
        else:
            daytrade = dayTradeCheck(portID, stock.id, 0)
            if daytrade == 3:
                return -5
            if shares == stock.get_shares():
             portfolio.set_funds(portfolio.get_funds()+(stock.get_shares()*StockData.get_price(stock.get_nameABV())))
             portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
             t.remove_stock(stockID)
             portfolio.remove_stock(stock)
             portfolio.update_stocks(portfolio.get_stocks(),portfolio.get_id())
             return 1            
            elif shares < stock.get_shares():
                portfolio.set_funds(portfolio.get_funds()+(shares*StockData.get_price(stock.get_nameABV())))
                portfolio.update_funds(portfolio.get_funds(), portfolio.get_id())
                stock.set_shares(stock.get_shares()-shares)
                stock.update_stockShares(stock.get_shares())
                return 1
            else:
                return -2

@app.route('/getPercentageList', methods=['POST'])
def getPercentageList():
    requestJson = request.get_json()
    abvs = requestJson['abvs']
    percentage = 0
    downup = -1
    print(requestJson['percentage'])
    print(requestJson['downup'])
    if requestJson['percentage'] == "":
        requestJson['percentage'] = '0' 
    try:
        percentage = int(requestJson['percentage'])
    except ValueError:
        return {
            "size": -1
        }

    try:
        downup = int(requestJson['downup'])
    except ValueError:
        return {
            "size": -2
        }    
    if not (downup == 0 or downup == 1):
        return {
            "size": -2
        }
     

    return stockChangeList.percentage_change_list(percentage, downup, abvs)

    
@app.route('/getTax', methods=['POST'])
def getTax():
    requestJson = request.get_json()
    amount = requestJson['amount']
    state = requestJson['state']
    print(amount)
    print(state)
    return {
        "taxPercentage" : tax.findTaxRate(state, amount),
        "taxAmount": tax.calculateValue(state, amount)
    }
