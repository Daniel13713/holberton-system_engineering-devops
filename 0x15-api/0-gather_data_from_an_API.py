#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv

id = argv[1]
URL_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(id)
URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)


with requests.session() as session:
    response_tasks = session.get(URL_tasks)
    response_users = session.get(URL_user)
    data_tasks = response_tasks.json()
    data_users = response_users.json()
    name_user = data_users["name"]
    tasks_done = 0
    tasks_all = len(data_tasks)
    tasks_title = ""
    for record in data_tasks:
        if record["completed"]:
            tasks_done += 1
            tasks_title += "\t {}\n".format(record["title"])

    print("Employee {0} is done with tasks({1}/{2}):\n{3}".format(name_user,
          tasks_done, tasks_all, tasks_title), end="")
