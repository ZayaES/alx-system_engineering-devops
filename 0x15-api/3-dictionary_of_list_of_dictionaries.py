#!/usr/bin/python3
"""exports the json data from api to csv format"""

import json
import requests


if __name__ == "__main__":
    users = requests.get(
            'https://jsonplaceholder.typicode.com/users/').json()
    total = 0
    completed = 0
    y = 0
    data = {}
    u_todo = requests.get('https://jsonplaceholder.typicode.com/todos/')
    todo = u_todo.json()
    test = {}
    id_count = 1

    for user in users:
        t_data = []
        for x in range(0, len(u_todo.json())):
            task_data = {}
            if todo[x]['userId'] == id_count:
                task_data = {
                        "username": str(user['username']),
                        "task": str(todo[x]['title']),
                        "completed": (todo[x]['completed'])
                        }
                t_data.append(task_data)
        id_count += 1
        data[user['id']] = t_data

    filepath = "todo_all_employees.json"
    json_data = json.dumps(data)

    with open(filepath, mode='w') as json_file:
        json_file.write(json_data)
