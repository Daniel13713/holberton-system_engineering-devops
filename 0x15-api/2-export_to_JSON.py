#!/usr/bin/python3
"""Gather data from an API"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    URL_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    with requests.session() as session:
        tasks = session.get(URL_tasks).json()
        users = session.get(URL_user).json()

        list_data = []
        for record in tasks:
            completed = record["completed"]
            title = record["title"]
            username = users["id"]
            data = {
                "task": title,
                "completed": completed,
                "username": username}
            list_data.append(data)

        textFile = "{}.json".format(id)
        with open(textFile, mode="w+", encoding="utf-8") as file:
            # write data
            data_id = {id: list_data}
            json.dump(data_id, file)
