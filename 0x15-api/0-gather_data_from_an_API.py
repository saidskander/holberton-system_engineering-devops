#!/usr/bin/python3
"""Python script that, using this REST API,
   for a given employee ID, returns information
   about his/her TODO list progress"""

from sys import argv
import requests

if __name__ == '__main__':
    userId = argv[1]
    main = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todosid = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    tasks_Done = []
    for task in todosid:
        if task.get('completed') is True:
            tasks_Done.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(main.get('name'), len(tasks_Done), len(todosid)))
    print("\n".join("\t {}".format(task) for task in tasks_Done))
