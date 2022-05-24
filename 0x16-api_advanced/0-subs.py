#!/usr/bin/python3
""" Number of subscribers for a user on reddit """

import requests


def number_of_subscribers(subreddit):
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
                    'User-agent': 'yourbot'}).json()
            num = res["data"]["children"][0]["data"]["subreddit_subscribers"]
            return num
    except Exception as err:
        return 0
