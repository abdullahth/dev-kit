# Importing Statments
import os
import threading as th
import json

USER_PATH = "./user.json"


class User:
    '''With Methods that Returns the User's Data'''
    
    def __init__(self):
        if not os.path.exists(USER_PATH):
            SignUp()
        else:
            with open(USER_PATH) as data:
                self.Data = json.load(data)
        
    def username(self):
        return str(self.Data['Username'])
    
    def password(self):
        return str(self.Data['Password'])



class SignUp:
    # Will be initilaized later
    '''Sign Up to the App'''
    pass