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
    print(user.get_id())
    data = {
        "id": user.get_id()
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
        user = User(str(uuid.uuid4()), userSignupDict[code][0], userSignupDict[code][1], userSignupDict[code][2], 1, "TODO", {})
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
    