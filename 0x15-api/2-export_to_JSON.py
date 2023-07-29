#!/usr/bin/python3
"""exports the json data from api to csv format"""

import json
import requests
import sys


if __name__ == "__main__":
    id_ = sys.argv[1]
    user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(id_))
    total = 0
    completed = 0
    y = 0
    data = {}
    t_data = []

    u_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo = u_todo.json()

    for x in range(0, len(u_todo.json())):
        if ((todo[x]['userId']) == int(id_)):
            task_data = {
                    "task": str(todo[x]['title']),
                    "completed": str(todo[x]['completed']),
                    "username": str(user.json()['username'])
                    }
            t_data.append(task_data)
            data[id_] = t_data
            if total == 0:
                y = x
            total += 1
            if (u_todo.json()[x]['completed'] is True):
                completed += 1

    filepath = "{}.json".format(id_)
    json_data = json.dumps(data)

    with open(filepath, mode='w') as json_file:
        json_file.write(json_data)
