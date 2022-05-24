#!/usr/bin/python3
""" Number of subscribers for a user on reddit """

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    ---------------------------------------
    Return all hot titles of the subreddit
    ---------------------------------------
    """
    URL = "https://www.reddit.com/r/{subreddit}/hot.json".format(
        subreddit=subreddit)
    params = {
        'limit': 100,
        'after': after
    }
    headers = {'User-agent': 'yourbot'}
    try:
        with requests.session() as session:
            res = session.get(
                URL,
                headers=headers,
                params=params,
                allow_redirects=False)
            # Check is subreddit exits
            if res.status_code is 404:
                return None

            data = res.json()
            # apartir de este valor hará el nuevo request
            after = data["data"]["after"]
            for post in data["data"]["children"]:
                hot_list.append(post["data"]["title"])

        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list

    except Exception as err:
        return None
