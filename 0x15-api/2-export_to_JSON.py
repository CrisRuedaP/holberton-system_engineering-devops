#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]
    employee_name = requests.get(url + '/users/{}'.format(employee_id)).json()
    amount = requests.get(url + '/todos?userId={}'.format(employee_id)).json()
    name = employee_name.get('username')

    all_tasks = []
    for task in amount:
        records = {}
        records["task"] = task.get("title")
        records["completed"] = task.get("completed")
        records["username"] = name
        all_tasks.append(records)

    data = {}
    data[employee_id] = all_tasks
    filename = '{}.json'.format(employee_id)
    with open(filename, 'w') as file:
        json.dump(data, file)
