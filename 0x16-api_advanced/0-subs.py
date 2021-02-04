#!/usr/bin/python3
import requests
"""subscribers"""


def number_of_subscribers(subreddit):
    """ Returns number of subscribers """
    r = requests.get("https://reddit.com/r/{}/about.json".format(subreddit),
                     headers={"User-Agent": "custum"})
    if (r.status_code == 200):
        return r.json().get("data").get("subscribers")
    else:
        return 0
