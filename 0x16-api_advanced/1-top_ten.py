#!/usr/bin/python3
""" Number of subscribers for a user on reddit """

import requests


def top_ten(subreddit):
    """
    ------------------------------
    GET request to subreddit user
    ------------------------------
    """
    URL = """
        https://www.reddit.com/r/{subreddit}/{listing}.json?limit={limit}&t={timeframe}
        """.format(
        subreddit=subreddit,
        listing="top",
        limit=100,
        timeframe="month"
    )
    try:
        with requests.session() as session:
            res = session.get(
                URL, headers={
                    'User-agent': 'yourbot'})
            data = res.json()
            # check if a valid subreddit
            data["data"]["children"][0]["data"]
            for post in data["data"]["children"][0:10]:
                print(post["data"]["title"])

    except Exception as err:
        print("None")
