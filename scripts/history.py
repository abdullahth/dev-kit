# Join Parent Dirctory
import sys
import os
import inspect
directory = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent = os.path.dirname(directory)
sys.path.insert(0, parent)

import user

current = user.User()
current = current.repos()

if len(current[0]) == 0:
    print('You have not created any repositories yet.')
    print('You can create one by: create <Repositry Name>')
else:
    for name, date in zip(current[0], current[1]):
        print('Repository Name: ', name, ' | Created in: ', date)
