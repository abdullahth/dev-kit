# Importing Statments
import os
import threading as th
import json

USER_PATH = """user.json"""
USER_PATH = os.path.join(os.path.dirname(__file__), USER_PATH)


class User:
    '''With Methods that Returns the User's Data'''
    def __init__(self, include_repo= False):
        if not os.path.exists(USER_PATH):
            SignUp()
        else:
            with open(USER_PATH) as data:
                self.Data = json.load(data)
                self.username = self.Data['Username']
                self.password = self.Data['Password']
                if include_repo == True:
                    self.repo = self.Data['Repos']


class SignUp:
    # Will be initilaized later
    '''Sign Up to the App'''
