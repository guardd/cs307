from User import User
class Notifications:
    def __init__(self, id, code, name, text, user):
        self.id = id #INTEGER PRIMARY KEY
        self.userid = user.get_id() #INTEGER links to user
        self.code = code #INTEGER #code to label event
        self.name = name #TEXT, name of event that created notifications : ex, account created, password change, stock price change
        self.text = text #TEXT

    def get_id(self):
        return self.id

    def get_userid(self):
        return self.userid

    def get_code(self):
        return self.code

    def get_name(self):
        return self.name

    def get_text(self):
        return self.text

#we woudln't need to modify the notification after making them, so only getter methods

#what kind of events are we going to have?
