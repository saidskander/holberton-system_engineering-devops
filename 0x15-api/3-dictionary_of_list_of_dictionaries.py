#!/usr/bin/python3
"""json req"""
import json
import requests as req


if __name__ == "__main__":
    enddict = {}
    newlist = []
    user = req.get("https://jsonplaceholder.typicode.com/users").json()
    todoID = req.get("https://jsonplaceholder.typicode.com/todos").json()
    user_dict_list = {}
    for person in user:
        for task in todoID:
            if person["id"] == task["userId"]:
                user_dict_list["task"] = task["title"]
                user_dict_list["completed"] = task["completed"]
                user_dict_list["username"] = person["username"]
                newlist.append(user_dict_list)
        enddict[person["id"]] = newlist

    with open("todo_all_employees.json", 'w') as x:
        json.dump(enddict, x)
