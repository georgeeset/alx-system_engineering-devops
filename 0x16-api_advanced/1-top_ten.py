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
        "User-Agent": "George Eset alx student task 1",
    }

    # configure for first 10 and global search
    parameter = {
        "limit": "10",
        "q": "GLOBAL",
    }

    response = requests.get(
        url,
        headers=header,
        params=parameter,
        allow_redirects=False
        )
    if response.status_code != 200:
        print("None")
        return
    data = response.json().get("data")
    children = data.get('children')

    for item in children:
        print(item.get('data').get('title'))
