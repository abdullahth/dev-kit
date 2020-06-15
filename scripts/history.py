# Importing User File
import sys
import os
import inspect
directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(directory)
sys.path.insert(0, parent)

import user

current = user.User()
current = current.Data

if len(current['Repos']) == 0:
    print('You have not created any repositories yet.')
    print('You can create one by: create <Repositry Name>')
else:
    for repo in current['Repos']:
        repository = current['Repos'][repo]
        print('Repository Name: ', repo, ' | Created in: ', repository['Time'])
        print('You Can Open the Repository by: open <Repository Name>')