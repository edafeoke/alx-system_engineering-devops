#!/usr/bin/python3
'''
for a given employee ID, returns information about his/her TODO list progress
'''

import json
from sys import argv
from urllib.request import urlopen

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos?userId={}'
    url = url.format(argv[1])
    with urlopen(url) as response:
        encoding = response.headers.get_content_charset("utf-8")
        data = response.read()
        data = data.decode(encoding)
        todos = json.loads(data)
        done = 0
        total = len(todos)
        for todo in todos:
            if todo["completed"] is True:
                done += 1
        text = "Employee EMPLOYEE_NAME is done with tasks({}/{}):"
        print(text.format(done, total))
        for todo in todos:
            if todo["completed"]:
                print("\t {}".format(todo["title"]))
