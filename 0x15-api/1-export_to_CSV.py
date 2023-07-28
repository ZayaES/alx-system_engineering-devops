#!/usr/bin/python3
"""exports the json data from api to csv format"""

import requests
import sys
import csv


if __name__ == "__main__":
    id_ = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    total = 0
    completed = 0
    y = 0
    data = []

    u_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    for x in range(0, len(u_todo.json())):
        if ((u_todo.json()[x]['userId']) == int(id_)):
            data.append(u_todo.json()[x])
            if total == 0:
                y = x
            total += 1
            if (u_todo.json()[x]['completed'] is True):
                completed += 1

    filepath = "{}.csv".format(id_)

    with open(filepath, mode='w') as csv_file:
        for x in range(y, y + total):
            csv_file.write('"{}", "{}", "{}", "{}"\n'.format(
                id_, user.json()['username'], u_todo.json()[x]['completed'],
                u_todo.json()[x]['title']))
