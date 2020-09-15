#!/usr/bin/python3
"""Dictionary of list of dictionaries"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employees = requests.get(url + '/users/').json()

    data = {}
    filename = 'todo_all_employees.json'
    for user in employees:
        all_tasks = []
        user_id = user.get('id')
        username = user.get('username')
        amount = requests.get(
            url + '/todos?userId={}'.format(user_id)).json()
        for task in amount:
            records = {}
            records["username"] = username
            records["task"] = task.get("title")
            records["completed"] = task.get("completed")
            all_tasks.append(records)
        data[user_id] = all_tasks
    with open(filename, 'w') as file:
        json.dump(data, file)
