#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TO-DO list progress
"""
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    todo_requests = 'https://jsonplaceholder.typicode.com/todos/'
    user_reuests = 'https://jsonplaceholder.typicode.com/users/'
    todoID = requests.get(todoID_requests, params={'userId': employee_id})
    user = requests.get(user_reuests, params={'id': employee_id})

    todo_list = todoID.json()
    user_dict_list = user.json()

    compleate_task = []
    total_tasks = len(todo_list)
    employee = user_dict_list[0].get('name')

    for task in todo_list:
        if task.get('completed') is True:
            compleate_task.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(compleate_task), total_tasks))

    for task in compleate_task:
        print("\t {}".format(task.get('title')))
