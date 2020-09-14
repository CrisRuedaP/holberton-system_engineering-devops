#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv


if __name__ == "__main__":
    """"""
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]
    employee_name = requests.get(url + '/users/{}'.format(employee_id)).json()
    amount = requests.get(url + '/todos?userId={}'.format(employee_id)).json()
    name = employee_name.get('name')

    number_of_done_tasks = []
    total_number_of_tasks = 0
    for task in amount:
        total_number_of_tasks += 1
        if task.get('completed') is True:
            number_of_done_tasks.append(task)
    print('Employee {} is done with tasks({}/{}):'
          .format(name, len(number_of_done_tasks), total_number_of_tasks))

    for task in number_of_done_tasks:
        print('\t {}'.format(task.get('title')))
