# Importing Statments
import os
import threading as th
import json
import pandas as pd

USER_PATH = """dataset/user.json"""
USER_PATH = os.path.join(os.path.dirname(__file__), USER_PATH)

REPOS_PATH = """dataset/repos.csv"""
REPOS_PATH = os.path.join(os.path.dirname(__file__), USER_PATH)

class User:
    '''With Methods that Returns the User's Data'''
    def __init__(self, include_repo= False):
        if not os.path.exists(USER_PATH):
            SignUp()
        else:
            with open(USER_PATH) as self.__data:
                self.Data = json.load(self.__data)
                self.username = self.Data['Username']
                self.password = self.Data['Password']
            if include_repo == True:
                self.repos_df = pd.read_csv(REPOS_PATH, sep=',')

    def save(self, name, date, link):
        with open(REPOS_PATH, 'a') as f:
            f.write('{},{},{}'.format(name, date, link))

class SignUp:
    # Will be initilaized later
    '''Sign Up to the App'''
