import sqlite3
import json

class Friend:
    def __init__(self, id, friendRequests, friends, messages):
        self.id = id #TEXT
        self.friendRequests = friendRequests #TEXT : friend's ID
        self.friends = friends #TEXT : friend's ID
        self.messages = messages #TEXT : format : Text, "Friend : blah blah blah"
        self.connect = sqlite3.connect("mydb.db") ##connects to database
        self.cur = self.connect.cursor()
#        self.notifications = #INTEGER in id
#        self.predictions = #INTEGER in id
    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    
    
    def get_friendRequests(self):
        return self.friendRequests

    def get_friends(self):
        return self.friends    
    
    def add_friend_request(self, id):
        self.friendRequests.append(id)
    
    def remove_friend_request(self, id):
        self.friendRequests.remove(id)

    def add_friend(self, id):
        self.friends.append(id)
    
    def remove_friend(self, id):
        self.friends.remove(id)

    def add_message(self, msg):
        self.messages.append(msg)
    
    def remove_message(self, msg):
        self.messages.remove(msg)
    
    def update_friend_requests(self):
        self.cur.execute("UPDATE 'Friends' SET friendRequests=? WHERE id=?", (json.dumps(self.friendRequests), self.id,))
        self.connect.commit()

    def update_friends(self):
        self.cur.execute("UPDATE 'Friends' SET friends=? WHERE id=?", (json.dumps(self.friends), self.id,))
        self.connect.commit()
    
    def update_messages(self):
        self.cur.execute("UPDATE 'Friends' SET messages=? WHERE id=?", (json.dumps(self.messages), self.id,))
        self.connect.commit()
    
   
    def pop_messages(self):
        returnString = self.messages
        self.messages = []
        self.cur.execute("UPDATE 'Friends' SET messages=? WHERE id=?", (json.dumps(self.messages), self.id,))
        self.connect.commit()
        return returnString