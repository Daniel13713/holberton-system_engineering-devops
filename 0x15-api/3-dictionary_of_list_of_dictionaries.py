#!/usr/bin/python3
"""Gather data from an API"""

import requests
from sys import argv

if __name__ == "__main__":
    data = "{"
    for id in range(1, 11):
        URL_tasks = """
                https://jsonplaceholder.typicode.com/users/{}/todos
                    """.format(id)
        URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)

        with requests.session() as session:
            response_tasks = session.get(URL_tasks)
            response_users = session.get(URL_user)
            data_tasks = response_tasks.json()
            data_users = response_users.json()
            username = data_users["username"]
            tasks_done = 0
            tasks_all = len(data_tasks)
            data += '"{}": ['.format(id)
            for record in data_tasks:
                completed = str(record["completed"]).lower()
                title = record["title"]
                data += """
                {{"username": "{2}", "task": "{0}", "completed": {1}}}
                """.format(
                    title, completed, username)
                if data_tasks[tasks_all - 1] != record:
                    data += ", "
            if id != 10:
                data += "], "
            else:
                data += "]"
    data += "}"

    textFile = "todo_all_employees.json"
    with open(textFile, mode="w+", encoding="utf-8") as file:
        file.write(data)
