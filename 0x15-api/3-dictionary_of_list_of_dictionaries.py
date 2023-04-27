#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""

import json
import requests


if __name__ == "__main__":

    users_json = requests.get(
        'https://jsonplaceholder.typicode.com/users').json()
    dict = {}
    for user in users_json:
        todo_list = []
        todos_json = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id'))).json()
        for todo in todos_json:
            td = {}
            td["task"] = todo.get("title")
            td["completed"] = todo.get("completed")
            td["username"] = user.get("username")
            todo_list.append(td)
        dict[user.get('id')] = todo_list
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(dict, jsonfile)
