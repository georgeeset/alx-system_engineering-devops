#!/usr/bin/python3
"""
Write a recursive function that queries the
Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], count=0, after=""):
    """recursively query Reddit API for hot articles"""

    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    param = {
       "g": "GLOBAL",
       "after": after,
       "count": count,
       "limit": 100,
    }

    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)

    if response.status_code != 200:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for child in results.get("children"):
        hot_list.append(child.get("data").get("title"))

    if after:
        return recurse(subreddit, hot_list=hot_list, count=count, after=after)
    return hot_list
