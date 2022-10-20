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
import json
import uuid 
app = Flask(__name__)
print("Flask running")
db = Transmission()
hostEmail = Email()
userSignupDict = {}

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
        db.insert_user(user)
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
    id = requestJson[id]
    userports = db.search_portfolio_by_userID(id)
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

@app.route('/makeNewPortfolio', methods=['POST'])
def makeNewPortfolio():
    requestJson = request.get_json()
    name = requestJson[name]
    id = requestJson[id]
    funds = requestJson[funds]
    port = Portfolio(name, str(uuid.uuid4()), id, funds, [], [], [])
    db.insert_porfolio(port)
    user = db.search_user_by_id(id)
    user.add_portfolio(port.id)
    user.update_portfolios()
    data = {
        "returncode": "0"
    }
    return data
