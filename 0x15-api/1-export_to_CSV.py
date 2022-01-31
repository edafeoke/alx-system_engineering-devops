#!/usr/bin/python3
'''
for a given employee ID, returns information about his/her TODO list progress
'''

import csv
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(argv[1])).json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        my_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            my_writer.writerow([argv[1], user.get('username'),
                                todo.get('completed'),
                                todo.get('title')])
