from Transmission import Transmission
from User import User
from Portfolio import Portfolio
from Property import Property
from Stock import Stock
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
app = Flask(__name__)
print("Flask running")
db = Transmission()
#hostEmail = Email()
userSignupDict = {}
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

@app.route('/getPredictions', methods=['POST'])
def getPredictions():
    requestJson = request.get_json()
    projectABV = requestJson['projectABV']
    stockdata = prediction.pullStockData(projectABV)
    data = {}
    i = 0
    for point in stockdata:
        
        
        obj = {"date": point[0], "close": point[1]}
        data[i] = obj
       
        i = i + 1
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
    print(prediction.generate_risk(stockdata))
    return data



@app.route('/makeNewPortfolio', methods=['POST'])
def makeNewPortfolio():
    requestJson = request.get_json()
    name = requestJson['name']
    id = requestJson['id']
    funds = requestJson['funds']
    port = Portfolio(name, str(uuid.uuid4()), id, funds, [], [], [])
    db.insert_portfolio(port)
    user = db.search_user_by_id(id)
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
    for stockid in stocks:
        stock = db.search_stock_by_id(stockid)
        obj = {"stockABVs": stock.nameABV,
        "stockids": stock.id,
          "stockAmount": stock.shares,
          "stockColor": stock.color,
           "stockPrices": StockData.get_price(stock.nameABV),
            "stockWeight": StockData.get_price(stock.nameABV) * stock.shares}
        #print(StockData.get_price(stock.nameABV) * stock.shares)
        data[i] = obj 
        i = i + 1
    data[0] = {"size": i, "funds": port.funds}
    return data

@app.route('/buyStock', methods=['POST'])
def buyStock():
    requestJson = request.get_json()
    uid = requestJson['uid']
    id = requestJson['id']
    nameABV = requestJson['nameABV']
    shares = requestJson['shares']
    port = db.search_portfolio_by_id(id)
    trade = Trade()
    ret = trade.buy_stock(uid, nameABV, id, int(shares))
    data = {
        "returncode": str(ret)
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
        index = userFriend.friendRequests.index("otherUserId")
        ## make them friends
        userFriend.remove_friend_request(otherUserId)
        userFriend.add_friend(otherUserId)
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
    for friendRequest in friend.friendRequests:
        if (db.search_user_by_id(friendRequest) == -1):
            friend.remove_friend_request(friendRequest)
            print("user gone, removed friend request")
            friend.update_friend_requests()
        else:
            friendRequests.append(friendRequest)
            friendRequestNames.append(db.search_user_by_id(friendRequest).get_username)
    for indfriend in friend.friends:
        if (db.search_user_by_id(indfriend) == -1):
            friend.remove_friend(indfriend)
            print("user gone, removed friend")
            friend.update_friends()
        else:    
            friendIds.append(indfriend)
            friendNames.append(db.search_user_by_id(indfriend).get_username)
    data["friendRequests"] = friendRequests
    data["friendRequestNames"] = friendRequestNames
    data["friendNames"] = friendNames
    data["friendIds"] = friendIds
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
        otherfriend.add_message(db.search_user_by_id(id).get_username + ": " + msg)
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
