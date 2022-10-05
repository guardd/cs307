class Notifications:
    def __init__(self, id, userid, name, text):
        self.id = id #INTEGER PRIMARY KEY
        self.userid = userid #INTEGER links to user
        self.code = code #INTEGER #code to label event
        self.name = name #TEXT, name of event that created notifications : ex, account created, password change, stock price change
        self.text = text #TEXT


#what kind of events are we going to have?
