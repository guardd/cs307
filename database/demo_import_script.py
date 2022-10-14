from re import S
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
from Trade import Trade

db = Transmission()
print(IDCreation.generate_ID())
userOne = User(IDCreation.generate_ID(), "userOne", "onePassword", "one@email.com", 10428, "M", [])
db.insert_user(userOne)
userTwo = User(IDCreation.generate_ID(), "userTwo", "twoPassword", "two@email.com", 104281, "f", [])
db.insert_user(userTwo)
print(userOne)
trade = Trade(userOne.id)
print(trade)
trade.create_new_portfolio("portfolioOne", 1000)
trade.create_new_portfolio("portfolioTwo", 500)
trade.buy_stock("PEP", userOne.get_userPortfolios()[0].get_id(), 5)
trade.sell_stock(userOne.get_userPortfolios()[0].get_stocks()[0].get_id(), 2)