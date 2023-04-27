#!/usr/bin/python3
"""
A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    completed_tasks = 0
    tasks_count = 0

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

    # iterate taskst to get completed tasks
    for todo in todos_json:
        if todo.get('completed') is True:
            completed_tasks += 1
        else:
            tasks_count += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(users_json['name'],
                  completed_tasks, tasks_count + completed_tasks
                  )
          )

    for todo in todos_json:
        if todo.get('completed') is True:
            print('\t {}'.format(todo.get('title')))
