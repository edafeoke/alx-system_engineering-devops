#!/usr/bin/python3
'''
for a given employee ID, returns information about his/her TODO list progress
'''

import json
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(argv[1])).json()
    with open('{}.json'.format(argv[1]), 'w', newline='') as jsonfile:
        json.dump({argv[1]: [{
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": user.get("username")} for todo in todos]}, jsonfile)
