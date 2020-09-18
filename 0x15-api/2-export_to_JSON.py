#!/usr/bin/python3

"""exporting data into json"""

import json
import requests
from sys import argv


def user_employee(user_id):
    """ employes tasks """
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = url + 'users/{}'.format(user_id)
    employee = requests.get(user_url).json()
    task_url = url + 'todos?userId={}'.format(employee.get('id'))
    tasks = requests.get(task_url).json()
    return {"employee": employee, "tasks": tasks}


def json_export(data):
    """Exports to  json"""
    data_id = data.get('employee').get('id')
    data_array = []
    for task in data.get('tasks'):
        data_info = {}
        data_info['task'] = task.get('title')
        data_info['completed'] = task.get('completed')
        data_info['username'] = data.get('employee').get('username')
        data_array.append(data_info)
    data_dict = {data_id: data_array}
    with open('{}.json'.format(data_id), 'w') as json_file:
        json.dump(data_dict, json_file)


if __name__ == '__main__':
    data = user_employee(argv[1])
    json_export(data)
