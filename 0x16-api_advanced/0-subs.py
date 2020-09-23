#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """number_of_subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "win64:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    x = requests.get(url, headers=headers, allow_redirects=False)
    if x.status_code == 404:
        return 0
    results = x.json().get("data")
    return results.get("subscribers")
