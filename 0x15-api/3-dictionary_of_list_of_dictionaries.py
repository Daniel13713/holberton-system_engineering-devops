#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":

    URL_tasks = "https://jsonplaceholder.typicode.com/todos"
    URL_user = "https://jsonplaceholder.typicode.com/users"

    with requests.session() as session:
        tasks = session.get(URL_tasks).json()
        users = session.get(URL_user).json()
        data_id = {}
        for user in users:
            list_data = []
            for record in tasks:
                if record["userId"] == user["id"]:
                    TASK_COMPLETED_STATUS = record["completed"]
                    TASK_TITLE = record["title"]
                    USERNAME = user["username"]
                    data = {
                        "task": TASK_TITLE,
                        "completed": TASK_COMPLETED_STATUS,
                        "username": USERNAME}
                    list_data.append(data)

            data_id.update({user["id"]: list_data})

        textFile = "todo_all_employees.json"
        with open(textFile, mode="w+", encoding="utf-8") as file:
            # write data
            json.dump(data_id, file)
