#!/usr/bin/python3
"""
 a function that queries the Reddit
 API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
     returns the number of subscribers (not active users,
     total subscribers) for a given subreddit.

     GET /r/subreddit/aboutread
     Return information about the subreddit.
     Data includes the subscriber count,
     description, and header image.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    header = {
        "User-Agent": "George Eset alx student"
    }
    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json().get("data")
    return data.get("subscribers")