#!/usr/bin/python3
"""
 a function that queries the Reddit API and prints the titles of the first
 10 hot posts listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Print the titles of the first 10 hot posts listed
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    header = {
        "User-Agent": "George Eset alx student",
    }

    param = {
        "limit": "10",
        "q": "GLOBAL",
    }

    response = requests.get(
        url,
        headers=header,
        params=param,
        allow_redirects=False
        )
    if response.status_code != 200:
        print(response.status_code)
        return 0
    data = response.json().get("data")
    children = data.get('children')

    for child in children:
        print(child.get('data').get('title'))
