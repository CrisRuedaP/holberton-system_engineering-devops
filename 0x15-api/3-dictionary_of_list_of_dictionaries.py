#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employees = requests.get(url + '/users/').json()

    for user in employees:
        user_id = user.get('id')
        username = user.get('username')
        amount = requests.get(
            url + '/todos?userId={}'.format(user_id)).json()

    all_tasks = []
    for task in amount:
        records = {}
        records["username"] = username
        records["task"] = task.get("title")
        records["completed"] = task.get("completed")
        all_tasks.append(records)

    data = {}
    data[user_id] = all_tasks
    filename = 'todo_all_employees.json'
    with open(filename, 'w') as file:
        json.dump(data, file)
