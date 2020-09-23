#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """number_of_subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {
        "User-Agent": "win64:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    x = requests.get(url, headers=headers).json().get('data')
    if x:
        return x.get('subscribers')
    return 0
