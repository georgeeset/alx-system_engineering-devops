#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""

import csv
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

    # create roes and populate csv file
    with open('{}.csv'.format(sys.argv[1]), 'w') as csvfile:
        todowriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for todo in todos_json:
            todowriter.writerow([todo.get('userId'),
                                 users_json.get('username'),
                                 todo.get('completed'),
                                 todo.get('title')])
