#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """number_of_subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
             AppleWebKit/537.36 (KHTML, like Gecko)\
             Chrome/85.0.4183.121 Safari/537.36"
    headers = {"User-Agent": agent}
    x = requests.get(url, headers=headers).json().get('data')
    if x:
        return x.get('subscribers')
    return 0
