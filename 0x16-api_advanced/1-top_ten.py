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
        listing="hot",
        limit=10,
        timeframe="month"
    )
    try:
        with requests.session() as session:
            res = session.get(
                URL, headers={
                    'User-agent': 'yourbot'})
            # Check is subreddit exits
            if res.status_code > 299 and res.status_code < 500:
                print("None")
                return

            data = res.json()
            for post in data["data"]["children"]:
                print(post["data"]["title"])

    except Exception as err:
        print("None")
