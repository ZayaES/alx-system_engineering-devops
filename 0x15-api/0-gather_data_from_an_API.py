#!/usr/bin/python3
"""Gathers data from an API"""

import requests
import sys


if __name__ == "__main__":
    id_ = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    total = 0
    completed = 0
    y = 0

    u_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    for x in range(0, len(u_todo.json())):
        if ((u_todo.json()[x]['userId']) == int(id_)):
            if total == 0:
                y = x
            total += 1
            if (u_todo.json()[x]['completed'] is True):
                completed += 1

    print("Employee {} is done with tasks({}/{}):".format(
            user.json()['name'], completed, total))
    for x in range(y, y + total):
        if ((u_todo.json()[x]['completed']) is True):
            print("\t {}".format(u_todo.json()[x]['title']))
