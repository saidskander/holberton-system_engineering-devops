#!/usr/bin/python3
"""
Python script that, using this REST API,
for a given employee ID, returns information
about his/her TO-DO list progress / CSV format
"""
import csv
import requests
from sys import argv

if __name__ == '__main__':
    employee_id = argv[1]
    todo_requests = 'https://jsonplaceholder.typicode.com/todos/'
    user_reuests = 'https://jsonplaceholder.typicode.com/users/'
    todo = requests.get(todo_requests, params={'userId': employee_id})
    user = requests.get(user_reuests, params={'id': employee_id})

    todo_list = todo.json()
    user_dict_list = user.json()

    employee = user_dict_list[0].get('username')

    with open("{}.csv".format(employee_id), "a+") as csvfile:
        csvemployee = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            completed_status = task['completed']
            completed_title = task['title']
            csvemployee.writerow(["{}".format(employee_id),
                                "{}".format(employee),
                                "{}".format(completed_status),
                                "{}".format(completed_title)])
