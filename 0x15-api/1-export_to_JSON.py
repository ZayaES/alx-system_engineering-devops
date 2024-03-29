#!/usr/bin/python3
"""exports the json data from api to csv format"""

import requests
import sys


if __name__ == "__main__":
    id_ = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    total = 0
    completed = 0
    y = 0
    data = {'"{}": []'.format(id_)}
    t_data = []

    u_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    for x in range(0, len(u_todo.json())):
        if ((u_todo.json()[x]['userId']) == int(id_)):
            t_data.append(
                    '{"task": "{}", \
                    "completed": {}, "username": "{}"}'.format(
                u_todo.json()[x]['title'],
                u_todo.json()[x]['completed'],
                user.json()['username']))
            data['{}'.format(id_)].append(t_data)
            if total == 0:
                y = x
            total += 1
            if (u_todo.json()[x]['completed'] is True):
                completed += 1
    print(t_data)
    print(data)
"""    filepath = "{}.csv".format(id_)

   with open(filepath, mode='w') as csv_file:
        for x in range(y, y + total):
            csv_file.write('"{}","{}","{}","{}"\n'.format(
                str(id_), str(user.json()['username']),
                str(u_todo.json()[x]['completed']),
                str(u_todo.json()[x]['title'])))


    with open """
