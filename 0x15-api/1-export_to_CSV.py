#!/usr/bin/python3
"""Export to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    employee_id = argv[1]
    employee_name = requests.get(url + '/users/{}'.format(employee_id)).json()
    amount = requests.get(url + '/todos?userId={}'.format(employee_id)).json()
    username = employee_name.get('username')

    filename = '{}.csv'.format(employee_id)
    with open(filename, 'w', newline='') as file:
        w = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in amount:
            w.writerow([employee_id, username,
                        task.get('completed'), task.get('title')])
