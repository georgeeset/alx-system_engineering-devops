#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":

    users = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'
        .format(sys.argv[1])
    )

    todo_list = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'
        .format(sys.argv[1])
    )

    users_json = users.json()
    todos_json = todo_list.json()

    # holds list of todo formated in json
    todo_list = []

    # create rows and populate json file
    for todo in todos_json:
        td = {}
        td["task"] = todo.get("title")
        td["completed"] = todo.get("completed")
        td["username"] = users_json.get("username")
        todo_list.append(td)
        dict = {sys.argv[1]: todo_list}
        with open('{}.json'.format(sys.argv[1]), 'w') as jsonfile:
            json.dump(dict, jsonfile)
