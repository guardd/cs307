from Transmission import Transmission
from User import User
from Portfolio import Portfolio
from Property import Property
from Stock import Stock
from flask import Flask, request, jsonify
from Email import Email
from notifications import Notifications
from Commodity import Commodity
import json
app = Flask(__name__)
print("Flask running")
db = Transmission()
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
    print()
