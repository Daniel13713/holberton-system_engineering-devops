#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":

    URL_tasks = "https://jsonplaceholder.typicode.com/todos"
    URL_users = "https://jsonplaceholder.typicode.com/users"

    with requests.session() as session:
        response_tasks = session.get(URL_tasks)
        response_users = session.get(URL_users)
        data_tasks = response_tasks.json()
        data_users = response_users.json()
        data = "{"
        user_all = len(data_users)
        for user in data_users:
            username = user["username"]
            tasks_done = 0
            tasks_all = len(data_tasks)
            data += '"{}": ['.format(user["id"])
            for record in data_tasks:
                if record["userId"] == user["id"]:
                    completed = str(record["completed"]).lower()
                    title = record["title"]
                    data += """
                    {{"username": "{2}", "task": "{0}", "completed": {1}}}
                    """.format(
                        title, completed, username)
                    data += ", "
            data = data[:-2]
            if data_users[user_all - 1] != user:
                data += "], "
            else:
                data += "]"
        data += "}"

    textFile = "todo_all_employees.json"
    with open(textFile, mode="w+", encoding="utf-8") as file:
        file.write(data)
