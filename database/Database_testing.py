from Transmission import Transmission
from User import User
from Portfolio import Portfolio
from Property import Property
from Stock import Stock

db = Transmission()
user = User(1, "one", "one", "one@test.com", 10100010, "m", [])
port = Portfolio("portOne", 162761, 1, 500, [], [], [])
stockOne = Stock("Google", "GGL", "thisisausrl", 2168217, 162761, 1, 500, 1)
