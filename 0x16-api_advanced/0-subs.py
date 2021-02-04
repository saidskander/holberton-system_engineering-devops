#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """number_of_subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
         AppleWebKit/537.36 (KHTML, like Gecko)\
         Chrome/197.10.93.189 Safari/537.36"
    }
    x = requests.get(url, headers=headers, allow_redirects=False)
    if x.status_code == 404:
        return 0
    results = x.json().get("data")
    return results.get("subscribers")
