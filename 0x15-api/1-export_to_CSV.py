#!/usr/bin/python3
"""Gather data from an API"""

import csv
import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    URL_tasks = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        id)
    URL_user = "https://jsonplaceholder.typicode.com/users/{}".format(id)

    with requests.session() as session:
        data_tasks = session.get(URL_tasks).json()
        data_users = session.get(URL_user).json()
        data = {}
        list_data = []
        for record in data_tasks:
            data["USER_ID"] = id
            data["USERNAME"] = data_users["username"]
            data["TASK_COMPLETED_STATUS"] = record["completed"]
            data["TASK_TITLE"] = record["title"]
            list_data.append(data.copy())

    textFile = "{}.csv".format(id)
    with open(textFile, mode="w+") as csvfile:
        writer = csv.writer(
            csvfile,
            quoting=csv.QUOTE_ALL)
        # Put header of the data in the first row
        # writer.writeheader()
        for data_dict in list_data:
            # Add each dictionary
            writer.writerow(data_dict.values())
