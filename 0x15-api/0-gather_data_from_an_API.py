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
    done = []
    total = len(todos)
    for todo in todos:
        if todo.get("completed") is True:
                done.append(todo.get("title"))
    text = "Employee {} is done with tasks({}/{}):"
    print(text.format(user.get("name"), len(done), total))
    for todo in done:
        print("\t {}".format(todo))
